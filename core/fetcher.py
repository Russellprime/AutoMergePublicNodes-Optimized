"""
Public source fetcher.
- Async concurrent fetch
- Dynamic URL support (date templates like %Y/%m/%d)
- List source support (a source that returns child source URLs)
- Retry handling
"""
from __future__ import annotations

import asyncio
import datetime
import logging
import re
from dataclasses import dataclass, field
from typing import List, Set, Tuple

logger = logging.getLogger(__name__)

import aiohttp
import yaml

from core.parser import Node, parse_content


@dataclass
class Source:
    url: str
    name: str = ""                # 来源名称
    kind: str = "url"             # url | dynamic | list
    enabled: bool = True
    ignore_protocols: Set[str] = field(default_factory=set)
    max_nodes: int = 0            # 0 表示不限

    @property
    def resolved_url(self) -> str:
        """处理动态 URL（日期模板）"""
        if "%" not in self.url:
            return self.url
        now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
        return now.strftime(self.url)


@dataclass
class FetchResult:
    source: Source
    success: bool = False
    nodes: List[Node] = field(default_factory=list)
    error: str = ""
    duration: float = 0.0
    bytes_received: int = 0


JSDELIVR_RE = re.compile(r"https?://raw\.githubusercontent\.com/([^/]+)/([^/]+)/(?:refs/heads/)?([^/]+)/(.+)")

# §2.6 单源最大下载字节数, 超过直接 reject, 防止恶意源喂大文件吃光内存
MAX_FETCH_BYTES = 20 * 1024 * 1024


def to_jsdelivr(url: str) -> str:
    """将 raw.githubusercontent.com 转 jsdelivr CDN（国内更稳定）"""
    m = JSDELIVR_RE.match(url)
    if not m:
        return url
    user, repo, branch, path = m.groups()
    return f"https://cdn.jsdelivr.net/gh/{user}/{repo}@{branch}/{path}"


async def _fetch_one(session: aiohttp.ClientSession, url: str, timeout: int = 15, retries: int = 2) -> Tuple[bool, str, int]:
    """抓取单个 URL，返回 (成功, 内容/错误, 字节数)，带重试"""
    last_err = ""
    for attempt in range(retries + 1):
        try:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=timeout)) as resp:
                if resp.status != 200:
                    last_err = f"HTTP {resp.status}"
                    if resp.status == 429 and attempt < retries:
                        await asyncio.sleep(1.5 * (attempt + 1))
                        continue
                    return False, last_err, 0
                data = bytearray()
                async for chunk in resp.content.iter_chunked(65536):
                    data.extend(chunk)
                    if len(data) > MAX_FETCH_BYTES:
                        return False, f"too-large:>{MAX_FETCH_BYTES}", 0
                try:
                    text = data.decode("utf-8", errors="replace")
                except Exception:
                    text = ""
                return True, text, len(data)
        except asyncio.TimeoutError:
            last_err = "timeout"
            if attempt < retries:
                await asyncio.sleep(0.5 * (attempt + 1))
                continue
            return False, "timeout", 0
        except Exception as e:
            last_err = str(e)[:100]
            if attempt < retries:
                await asyncio.sleep(0.5 * (attempt + 1))
                continue
            return False, last_err, 0
    return False, last_err, 0


async def fetch_source(
    session: aiohttp.ClientSession,
    src: Source,
    timeout: int = 15,
    retries: int = 2,
) -> FetchResult:
    """抓取单个订阅源"""
    start = asyncio.get_event_loop().time()
    result = FetchResult(source=src)

    url = src.resolved_url

    # Try original URL first, then jsDelivr fallback.
    candidates = [url]
    cdn = to_jsdelivr(url)
    if cdn != url:
        candidates.append(cdn)

    last_err = ""
    text = ""
    for candidate in candidates:
        ok, content, n_bytes = await _fetch_one(session, candidate, timeout, retries=max(retries, 0))
        if ok:
            text = content
            result.bytes_received = n_bytes
            break
        last_err = content

    if not text:
        result.error = last_err
        result.duration = asyncio.get_event_loop().time() - start
        return result

    # List source: each line is another URL.
    if src.kind == "list":
        sub_urls = []
        for line in text.splitlines():
            line = line.strip()
            if line and "://" in line and not line.startswith("#"):
                sub_urls.append(line)
        # Fetch one depth of child URLs with bounded concurrency.
        list_sem = asyncio.Semaphore(10)

        async def _fetch_sub(sub_url: str) -> List[Node]:
            async with list_sem:
                ok, content, _ = await _fetch_one(session, sub_url, timeout, retries=max(retries, 0))
                return parse_content(content) if ok else []

        sub_results = await asyncio.gather(*[_fetch_sub(u) for u in sub_urls[:50]])
        for sub_nodes in sub_results:
            result.nodes.extend(sub_nodes)
    else:
        result.nodes = parse_content(text)

    # Protocol filter
    if src.ignore_protocols:
        result.nodes = [n for n in result.nodes if n.type not in src.ignore_protocols]

    # Per-source node cap
    if src.max_nodes > 0 and len(result.nodes) > src.max_nodes:
        result.nodes = result.nodes[:src.max_nodes]

    result.success = True
    result.duration = asyncio.get_event_loop().time() - start
    return result


