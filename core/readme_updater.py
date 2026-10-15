"""README status block updater.

Keeps the repository homepage synchronized with the latest pipeline stats.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

START_MARKER = "<!-- AUTONODES_STATS_START -->"
END_MARKER = "<!-- AUTONODES_STATS_END -->"


def _table(headers: List[str], rows: List[List[object]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(x) for x in row) + " |")
    return "\n".join(lines)


def _fmt_rate(numerator: object, denominator: object) -> str:
    try:
        n = int(numerator or 0)
        d = int(denominator or 0)
    except (TypeError, ValueError):
        return "-"
    if d <= 0:
        return "-"
    return f"{n / d * 100:.1f}%"


def _top_sources(stats: Dict[str, Any], limit: int = 5) -> List[List[object]]:
    source_scores = stats.get("source_scores") or {}
    if not isinstance(source_scores, dict):
        return []

    rows: List[List[object]] = []
    for name, data in sorted(
        source_scores.items(),
        key=lambda x: -float(x[1].get("score", 0)) if isinstance(x[1], dict) else 0,
    )[:limit]:
        if not isinstance(data, dict):
            continue
        rows.append([
            name,
            data.get("score", "-"),
            data.get("tested", 0),
            data.get("recommendation", "-"),
        ])
    return rows


def build_readme_stats_block(stats: Dict[str, Any]) -> str:
    overview_rows = [
        ["Updated", stats.get("timestamp", "-")],
        ["Version", stats.get("version", "-")],
        ["Sources", f"{stats.get('sources_healthy', 0)}/{stats.get('sources_total', 0)}"],
        ["Raw nodes", stats.get("nodes_raw", 0)],
        ["Unique nodes", stats.get("nodes_dedup", 0)],
        ["TCP pass", stats.get("nodes_tcp_ok", 0)],
        ["Real-test pass", stats.get("nodes_real_ok", 0)],
        ["Real-test pass rate", _fmt_rate(stats.get("nodes_real_ok"), stats.get("nodes_tcp_ok"))],
        ["Top links output", stats.get("nodes_top_output", 0)],
        ["Clean IPs", (stats.get("clean_ip") or {}).get("count", 0)],
        ["Verified output", stats.get("nodes_verified_output", 0)],
        ["Global output", stats.get("nodes_global_output", 0)],
        ["All output", stats.get("nodes_all_output", 0)],
    ]

    top_score_rows = [
        [
            item.get("score", "-"),
            item.get("type", "-"),
            item.get("latency_ms", "-"),
            item.get("source", "-"),
        ]
        for item in (stats.get("top_scores") or [])[:5]
        if isinstance(item, dict)
    ]

    source_rows = _top_sources(stats, limit=5)

    guard = stats.get("output_guard") or {}
    preserved = []
    if isinstance(guard, dict):
        preserved = [name for name, data in guard.items() if isinstance(data, dict) and data.get("preserved")]
    guard_text = "none" if not preserved else ", ".join(preserved)

    lines = [
        START_MARKER,
        "## Current Run Status",
        "",
        _table(["指标", "数值"], overview_rows),
        "",
        f"> Output guard: {guard_text}. Full report: `output/health_report.md`, `output/stats.json`.",
        "",
        "### Top Node Scores",
        "",
        _table(["Score", "Protocol", "Latency(ms)", "Source"], top_score_rows) if top_score_rows else "_No scoring data_",
        "",
        "### Top Source Quality",
        "",
        _table(["Source", "Score", "Tested", "Recommendation"], source_rows) if source_rows else "_No source score data_",
        "",
        END_MARKER,
    ]
    return "\n".join(lines)


def update_readme_stats(readme_path: str, stats: Dict[str, Any]) -> bool:
    path = Path(readme_path)
    if not path.exists():
        return False

    original = path.read_text(encoding="utf-8")
    block = build_readme_stats_block(stats)

    if START_MARKER in original and END_MARKER in original:
        before = original.split(START_MARKER, 1)[0].rstrip()
        after = original.split(END_MARKER, 1)[1].lstrip()
        updated = before + "\n\n" + block + "\n\n" + after
    else:
        updated = original.rstrip() + "\n\n" + block + "\n"

    if updated == original:
        return False

    path.write_text(updated, encoding="utf-8")
    return True
