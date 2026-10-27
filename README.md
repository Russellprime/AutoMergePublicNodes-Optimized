# AutoMergePublicNodes-Optimized

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue)]()

Automatically aggregates public proxy sources, parses multi-protocol nodes, runs bounded connectivity tests, ranks usable nodes, and exports client-ready outputs.

> For learning/research use only. Public nodes are unstable and may carry compliance or security risk.

---

## Key Features

- Multi-source fetch from `config/sources.yaml` with per-source isolation
- Source and node deduplication
- Bounded network behavior (timeouts, concurrency, retries, optional rate limit)
- Lightweight probe + real sing-box proxy tests
- Weighted ranking (latency, jitter, TCP, speed, fingerprint resistance, historical protocol/source pass rate)
- Deterministic ranked top-link output: `output/200_links.txt`
- Independent clean-IP detection with early stop at target (default 20): `output/clean_ips_20.txt`
- Standard outputs preserved: Clash (`*.yaml`), sing-box (`*.json`), V2Ray/base64 (`*.txt`), URL lists (`*.urls`)

---

## Configuration

### Public sources

- File: `config/sources.yaml`
- Supports source metadata such as `name`, `kind`, `enabled`, `ignore_protocols`, `max_nodes`
- Duplicate/malformed entries are ignored safely at runtime

### Runtime pipeline defaults

- File: `config/runtime.yaml`
- Main controls:
  - `top_n` (default `200`)
  - `clean_ip_target` (default `20`)
  - fetch timeout/concurrency/retries/rate limit
  - probe/test timeout/concurrency/retries/probe count
  - speed-test toggle and payload bytes
  - ranking thresholds (`max_latency_ms`, `min_speed_kbps`)
  - clean-IP timeout/concurrency/latency threshold/output path

### Scoring

- File: `config/scoring.yaml`
- Weights are transparent and configurable.

---

## Local Run

```bash
git clone https://github.com/Russellprime/AutoMergePublicNodes-Optimized.git
cd AutoMergePublicNodes-Optimized
pip install -r requirements.txt

# run with defaults (including top 200 and clean-ip target 20)
python main.py
```

Useful checks:

```bash
python -m compileall -q main.py core tools tests
python tools/import_contract.py
python tools/validate_config.py --sources config/sources.yaml --filter-rules config/filter_rules.yaml --runtime-config config/runtime.yaml --scoring-rules 'config/scoring*.yaml'
python -m unittest -v tests.test_regressions
```

---

## Generated Files

- Ranked strict outputs:
  - `output/verified.yaml`
  - `output/verified.txt`
  - `output/verified.json`
  - `output/verified.urls`
- Extended/global outputs:
  - `output/global.yaml`
  - `output/global.txt`
  - `output/global.json`
  - `output/global.urls`
- Full deduplicated pool:
  - `output/all.yaml`
  - `output/all.txt`
  - `output/all.json`
  - `output/all.urls`
- New deterministic ranked links:
  - `output/200_links.txt`
- New clean IP output (early-stop target):
  - `output/clean_ips_20.txt`
- Reports:
  - `output/stats.json`
  - `output/health_report.md`
  - `output/health_report.json`

`output/200_links.txt` is duplicate-free and deterministic, one usable link per line, no metadata lines.

Clean-IP probing stops launching new probes as soon as the target count is reached.

---

## GitHub Actions / Cron

Workflow: `.github/workflows/update.yml`

- Scheduled run every 6 hours
- Manual run via workflow_dispatch
- Validates config, runs tests, executes pipeline, builds reports, uploads artifacts

---

## Project Structure

```text
main.py                 # pipeline + CLI
core/                   # fetch/parse/test/rank/generate/report helpers
config/                 # sources, runtime defaults, scoring/filter rules
tools/                  # validation, reports, maintenance utilities
tests/                  # regression tests
output/                 # generated outputs and reports
```

## License

MIT

## Acknowledgements

- [sing-box](https://github.com/SagerNet/sing-box)
- Public source maintainers and contributors

<!-- AUTONODES_STATS_START -->
## Current Run Status

| 指标 | 数值 |
| --- | --- |
| Updated | 2026-10-27 06:08:23 |
| Version | 2.5.0 |
| Sources | 88/107 |
| Raw nodes | 96324 |
| Unique nodes | 26586 |
| TCP pass | 3000 |
| Real-test pass | 104 |
| Real-test pass rate | 3.5% |
| Top links output | 104 |
| Clean IPs | 20 |
| Verified output | 104 |
| Global output | 106 |
| All output | 26586 |

> Output guard: none. Full report: `output/health_report.md`, `output/stats.json`.

### Top Node Scores

| Score | Protocol | Latency(ms) | Source |
| --- | --- | --- | --- |
| 73.99 | vless | 268.0 | Au1rxx-base64 |
| 72.39 | vless | 342.4 | Au1rxx-base64 |
| 72.36 | vless | 337.1 | Au1rxx-base64 |
| 72.29 | vless | 293.9 | Au1rxx-base64 |
| 72.26 | shadowsocks | 254.0 | Au1rxx-base64 |

### Top Source Quality

| Source | Score | Tested | Recommendation |
| --- | --- | --- | --- |
| ermaozi | 0.848 | 89 | prefer |
| mheidari-all | 0.565 | 134 | observe |
| Au1rxx-base64 | 0.543 | 377 | observe |
| Surfboard-tg-mixed | 0.3 | 5 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | 0 | observe |

<!-- AUTONODES_STATS_END -->

