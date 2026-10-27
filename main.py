#!/usr/bin/env python3
"""
autonodes entrypoint.
Pipeline:
1) fetch all public sources (async)
2) parse nodes across supported protocols
3) deduplicate + TCP pre-check
4) run real proxy tests via sing-box
5) score/rank and keep Top N
6) generate subscription outputs
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import socket
import sys
import time
from pathlib import Path
from dataclasses import replace
from typing import Dict, List, Tuple, Any

# 让脚本能直接运行
sys.path.insert(0, str(Path(__file__).resolve().parent))

__version__ = "2.5.0"

from core.fetcher import fetch_all, load_sources
from core.geo import geo_flag_map, flag_for_server
from core.parser import Node
from core.filtering import load_filter_rules, quality_prefilter, filter_ssrf, is_ssrf_target
from core.sampling import protocol_priority, sample_for_real_test, sample_for_real_test_weighted
from core.stats import build_source_scores, load_historical_pass_rates, update_trend_history, update_node_stability, load_node_stability, get_stable_nodes
from core.scoring import ScoreInput, calculate_score, calculate_score_breakdown, load_scoring_config
from core.report import write_health_report
from core.readme_updater import update_readme_stats
from core.clean_ip import extract_candidate_ips, probe_clean_ips
from core.generator import node_to_url

try:
    import yaml
except Exception:  # pragma: no cover
    yaml = None


def load_runtime_config(path: str) -> Dict[str, Any]:
    if not path or yaml is None:
        return {}
    runtime_path = Path(path)
    if not runtime_path.exists():
        return {}
    try:
        data = yaml.safe_load(runtime_path.read_text(encoding="utf-8")) or {}
    except Exception:
        return {}
    return data if isinstance(data, dict) else {}


def apply_runtime_overrides(args: argparse.Namespace, cfg: Dict[str, Any]) -> None:
    mapping = {
        "top_n": "top_n",
        "top_links_path": "top_links_path",
        "clean_ip_output": "clean_ip_output",
        "fetch_concurrency": "fetch_concurrency",
        "fetch_timeout": "fetch_timeout",
        "fetch_overall_timeout": "fetch_overall_timeout",
        "fetch_retries": "fetch_retries",
        "fetch_rate_limit_per_sec": "fetch_rate_limit_per_sec",
        "tcp_concurrency": "tcp_concurrency",
        "tcp_timeout": "tcp_timeout",
        "test_concurrency": "test_concurrency",
        "test_timeout": "test_timeout",
        "test_limit": "test_limit",
        "probe_concurrency": "probe_concurrency",
        "probe_timeout": "probe_timeout",
        "probe_count": "probe_count",
        "test_retries": "test_retries",
        "speed_test_enabled": "speed_test_enabled",
        "speed_test_bytes": "speed_test_bytes",
        "global_output": "global_output",
        "china_check": "china_check",
        "real_test": "real_test",
        "lightweight_probe": "lightweight_probe",
        "quality_filter": "quality_filter",
        "max_latency_ms": "max_latency_ms",
        "min_speed_kbps": "min_speed_kbps",
        "clean_ip_target": "clean_ip_target",
        "clean_ip_concurrency": "clean_ip_concurrency",
        "clean_ip_timeout": "clean_ip_timeout",
        "clean_ip_port": "clean_ip_port",
        "clean_ip_max_latency_ms": "clean_ip_max_latency_ms",
    }
    for key, attr in mapping.items():
        if key in cfg and getattr(args, attr, None) is not None:
            setattr(args, attr, cfg[key])


def dedupe(nodes: List[Node]) -> List[Node]:
    seen = set()
    out = []
    for n in nodes:
        fp = n.fingerprint()
        if fp in seen:
            continue
        seen.add(fp)
        out.append(n)
    return out



def build_output_nodes(valid: List[tuple], flag_map: Dict[str, str], top_n: int) -> List[Node]:
    output_nodes: List[Node] = []
    for i, (n, lat, jit) in enumerate(valid[:top_n], 1):
        flag = flag_for_server(n.server, flag_map)
        prefix = f"{flag} " if flag else ""
        new_tag = n.tag
        if lat > 0:
            jitter_str = f" +/-{jit:.0f}ms" if jit > 0 else ""
            new_tag = f"{prefix}[{lat:>5.1f}ms{jitter_str}] {n.tag}"
        output_nodes.append(replace(n, tag=new_tag))
    return output_nodes




def count_existing_urls(output_dir: str, prefix: str) -> int:
    path = Path(output_dir) / f"{prefix}.urls"
    if not path.exists():
        return 0
    try:
        return sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.strip())
    except Exception:
        return 0


def should_preserve_previous_output(new_count: int, previous_count: int, min_retain_ratio: float) -> bool:
    if previous_count <= 0 or min_retain_ratio <= 0:
        return False
    return new_count < int(previous_count * min_retain_ratio)


async def _resolve_and_check_ssrf(server: str, port: int, timeout: float) -> bool:
    """解析域名并检查是否命中 SSRF。返回 True=应拦截。抽成独立函数以便测试 mock。"""
    try:
        infos = await asyncio.wait_for(
            asyncio.get_event_loop().getaddrinfo(
                server, port, type=socket.SOCK_STREAM),
            timeout=timeout)
    except Exception:
        return False  # 解析失败交给 open_connection 处理，不在此拦截
    return any(is_ssrf_target(info[4][0]) for info in infos)


async def tcp_check_batch(
    nodes: List[Node],
    concurrency: int = 200,
    timeout: float = 3.0,
    error_counts: Dict[str, int] | None = None,
) -> List[Tuple[Node, float]]:
    """快速 TCP 预筛选：返回 [(node, tcp_latency_ms)]，按延迟升序。

    可选 error_counts 用于记录失败异常类型，便于 stats/health report 定位网络问题。
    """
    queue: asyncio.Queue[Node] = asyncio.Queue()
    for n in nodes:
        queue.put_nowait(n)

    ok: List[Tuple[Node, float]] = []
    errors = error_counts if error_counts is not None else {}

    async def _worker():
        while True:
            try:
                n = queue.get_nowait()
            except asyncio.QueueEmpty:
                return
            t0 = time.perf_counter()
            writer = None
            try:
                # SSRF 纵深防御：域名先解析，对每个解析出的 IP 跑 is_ssrf_target。
                # filter_ssrf 只拦字面 IP，恶意域名 DNS 到内网 IP 会绕过它。
                if await _resolve_and_check_ssrf(n.server, n.server_port, timeout):
                    errors["SSRFBlocked"] = errors.get("SSRFBlocked", 0) + 1
                    continue
                fut = asyncio.open_connection(n.server, n.server_port)
                _, writer = await asyncio.wait_for(fut, timeout=timeout)
                lat_ms = (time.perf_counter() - t0) * 1000
                ok.append((n, lat_ms))
            except Exception as exc:
                key = type(exc).__name__
                errors[key] = errors.get(key, 0) + 1
            finally:
                if writer:
                    writer.close()
                    try:
                        await writer.wait_closed()
                    except Exception:
                        pass
                queue.task_done()

    worker_count = min(max(concurrency, 1), len(nodes))
    if worker_count > 0:
        await asyncio.gather(*[asyncio.create_task(_worker()) for _ in range(worker_count)])
    ok.sort(key=lambda x: x[1])
    return ok


async def run(args):
    t0 = time.time()
    stage_durations: Dict[str, float] = {}
    stage_start = t0
    print("╔══════════════════════════════════════════════╗")
    print("║  autonodes - public node pipeline            ║")
    print("╚══════════════════════════════════════════════╝\n")

    fetch_retries = int(getattr(args, "fetch_retries", 2))
    fetch_rate_limit_per_sec = float(getattr(args, "fetch_rate_limit_per_sec", 0.0))
    probe_count = int(getattr(args, "probe_count", 3))
    test_retries = int(getattr(args, "test_retries", 0))
    speed_test_enabled = bool(getattr(args, "speed_test_enabled", True))
    speed_test_bytes = int(getattr(args, "speed_test_bytes", 102400))
    max_latency_ms = float(getattr(args, "max_latency_ms", 0.0))
    min_speed_kbps = float(getattr(args, "min_speed_kbps", 0.0))
    top_links_path_value = str(getattr(args, "top_links_path", "200_links.txt"))
    clean_ip_output_value = str(getattr(args, "clean_ip_output", "clean_ips_20.txt"))
    clean_ip_target = int(getattr(args, "clean_ip_target", 20))
    clean_ip_concurrency = int(getattr(args, "clean_ip_concurrency", 60))
    clean_ip_timeout = float(getattr(args, "clean_ip_timeout", 2.0))
    clean_ip_port = int(getattr(args, "clean_ip_port", 443))
    clean_ip_max_latency_ms = float(getattr(args, "clean_ip_max_latency_ms", 800.0))
    clean_ip_resolve_timeout = float(getattr(args, "clean_ip_resolve_timeout", 2.0))
    clean_ip_resolve_concurrency = int(getattr(args, "clean_ip_resolve_concurrency", 60))

    # 1) 加载订阅源
    sources = load_sources(args.sources)
    scoring_rules_path = getattr(args, "scoring_rules", "config/scoring.yaml")
    scoring_config = load_scoring_config(scoring_rules_path)
    protocol_rates, source_rates = load_historical_pass_rates(args.output_dir)
    print(f"[1/7] Loaded {len(sources)} source entries")
    if protocol_rates or source_rates:
        print(f"      Historical pass rates: {len(source_rates)} sources, {len(protocol_rates)} protocols")

    # 2) 抓取
    print(f"[2/7] Fetching sources (concurrency={args.fetch_concurrency}, overall_timeout={args.fetch_overall_timeout}s)")
    fetch_kwargs = {
        "concurrency": args.fetch_concurrency,
        "timeout": args.fetch_timeout,
        "overall_timeout": args.fetch_overall_timeout,
    }
    if hasattr(args, "fetch_retries"):
        fetch_kwargs["retries"] = fetch_retries
    if hasattr(args, "fetch_rate_limit_per_sec"):
        fetch_kwargs["rate_limit_per_sec"] = fetch_rate_limit_per_sec
    fr_list = await fetch_all(sources, **fetch_kwargs)
    stage_durations["fetch"] = round(time.time() - stage_start, 1)
    stage_start = time.time()

    total_raw = sum(len(r.nodes) for r in fr_list)
    healthy = sum(1 for r in fr_list if r.success and len(r.nodes) > 0)
    print(f"      Fetch complete: healthy={healthy}/{len(sources)}, raw_nodes={total_raw}")
    print(f"[funnel] stage=fetch in=0 out={total_raw}")

    all_nodes: List[Node] = []
    proto_count: Dict[str, int] = {}
    source_nodes: Dict[str, int] = {}
    source_dead_counts: Dict[str, int] = {}
    # 跟踪每个节点来自哪个 source（用于 per-source 通过率统计）
    node_source_map: Dict[str, str] = {}  # fingerprint -> source_name
    for r in fr_list:
        src_name = r.source.name or r.source.url[:80]
        source_nodes[src_name] = source_nodes.get(src_name, 0) + len(r.nodes)
        if not r.success or len(r.nodes) == 0:
            source_dead_counts[src_name] = 1
        for n in r.nodes:
            all_nodes.append(n)
            proto_count[n.type] = proto_count.get(n.type, 0) + 1
            node_source_map.setdefault(n.fingerprint(), src_name)

    # 3) Deduplicate collected nodes
    nodes = dedupe(all_nodes)
    dedup_pool = list(nodes)  # 保存完整 deduped 池(8K+),供 all.* 输出

    # GeoIP flag mapping
    print("      GeoIP lookup (batch ip-api.com)...")
    flag_map = await geo_flag_map(all_nodes)
    stage_durations["geo"] = round(time.time() - stage_start, 1)
    stage_start = time.time()
    print(f"      Flag map entries: {len(flag_map)} IPs")

    print(f"[3/7] Deduplicated nodes: {len(all_nodes)} -> {len(nodes)}")
    print(f"[funnel] stage=dedup in={len(all_nodes)} out={len(nodes)}")
    for k, v in sorted(proto_count.items(), key=lambda x: -x[1]):
        print(f"        {k:14s}: {v}")

    # 3.4) SSRF defense
    nodes, ssrf_dropped = filter_ssrf(nodes)
    if ssrf_dropped > 0:
        print(f"[3.4] SSRF blocked: removed {ssrf_dropped} private/metadata targets")

    filter_rule_hits: Dict[str, int] = {}
    # 3.5) Optional quality pre-filter
    if args.quality_filter:
        before = len(nodes)
        filter_rules = load_filter_rules(args.filter_rules)
        nodes, filter_rule_hits = quality_prefilter(nodes, max_per_server=args.max_per_server, rules=filter_rules, protocol_priority=protocol_priority)
        mode = str(filter_rules.get("mode", "block"))
        hit_summary = ", ".join(f"{k}={v}" for k, v in sorted(filter_rule_hits.items(), key=lambda x: -x[1])[:5])
        suffix = f"; rule hits: {hit_summary}" if hit_summary else ""
        if args.max_per_server > 0:
            print(f"[3.5] Quality filter (mode={mode}, max_per_server={args.max_per_server}): {before} -> {len(nodes)}{suffix}")
        else:
            print(f"[3.5] Quality filter (mode={mode}, no per-server cap): {before} -> {len(nodes)}{suffix}")
    else:
        print("[3.5] Skipped quality filter")

    # 4) TCP pre-check
    tcp_errors: Dict[str, int] = {}
    if args.tcp_check:
        print(f"[4/7] TCP pre-check (concurrency={args.tcp_concurrency}, timeout={args.tcp_timeout}s)")
        tcp_results = await tcp_check_batch(nodes, args.tcp_concurrency, args.tcp_timeout, tcp_errors)
        stage_durations["tcp"] = round(time.time() - stage_start, 1)
        stage_start = time.time()
        nodes_tcp_reachable = len(tcp_results)  # TCP 真实可达数(下采样前)
        print(f"      TCP reachable: {nodes_tcp_reachable}")
        print(f"[funnel] stage=tcp out={nodes_tcp_reachable}")
        if tcp_errors:
            _tcp_top = sorted(tcp_errors.items(), key=lambda x: -x[1])[:5]
            print(f"      TCP error top: {', '.join(f'{k}={v}' for k, v in _tcp_top)}")
        nodes = [n for n, _ in tcp_results]
        tcp_latency = {n.fingerprint(): lat for n, lat in tcp_results}
    else:
        print("[4/7] Skipped TCP pre-check")
        tcp_latency = {}
        stage_durations["tcp"] = 0.0
        stage_start = time.time()

    # 限制送入真实测试的数量（控制时间）
    if args.test_limit > 0 and len(nodes) > args.test_limit:
        before_sample = len(nodes)
        nodes = sample_for_real_test_weighted(nodes, tcp_latency, args.test_limit, node_source_map, protocol_rates, source_rates)
        print(f"      Sampled for real-test: {before_sample} -> {len(nodes)}")

    # 4.5) Optional lightweight probe
    nodes_before_probe = len(nodes)  # TCP 后、probe 前的节点数
    probe_error_top = []  # 防御性初始化：nodes 为空时 580 行引用不崩溃
    if args.lightweight_probe and args.real_test and nodes:
        from core.tester import SingBoxTester
        print(f"[4.5/7] Lightweight probe (concurrency={args.probe_concurrency}, timeout={args.probe_timeout}s)")
        probe_tester = SingBoxTester(
            sb_path=args.singbox,
            concurrency=args.probe_concurrency,
            startup_wait=args.probe_startup_wait,
            request_timeout=args.probe_timeout,
            min_latency_ms=0,
            probe_only=True,
            probe_count=max(1, probe_count),
            retries=max(0, test_retries),
            enable_speed_test=False,
        )
        probe_results = await probe_tester.test_all(nodes, progress_every=100)
        probe_pass_fps = {r.node.fingerprint() for r in probe_results if r.success}
        before_probe = len(nodes)
        nodes = [n for n in nodes if n.fingerprint() in probe_pass_fps]
        stage_durations["probe"] = round(time.time() - stage_start, 1)
        stage_start = time.time()
        print(f"      Probe passed: {len(nodes)}/{before_probe}")
        print(f"[funnel] stage=probe in={before_probe} out={len(nodes)}")
        # 记录 probe 失败原因分布, 填补可观测性空白
        probe_error_counts: Dict[str, int] = {}
        for r in probe_results:
            if not r.success and r.error:
                key = r.error.split(":")[0] if ":" in r.error else r.error
                probe_error_counts[key] = probe_error_counts.get(key, 0) + 1
        probe_error_top = sorted(probe_error_counts.items(), key=lambda x: -x[1])[:10]
        if probe_error_top:
            print(f"      Probe failures top: {', '.join(f'{k}={v}' for k, v in probe_error_top)}")
    nodes_after_probe = len(nodes)  # probe 后的节点数

    # 5) Real proxy test (sing-box)
    valid: List[tuple] = []  # [(node, latency_ms, jitter_ms)]
    scored_valid: List[tuple] = []  # [(node, latency_ms, jitter_ms, score, source, breakdown)]
    results = []  # 保存全部测试结果（含失败），供统计使用
    cn_block_retry_results = []
    cn_block_retry_valid: List[tuple] = []
    real_test_passed = False
    if args.real_test and nodes:
        from core.tester import SingBoxTester
        print(f"[5/7] sing-box real test (concurrency={args.test_concurrency})")
        tester = SingBoxTester(
            sb_path=args.singbox,
            concurrency=args.test_concurrency,
            startup_wait=args.startup_wait,
            request_timeout=args.test_timeout,
            min_latency_ms=args.min_latency,
            probe_count=max(1, probe_count),
            retries=max(0, test_retries),
            enable_speed_test=speed_test_enabled,
            speed_test_bytes=speed_test_bytes,
        )
        results = await tester.test_all(nodes)
        if test_retries > 0:
            best_by_fp = {r.node.fingerprint(): r for r in results}
            for _ in range(test_retries):
                retry_nodes = [r.node for r in best_by_fp.values() if not r.success]
                if not retry_nodes:
                    break
                retry_results = await tester.test_all(retry_nodes)
                for rr in retry_results:
                    fp = rr.node.fingerprint()
                    prev = best_by_fp.get(fp)
                    if prev is None or (not prev.success and rr.success):
                        best_by_fp[fp] = rr
            results = list(best_by_fp.values())

        # Load node stability for scoring boost
        stability_data = load_node_stability(args.output_dir)
        stable_fingerprints = set(get_stable_nodes(stability_data, min_consecutive=2)) if stability_data else set()

        scored_valid = []
        for r in results:
            if not r.success:
                continue

            fp = r.node.fingerprint()
            src_name = node_source_map.get(fp, "unknown")
            score_input = ScoreInput(
                latency_ms=r.latency_ms,
                jitter_ms=r.jitter_ms,
                tcp_latency_ms=tcp_latency.get(fp, 0),
                protocol=r.node.type,
                source=src_name,
                protocol_rates=protocol_rates,
                source_rates=source_rates,
                speed_kbps=getattr(r, "speed_kbps", 0),
                fingerprint_resistance=getattr(r, "fingerprint_resistance_score", 0.0),
            )
            score = calculate_score(score_input, scoring_config)
            breakdown = calculate_score_breakdown(score_input, scoring_config)

            # Stability bonus for repeatedly successful nodes.
            stability_bonus = 0.0
            if fp in stable_fingerprints:
                stability_count = stability_data.get(fp, {}).get("consecutive_pass", 0) if stability_data else 0
                stability_bonus = min(5.0, float(stability_count))
                score = round(score + stability_bonus, 2)
            if max_latency_ms > 0 and r.latency_ms > max_latency_ms:
                continue
            if min_speed_kbps > 0 and getattr(r, "speed_kbps", 0.0) < min_speed_kbps:
                continue
            scored_valid.append((r.node, r.latency_ms, r.jitter_ms, score, src_name, breakdown, r, stability_bonus))

        scored_valid.sort(key=lambda x: (-x[3], x[1], x[2], x[0].fingerprint()))
        valid = [(n, lat, jit) for n, lat, jit, _, _, _, _, _ in scored_valid]
        real_test_passed = bool(valid)
        try:
            import json as _json
            _details = []
            for n, lat, jit, score, src, bd, r, sbonus in scored_valid:
                _details.append({
                    "fingerprint": n.fingerprint(),
                    "protocol": n.type,
                    "source": src,
                    "latency_ms": lat,
                    "jitter_ms": jit,
                    "tcp_latency_ms": tcp_latency.get(n.fingerprint(), 0),
                    "speed_kbps": getattr(r, "speed_kbps", 0),
                    "score": score,
                    "stability_bonus": sbonus,
                    "breakdown": bd,
                })
            with open(f"{args.output_dir}/score_details.json", "w") as _f:
                _json.dump({"updated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                            "count": len(_details), "nodes": _details}, _f)
        except Exception as _e:
            print(f"      score_details write failed ({type(_e).__name__}), skipped")
        print(f"      Real-test valid: {len(valid)}/{len(nodes)}")
        print(f"[funnel] stage=real_test in={len(nodes)} out={len(valid)}")
        if valid:
            print(f"      Latency range: best={valid[0][1]:.1f}ms worst={valid[-1][1]:.1f}ms")

        if args.global_output and results:
            cn_block_nodes = [r.node for r in results if (not r.success and r.error.startswith("cn-block:"))]
            if cn_block_nodes:
                print(f"      Global retry pass (skip cn-block): {len(cn_block_nodes)} nodes...")
                global_tester = SingBoxTester(
                    sb_path=args.singbox,
                    concurrency=args.test_concurrency,
                    startup_wait=args.startup_wait,
                    request_timeout=args.test_timeout,
                    min_latency_ms=args.min_latency,
                    skip_target_kinds={"cn-block"},
                    probe_count=max(1, probe_count),
                    retries=max(0, test_retries),
                    enable_speed_test=speed_test_enabled,
                    speed_test_bytes=speed_test_bytes,
                )
                cn_block_retry_results = await global_tester.test_all(cn_block_nodes)
                cn_block_retry_valid = sorted(
                    [(r.node, r.latency_ms, r.jitter_ms) for r in cn_block_retry_results if r.success],
                    key=lambda x: (x[1], x[0].fingerprint()),
                )
                print(f"      Global extra valid: {len(cn_block_retry_valid)}/{len(cn_block_nodes)}")
        stage_durations["real_test"] = round(time.time() - stage_start, 1)
        stage_start = time.time()
    else:
        print("[5/7] Skipped real test")
        stage_durations["real_test"] = 0.0
        stage_start = time.time()

    if not args.real_test:
        cn_block_retry_results = []
        cn_block_retry_valid = []

    # TCP 延迟只保留为"是否可达"信息, 不参与延迟排序. 真测 0 通过时降级.
    degraded_mode = False
    if real_test_passed:
        pass
    elif not args.real_test:
        valid = sorted(
            [(n, tcp_latency.get(n.fingerprint(), 0), 0.0) for n in nodes],
            key=lambda x: (x[1], x[0].fingerprint()),
        )
        print(f"[5/7] TCP-only mode: {len(valid)} nodes")
    else:
        err_counter: Dict[str, int] = {}
        for r in results:
            if not r.success and r.error:
                key = r.error[:60]
                err_counter[key] = err_counter.get(key, 0) + 1
        top_errs = sorted(err_counter.items(), key=lambda x: -x[1])[:5]
        print("      Warning: real test had 0 valid nodes; fallback to TCP mode")
        for err, cnt in top_errs:
            print(f"        [{cnt}×] {err}")
        global _REAL_TEST_FAIL_REASONS
        _REAL_TEST_FAIL_REASONS = dict(err_counter)
        valid = sorted(
            [(n, tcp_latency.get(n.fingerprint(), 0), 0.0) for n in nodes],
            key=lambda x: (x[1], x[0].fingerprint()),
        )
        degraded_mode = True
        print(f"      Fallback output uses {len(valid)} TCP-reachable nodes")

    # 真实测试失败原因统计 — 让 stats.json 自带诊断
    from core.tester import build_error_detail
    real_test_errors: Dict[str, int] = {}
    real_test_error_details_counter: Dict[str, int] = {}
    real_test_error_structured_counter: Dict[tuple, Dict[str, object]] = {}
    for r in results if args.real_test else []:
        if r.success:
            continue
        error = r.error or "unknown"
        detail = r.error_detail or build_error_detail(error)
        target = str(detail.get("target", error.split(":", 1)[0]))
        reason = str(detail.get("reason", "unknown"))
        err_key = target
        real_test_errors[err_key] = real_test_errors.get(err_key, 0) + 1
        detail_key = error[:120]
        real_test_error_details_counter[detail_key] = real_test_error_details_counter.get(detail_key, 0) + 1
        struct_key = (target, reason, str(detail.get("status", detail.get("value", ""))))
        row = real_test_error_structured_counter.setdefault(struct_key, {
            "target": target,
            "reason": reason,
            "status": detail.get("status"),
            "value": detail.get("value"),
            "count": 0,
        })
        row["count"] = int(row["count"]) + 1
    real_test_error_details = [
        {"error": error, "count": count}
        for error, count in sorted(real_test_error_details_counter.items(), key=lambda x: -x[1])[:10]
    ]
    real_test_error_structured = sorted(
        real_test_error_structured_counter.values(),
        key=lambda row: -int(row.get("count", 0)),
    )[:20]

    # 5.5) Optional China reachability check
    china_reachable_count = 0
    china_unreachable_count = 0
    gen_start = time.time()
    if getattr(args, 'china_check', False) and valid:
        print(f"[5.5/7] China reachability check (GlobalPing): {len(valid)} nodes")
        try:
            from core.globalping import check_china_reachability
            china_map = await check_china_reachability(valid)
            china_valid = [(n, lat, jit) for n, lat, jit in valid if china_map.get(n.fingerprint(), False)]
            china_reachable_count = len(china_valid)
            china_unreachable_count = len(valid) - china_reachable_count
            print(f"      China reachable: {china_reachable_count}, unreachable: {china_unreachable_count}")
            if china_valid:
                valid = china_valid
            else:
                print("      Warning: all nodes unreachable from China probes, keeping global results")
        except Exception as e:
            print(f"      China check failed ({e}), keeping global results")
    stage_durations["china_check"] = round(time.time() - gen_start, 1)
    gen_start = time.time()
    stage_start = time.time()
    top = valid[:args.top_n]
    final_nodes = build_output_nodes(valid, flag_map, args.top_n)
    global_valid = sorted(valid + cn_block_retry_valid, key=lambda x: x[1])
    global_nodes = build_output_nodes(global_valid, flag_map, args.top_n)

    # 6) Generate outputs
    print("[6/7] Generating subscription files...")
    from core.generator import write_outputs, write_chunked_outputs, write_protocol_outputs

    output_guard: Dict[str, Dict[str, object]] = {}

    previous_verified = count_existing_urls(args.output_dir, "verified")
    proposed_verified = len([n for n in final_nodes if n])
    if should_preserve_previous_output(proposed_verified, previous_verified, args.min_retain_ratio):
        n_top = previous_verified
        output_guard["verified"] = {
            "preserved": True,
            "previous_count": previous_verified,
            "proposed_count": proposed_verified,
            "min_retain_ratio": args.min_retain_ratio,
        }
        print(f"      verified.* kept previous output: {previous_verified} (current={proposed_verified} below threshold)")
    else:
        _w0 = time.time()
        n_top = write_outputs(final_nodes, args.output_dir, prefix="verified", repo_path=args.repo, branch=args.branch)
        # P0: 分块输出 (verified)
        write_chunked_outputs(final_nodes, args.output_dir, prefix="verified",
                             repo_path=args.repo, branch=args.branch, chunk_size=100)
        # P1: 协议分文件输出 (verified)
        stage_durations["write_verified"] = round(time.time() - _w0, 1)
        write_protocol_outputs(final_nodes, args.output_dir, prefix="verified",
                              repo_path=args.repo, branch=args.branch)
        output_guard["verified"] = {"preserved": False, "previous_count": previous_verified, "proposed_count": n_top}

    if args.global_output:
        previous_global = count_existing_urls(args.output_dir, "global")
        proposed_global = len([n for n in global_nodes if n])
        if should_preserve_previous_output(proposed_global, previous_global, args.min_retain_ratio):
            n_global = previous_global
            output_guard["global"] = {
                "preserved": True,
                "previous_count": previous_global,
                "proposed_count": proposed_global,
                "min_retain_ratio": args.min_retain_ratio,
            }
            print(f"      global.* kept previous output: {previous_global} (current={proposed_global} below threshold)")
        else:
            _w0 = time.time()
            n_global = write_outputs(global_nodes, args.output_dir, prefix="global", repo_path=args.repo, branch=args.branch)
            # P0: 分块输出 (global)
            write_chunked_outputs(global_nodes, args.output_dir, prefix="global",
                                 repo_path=args.repo, branch=args.branch, chunk_size=100)
            # P1: 协议分文件输出 (global)
            write_protocol_outputs(global_nodes, args.output_dir, prefix="global",
                                  repo_path=args.repo, branch=args.branch)
            output_guard["global"] = {"preserved": False, "previous_count": previous_global, "proposed_count": n_global}
    else:
        n_global = 0
    # all.* keeps the full deduplicated pool.
    all_valid = dedup_pool
    _w0 = time.time()
    n_all = write_outputs(
        all_valid,
        args.output_dir,
        prefix="all",
        repo_path=args.repo,
        flag_map=flag_map,
        branch=args.branch,
        mode=args.all_output_mode,
    )
    stage_durations["generate"] = round(time.time() - stage_start, 1)

    # 6.5) Deterministic top-link output without metadata.
    top_urls = []
    seen_urls = set()
    for node in final_nodes[: args.top_n]:
        url = node_to_url(node)
        if not url or url in seen_urls:
            continue
        seen_urls.add(url)
        top_urls.append(url)
    top_links_path = Path(args.output_dir) / top_links_path_value
    top_links_path.parent.mkdir(parents=True, exist_ok=True)
    top_links_path.write_text(("\n".join(top_urls) + "\n") if top_urls else "", encoding="utf-8")

    # 7) Clean IP detection from valid ranked nodes.
    clean_candidates = await extract_candidate_ips(
        [row[0] for row in valid],
        resolve_timeout=clean_ip_resolve_timeout,
        resolve_concurrency=clean_ip_resolve_concurrency,
    )
    clean_found, clean_probe_stats = await probe_clean_ips(
        clean_candidates,
        target=clean_ip_target,
        timeout=clean_ip_timeout,
        concurrency=clean_ip_concurrency,
        port=clean_ip_port,
        max_latency_ms=clean_ip_max_latency_ms,
    )
    clean_ips = [ip for ip, _ in clean_found]
    clean_path = Path(args.output_dir) / clean_ip_output_value
    clean_path.parent.mkdir(parents=True, exist_ok=True)
    clean_path.write_text(("\n".join(clean_ips) + "\n") if clean_ips else "", encoding="utf-8")

    elapsed = time.time() - t0
    print("\n┌─────────────────────────────────────────────┐")
    print(f"│  ✅ Finished [{elapsed:.1f}s]")
    print(f"│  • Raw nodes:   {total_raw:>6}")
    print(f"│  • Unique:      {len(set(nd.fingerprint() for nd in all_nodes)):>6}")
    print(f"│  • TCP pass:    {nodes_before_probe:>6}")
    print(f"│  • Probe pass:  {nodes_after_probe:>6}")
    print(f"│  • Real valid:  {len(valid):>6}")
    print(f"│  • China pass:  {china_reachable_count:>6}")
    print(f"│  • Top links:   {len(top_urls):>6}")
    print(f"│  • Clean IPs:   {len(clean_ips):>6}")
    print(f"│  • Verified:    {n_top:>6}")
    if args.global_output:
        print(f"│  • Global:      {n_global:>6}")
    print("└─────────────────────────────────────────────┘")

    # 统计 JSON
    proto_pass: Dict[str, Dict[str, int]] = {}
    for r in results if args.real_test else []:
        t = r.node.type
        if t not in proto_pass:
            proto_pass[t] = {"pass": 0, "fail": 0}
        proto_pass[t]["pass" if r.success else "fail"] += 1

    # per-source 通过率统计
    src_pass: Dict[str, Dict[str, int]] = {}
    for r in results if args.real_test else []:
        src_name = node_source_map.get(r.node.fingerprint(), "unknown")
        if src_name not in src_pass:
            src_pass[src_name] = {"pass": 0, "fail": 0}
        src_pass[src_name]["pass" if r.success else "fail"] += 1
    source_scores = build_source_scores(source_nodes, src_pass, source_dead_counts)

    stats = {
        "version": __version__,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "duration_sec": round(elapsed, 1),
        "degraded_mode": degraded_mode,
        "stage_durations": stage_durations,
        "sources_total": len(sources),
        "sources_unique": len(sources),
        "sources_healthy": healthy,
        "sources_failed": max(0, len(sources) - healthy),
        "nodes_raw": total_raw,
        "nodes_collected": len(all_nodes),
        "nodes_dedup": len(set(nd.fingerprint() for nd in all_nodes)),
        "nodes_tcp_ok": nodes_before_probe,
        "nodes_tcp_reachable": nodes_tcp_reachable if args.tcp_check else len(nodes),
        "nodes_probe_ok": nodes_after_probe,
        "nodes_real_ok": len(valid),
        "probe_error_details": probe_error_top if (args.lightweight_probe and args.real_test) else [],
        "nodes_verified_output": n_top,
        "nodes_global_output": n_global,
        "nodes_top_output": len(top_urls),
        "top_links_output_path": top_links_path_value,
        "output_guard": output_guard,
        "nodes_global_extra_from_cn_block": len(cn_block_retry_valid),
        "global_skip_target_kinds": ["cn-block"] if args.global_output else [],
        "nodes_all_output": n_all,
        "elapsed_test_time_sec": stage_durations.get("real_test", 0.0),
        "ranking": {
            "weights": scoring_config.weights,
            "max_latency_ms": max_latency_ms,
            "min_speed_kbps": min_speed_kbps,
        },
        "clean_ip": {
            "target": clean_ip_target,
            "count": len(clean_ips),
            "output_path": clean_ip_output_value,
            "tested_candidates": clean_probe_stats.get("tested", 0),
            "all_candidates": clean_probe_stats.get("candidates", 0),
            "success_count": clean_probe_stats.get("success", 0),
        },
        "all_output_mode": args.all_output_mode,
        "protocol_dist": proto_count,
        "filter_rule_hits": filter_rule_hits,
        "protocol_pass_rate": proto_pass,
        "source_pass_rate": src_pass,
        "source_nodes": source_nodes,
        "source_scores": source_scores,
        "tcp_errors": tcp_errors,
        "real_test_errors": real_test_errors,
        "real_test_error_details": real_test_error_details,
        "real_test_error_structured": real_test_error_structured,
        "top_latencies_ms": [round(lat, 1) for _, lat, _ in top if lat > 0][:20],
        "top_jitters_ms": [round(jit, 1) for _, _, jit in top if jit > 0][:20],
        "scoring": {
            "weights": scoring_config.weights,
            "excellent_latency_ms": scoring_config.excellent_latency_ms,
            "bad_latency_ms": scoring_config.bad_latency_ms,
            "bad_jitter_ms": scoring_config.bad_jitter_ms,
            "excellent_tcp_latency_ms": scoring_config.excellent_tcp_latency_ms,
            "bad_tcp_latency_ms": scoring_config.bad_tcp_latency_ms,
            "missing_tcp_score": scoring_config.missing_tcp_score,
            "missing_history_score": scoring_config.missing_history_score,
        },
        "top_scores": [
            {
                "tag": n.tag,
                "server": n.server,
                "type": n.type,
                "source": source,
                "latency_ms": round(lat, 1),
                "jitter_ms": round(jit, 1),
                "score": score,
                "score_breakdown": breakdown,
                "stability_bonus": stability_bonus,
                "speed_kbps": getattr(r, "speed_kbps", 0) if r else 0,
                "fingerprint_resistance": getattr(r, "fingerprint_resistance", "") if r else "",
                "netflix": getattr(r, "netflix_ok", False) if r else False,
                "chatgpt": getattr(r, "chatgpt_ok", False) if r else False,
                "stability_bonus": stability_bonus,
            }
            for n, lat, jit, score, source, breakdown, r, stability_bonus in scored_valid[:20]
        ],
    }
    os.makedirs(args.output_dir, exist_ok=True)
    with open(f"{args.output_dir}/stats.json", "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    update_trend_history(args.output_dir, stats)

    # Node stability tracking
    if args.real_test and results:
        passed_fps = [r.node.fingerprint() for r in results if r.success]
        failed_fps = [r.node.fingerprint() for r in results if not r.success]
        stability = update_node_stability(args.output_dir, passed_fps, failed_fps,
                                          stats.get("timestamp", ""))
        stats["node_stability_count"] = stability.get("total_tracked", 0) if isinstance(stability, dict) else 0
        # Re-write stats with stability count
        with open(f"{args.output_dir}/stats.json", "w", encoding="utf-8") as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)
    report_path = write_health_report(args.output_dir, stats)
    print(f"      Health report: {report_path}")
    if update_readme_stats("README.md", stats):
        print("      README status block updated")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--sources", default="config/sources.yaml")
    p.add_argument("--runtime-config", default="config/runtime.yaml",
                   help="Runtime pipeline options YAML file")
    p.add_argument("--output-dir", default="output")
    p.add_argument("--singbox", default="./sing-box")
    p.add_argument("--top-n", type=int, default=200, help="Maximum number of ranked output nodes")
    p.add_argument("--top-links-path", default="200_links.txt",
                   help="Relative path under output-dir for deterministic top links")
    p.add_argument("--clean-ip-output", default="clean_ips_20.txt",
                   help="Relative path under output-dir for clean IP output")
    p.add_argument("--clean-ip-target", type=int, default=20, help="Stop after collecting this many clean IPs")
    p.add_argument("--clean-ip-concurrency", type=int, default=60)
    p.add_argument("--clean-ip-timeout", type=float, default=2.0)
    p.add_argument("--clean-ip-port", type=int, default=443)
    p.add_argument("--clean-ip-max-latency-ms", type=float, default=800.0)
    p.add_argument("--clean-ip-resolve-timeout", type=float, default=2.0)
    p.add_argument("--clean-ip-resolve-concurrency", type=int, default=60)

    p.add_argument("--fetch-concurrency", type=int, default=30)
    p.add_argument("--fetch-timeout", type=int, default=15)
    p.add_argument("--fetch-retries", type=int, default=2)
    p.add_argument("--fetch-rate-limit-per-sec", type=float, default=0.0,
                   help="Optional source fetch start rate limit (0 disables)")
    p.add_argument("--fetch-overall-timeout", type=int, default=120,
                   help="Overall timeout in seconds for source fetch stage")

    p.add_argument("--tcp-check", action=argparse.BooleanOptionalAction, default=True)
    p.add_argument("--tcp-concurrency", type=int, default=500)
    p.add_argument("--tcp-timeout", type=float, default=2.0)
    p.add_argument("--china-check", action=argparse.BooleanOptionalAction, default=True,
                   help="Use GlobalPing China probes to validate reachability from mainland China")

    p.add_argument("--real-test", action=argparse.BooleanOptionalAction, default=True)
    p.add_argument("--test-concurrency", type=int, default=75)
    p.add_argument("--test-retries", type=int, default=0)
    p.add_argument("--lightweight-probe", action=argparse.BooleanOptionalAction, default=True)
    p.add_argument("--probe-concurrency", type=int, default=100)
    p.add_argument("--probe-timeout", type=float, default=4.0)
    p.add_argument("--probe-count", type=int, default=3,
                   help="Per-node probe sample count for 204 target")
    p.add_argument("--probe-startup-wait", type=float, default=0.4)
    p.add_argument("--test-timeout", type=float, default=6.0)
    p.add_argument("--startup-wait", type=float, default=0.6)
    p.add_argument("--test-limit", type=int, default=3000, help="Max nodes to enter real test (0=unlimited)")
    p.add_argument("--quality-filter", action=argparse.BooleanOptionalAction, default=True,
                   help="Enable quality pre-filtering")
    p.add_argument("--filter-rules", default="config/filter_rules.yaml",
                   help="Quality filter rules file")
    p.add_argument("--scoring-rules", default="config/scoring.yaml",
                   help="Node scoring rules file")
    p.add_argument("--max-per-server", type=int, default=0,
                   help="Keep at most N nodes per server IP (0 disables)")
    p.add_argument("--min-latency", type=float, default=30.0,
                   help="Reject suspiciously low latency values in real test (0 disables)")
    p.add_argument("--max-latency-ms", type=float, default=0.0,
                   help="Optional max allowed real-test latency (0 disables)")
    p.add_argument("--min-speed-kbps", type=float, default=0.0,
                   help="Optional minimum required download speed in KB/s (0 disables)")
    p.add_argument("--speed-test-enabled", action=argparse.BooleanOptionalAction, default=True)
    p.add_argument("--speed-test-bytes", type=int, default=102400)
    p.add_argument("--global-output", action=argparse.BooleanOptionalAction, default=True,
                   help="Generate global.* outputs in addition to verified.*")
    p.add_argument("--min-retain-ratio", type=float, default=0.7,
                   help="Preserve previous verified/global outputs if new count shrinks below ratio")
    p.add_argument("--all-output-mode", choices=("full", "light"), default=os.environ.get("AUTONODES_ALL_OUTPUT_MODE", "full"),
                   help="all.* output mode")
    p.add_argument("--repo", default="LeilaoMi/AutoMergePublicNodes-Optimized",
                   help="owner/repo used for generated converter links")
    p.add_argument("--branch", default=os.environ.get("AUTONODES_BRANCH", "main"),
                   help="Branch name used for converter links")

    args = p.parse_args()
    apply_runtime_overrides(args, load_runtime_config(args.runtime_config))

    # 参数验证
    if args.top_n < 0:
        p.error("--top-n must be >= 0")
    if args.fetch_concurrency <= 0:
        p.error("--fetch-concurrency must be > 0")
    if args.fetch_overall_timeout <= 0:
        p.error("--fetch-overall-timeout must be > 0")
    if args.tcp_concurrency <= 0:
        p.error("--tcp-concurrency must be > 0")
    if args.test_concurrency <= 0:
        p.error("--test-concurrency must be > 0")
    if args.test_limit < 0:
        p.error("--test-limit must be >= 0")
    if args.min_latency < 0:
        p.error("--min-latency must be >= 0")
    if args.min_retain_ratio < 0:
        p.error("--min-retain-ratio must be >= 0")
    if args.fetch_retries < 0:
        p.error("--fetch-retries must be >= 0")
    if args.fetch_rate_limit_per_sec < 0:
        p.error("--fetch-rate-limit-per-sec must be >= 0")
    if args.probe_count <= 0:
        p.error("--probe-count must be > 0")
    if args.test_retries < 0:
        p.error("--test-retries must be >= 0")
    if args.max_latency_ms < 0:
        p.error("--max-latency-ms must be >= 0")
    if args.min_speed_kbps < 0:
        p.error("--min-speed-kbps must be >= 0")
    if args.speed_test_bytes <= 0:
        p.error("--speed-test-bytes must be > 0")
    if args.clean_ip_target < 0:
        p.error("--clean-ip-target must be >= 0")
    if args.clean_ip_concurrency <= 0:
        p.error("--clean-ip-concurrency must be > 0")
    if args.clean_ip_timeout <= 0:
        p.error("--clean-ip-timeout must be > 0")
    if args.clean_ip_port <= 0 or args.clean_ip_port > 65535:
        p.error("--clean-ip-port must be in 1..65535")
    if args.clean_ip_max_latency_ms < 0:
        p.error("--clean-ip-max-latency-ms must be >= 0")

    # Environment variable overrides
    if os.environ.get("AUTONODES_TOP_N"):
        args.top_n = int(os.environ["AUTONODES_TOP_N"])
    if os.environ.get("AUTONODES_TEST_LIMIT"):
        args.test_limit = int(os.environ["AUTONODES_TEST_LIMIT"])
    asyncio.run(run(args))


if __name__ == "__main__":
    main()
