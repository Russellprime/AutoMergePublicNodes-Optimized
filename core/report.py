"""Markdown health report generation."""
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List


def _table(headers: List[str], rows: List[List[object]]) -> str:
    if not rows:
        return "_No data_"

    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(x) for x in row) + " |")
    return "\n".join(lines)


def write_health_report(output_dir: str, stats: Dict[str, Any]) -> str:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    report_path = output_path / "health_report.md"

    overview_rows = [
        ["Version", stats.get("version", "-")],
        ["Updated", stats.get("timestamp", "-")],
        ["Elapsed", f"{stats.get('duration_sec', 0)}s"],
        ["Sources (total)", stats.get("sources_total", 0)],
        ["Sources (healthy)", stats.get("sources_healthy", 0)],
        ["Nodes (raw)", stats.get("nodes_raw", 0)],
        ["Nodes (unique)", stats.get("nodes_dedup", 0)],
        ["Nodes (TCP pass)", stats.get("nodes_tcp_ok", 0)],
        ["Nodes (probe pass)", stats.get("nodes_probe_ok", 0)],
        ["Nodes (real-test pass)", stats.get("nodes_real_ok", 0)],
        ["Top links output", stats.get("nodes_top_output", 0)],
        ["Clean IPs", (stats.get("clean_ip") or {}).get("count", 0)],
        ["Verified output", stats.get("nodes_verified_output", 0)],
        ["Global output", stats.get("nodes_global_output", 0)],
        ["All output", stats.get("nodes_all_output", 0)],
    ]

    protocol_rows = [
        [name, count]
        for name, count in sorted(
            (stats.get("protocol_dist") or {}).items(),
            key=lambda x: -int(x[1]),
        )
    ]

    source_score_rows = []
    source_scores = stats.get("source_scores") or {}
    if isinstance(source_scores, dict):
        for name, data in sorted(
            source_scores.items(),
            key=lambda x: -float(x[1].get("score", 0)) if isinstance(x[1], dict) else 0,
        )[:15]:
            if not isinstance(data, dict):
                continue
            source_score_rows.append([
                name,
                data.get("score", "-"),
                data.get("pass_rate", "-"),
                data.get("tested", 0),
                data.get("parsed_nodes", 0),
                data.get("recommendation", "-"),
            ])

    error_rows = [
        [
            item.get("target", "-"),
            item.get("reason", "-"),
            item.get("status") or item.get("value") or "-",
            item.get("count", 0),
        ]
        for item in (stats.get("real_test_error_structured") or [])[:15]
        if isinstance(item, dict)
    ]

    scoring = stats.get("scoring") or {}
    weights = scoring.get("weights") if isinstance(scoring, dict) else {}
    scoring_rows = []
    if isinstance(weights, dict):
        scoring_rows = [[key, value] for key, value in weights.items()]

    score_rows = []
    for item in (stats.get("top_scores") or [])[:20]:
        if not isinstance(item, dict):
            continue
        breakdown = item.get("score_breakdown") or {}

        def _points(name: str) -> object:
            value = breakdown.get(name) if isinstance(breakdown, dict) else None
            return value.get("points", "-") if isinstance(value, dict) else "-"

        score_rows.append([
            item.get("score", "-"),
            item.get("type", "-"),
            item.get("latency_ms", "-"),
            item.get("jitter_ms", "-"),
            _points("latency"),
            _points("jitter"),
            _points("tcp"),
            _points("protocol_history"),
            _points("source_history"),
            item.get("source", "-"),
            item.get("server", "-"),
        ])

    guard_rows = []
    output_guard = stats.get("output_guard") or {}
    if isinstance(output_guard, dict):
        for name, data in output_guard.items():
            if isinstance(data, dict):
                guard_rows.append([
                    name,
                    data.get("preserved", False),
                    data.get("previous_count", 0),
                    data.get("proposed_count", 0),
                    data.get("min_retain_ratio", "-"),
                ])

    content = f"""# AutoNodes Health Report

## Overview

{_table(["Metric", "Value"], overview_rows)}

## Stage Duration

{_table(["Stage", "Seconds"], [[k, v] for k, v in (stats.get("stage_durations") or {}).items()])}

## Protocol Distribution

{_table(["Protocol", "Count"], protocol_rows)}

## Ranking Weights

{_table(["Factor", "Weight"], scoring_rows)}

## Top Node Scores

{_table(["Score", "Protocol", "Latency(ms)", "Jitter(ms)", "Latency pts", "Jitter pts", "TCP pts", "Protocol-history pts", "Source-history pts", "Source", "Server"], score_rows)}

## Source Quality

{_table(["Source", "Score", "Pass Rate", "Tested", "Parsed Nodes", "Recommendation"], source_score_rows)}

## Real Test Failures

{_table(["Target", "Reason", "Status/Value", "Count"], error_rows)}

## Output Guard

{_table(["Prefix", "Preserved previous", "Previous count", "Current proposed count", "Retain ratio"], guard_rows)}

---

Generated by `core.report.write_health_report()`.
"""

    report_path.write_text(content, encoding="utf-8")
    return str(report_path)