async def fetch_all(
    sources: List[Source],
    concurrency: int = 30,
    timeout: int = 15,
    overall_timeout: int = 120,
    retries: int = 2,
    rate_limit_per_sec: float = 0.0,
) -> List[FetchResult]:
    """Fetch all enabled sources with bounded concurrency and optional rate limit."""
    sem = asyncio.Semaphore(concurrency)
    connector = aiohttp.TCPConnector(limit=concurrency * 2)
    headers = {
        "User-Agent": "ClashforWindows/0.20.39 (clash-meta)",
        "Accept": "*/*",
    }

    rate_lock = asyncio.Lock()
    next_allowed_at = 0.0

    async def _wrapped(session, src):
        nonlocal next_allowed_at
        async with sem:
            if rate_limit_per_sec > 0:
                min_interval = 1.0 / rate_limit_per_sec
                async with rate_lock:
                    now = asyncio.get_event_loop().time()
                    wait_for = max(0.0, next_allowed_at - now)
                    if wait_for > 0:
                        await asyncio.sleep(wait_for)
                    next_allowed_at = asyncio.get_event_loop().time() + min_interval
            return await fetch_source(session, src, timeout, retries=max(retries, 0))

    async with aiohttp.ClientSession(connector=connector, headers=headers) as session:
        async def _fetch_one_source(src: Source) -> FetchResult:
            # Keep retries bounded and isolated per source.
            for attempt in range(max(retries, 0) + 1):
                result = await _wrapped(session, src)
                if getattr(result, "success", False) or attempt >= retries:
                    return result
            return FetchResult(source=src, success=False, error="exhausted")

        tasks = [asyncio.create_task(_fetch_one_source(s)) for s in sources if s.enabled]
        try:
            return await asyncio.wait_for(asyncio.gather(*tasks), timeout=overall_timeout)
        except asyncio.TimeoutError:
            logger.warning("fetch_all overall timeout (%ss), returning partial results", overall_timeout)
            done_results = []
            for t in tasks:
                if t.done() and not t.cancelled() and t.exception() is None:
                    done_results.append(t.result())
            for t in tasks:
                if not t.done():
                    t.cancel()
            await asyncio.gather(*tasks, return_exceptions=True)
            return done_results


def load_sources(path: str) -> List[Source]:
    """Load source definitions from YAML and deduplicate malformed/duplicate entries."""
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    sources: List[Source] = []
    seen_urls: Set[str] = set()
    seen_names: Set[str] = set()
    for entry in data.get("sources", []):
        if isinstance(entry, str):
            url = entry.strip()
            if not url:
                continue
            if url in seen_urls:
                continue
            seen_urls.add(url)
            sources.append(Source(url=url))
        elif isinstance(entry, dict):
            url = str(entry.get("url", "")).strip()
            if not url:
                logger.warning("Skipping malformed source without URL: %s", entry)
                continue
            name = str(entry.get("name", "")).strip()
            if url in seen_urls:
                continue
            if name and name in seen_names:
                logger.warning("Duplicate source name skipped: %s", name)
                continue
            src = Source(
                url=url,
                name=name,
                kind=entry.get("kind", "url"),
                enabled=entry.get("enabled", True),
                ignore_protocols=set(entry.get("ignore_protocols", [])),
                max_nodes=int(entry.get("max_nodes", 0)),
            )
            seen_urls.add(url)
            if name:
                seen_names.add(name)
            sources.append(src)
        else:
            logger.warning("Skipping malformed source entry: %r", entry)
    return sources
