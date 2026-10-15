"""Clean public IP detection with early stop."""
from __future__ import annotations

import asyncio
import ipaddress
import socket
import time
from typing import Dict, Iterable, List, Sequence, Tuple

from core.parser import Node
from core.filtering import is_ssrf_target


def _is_public_ip(value: str) -> bool:
    try:
        ip = ipaddress.ip_address(value)
    except ValueError:
        return False
    return (
        not ip.is_private
        and not ip.is_loopback
        and not ip.is_multicast
        and not ip.is_reserved
        and not ip.is_unspecified
        and not ip.is_link_local
        and not is_ssrf_target(value)
    )


async def _resolve_host_ips(host: str, port: int, timeout: float) -> List[str]:
    try:
        infos = await asyncio.wait_for(
            asyncio.get_event_loop().getaddrinfo(host, port, type=socket.SOCK_STREAM),
            timeout=timeout,
        )
    except Exception:
        return []
    ips: List[str] = []
    seen = set()
    for info in infos:
        ip = info[4][0]
        if ip in seen:
            continue
        seen.add(ip)
        ips.append(ip)
    return ips


async def extract_candidate_ips(
    nodes: Sequence[Node],
    *,
    resolve_timeout: float = 2.0,
    resolve_concurrency: int = 50,
) -> List[str]:
    """Extract public candidate IPs from node servers in stable order."""
    sem = asyncio.Semaphore(max(1, resolve_concurrency))
    seen = set()
    out: List[str] = []

    async def _resolve(node: Node) -> List[str]:
        server = (node.server or "").strip()
        if not server:
            return []
        if _is_public_ip(server):
            return [server]
        async with sem:
            ips = await _resolve_host_ips(server, node.server_port, resolve_timeout)
            return [ip for ip in ips if _is_public_ip(ip)]

    resolved = await asyncio.gather(*[_resolve(node) for node in nodes], return_exceptions=False)
    for ip_list in resolved:
        for ip in ip_list:
            if ip in seen:
                continue
            seen.add(ip)
            out.append(ip)
    return out


async def probe_clean_ips(
    candidates: Sequence[str],
    *,
    target: int = 20,
    timeout: float = 2.0,
    concurrency: int = 50,
    port: int = 443,
    max_latency_ms: float = 800.0,
) -> Tuple[List[Tuple[str, float]], Dict[str, int]]:
    """Probe public IP candidates and stop launching probes when target is met."""
    if target <= 0 or not candidates:
        return [], {"candidates": len(candidates), "tested": 0, "success": 0}

    idx = 0
    index_lock = asyncio.Lock()
    found: List[Tuple[str, float]] = []
    found_set = set()
    stats = {"candidates": len(candidates), "tested": 0, "success": 0}

    async def _worker() -> None:
        nonlocal idx
        while True:
            async with index_lock:
                if len(found) >= target or idx >= len(candidates):
                    return
                ip = candidates[idx]
                idx += 1
                stats["tested"] += 1
            started = time.perf_counter()
            writer = None
            try:
                _, writer = await asyncio.wait_for(asyncio.open_connection(ip, port), timeout=timeout)
                lat_ms = (time.perf_counter() - started) * 1000.0
                if max_latency_ms > 0 and lat_ms > max_latency_ms:
                    continue
                async with index_lock:
                    if len(found) >= target:
                        return
                    if ip in found_set:
                        continue
                    found_set.add(ip)
                    found.append((ip, lat_ms))
                    stats["success"] += 1
            except Exception:
                continue
            finally:
                if writer:
                    writer.close()
                    try:
                        await writer.wait_closed()
                    except Exception:
                        pass

    worker_count = min(max(1, concurrency), len(candidates))
    await asyncio.gather(*[asyncio.create_task(_worker()) for _ in range(worker_count)])
    found.sort(key=lambda row: (row[1], row[0]))
    return found[:target], stats

