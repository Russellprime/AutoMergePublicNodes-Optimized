# AutoNodes Health Report

## Overview

| Metric | Value |
| --- | --- |
| Version | 2.5.0 |
| Updated | 2026-10-27 08:03:08 |
| Elapsed | 309.2s |
| Sources (total) | 107 |
| Sources (healthy) | 88 |
| Nodes (raw) | 96374 |
| Nodes (unique) | 26563 |
| Nodes (TCP pass) | 3000 |
| Nodes (probe pass) | 540 |
| Nodes (real-test pass) | 113 |
| Top links output | 113 |
| Clean IPs | 20 |
| Verified output | 113 |
| Global output | 116 |
| All output | 26563 |

## Stage Duration

| Stage | Seconds |
| --- | --- |
| fetch | 7.3 |
| geo | 1.5 |
| tcp | 79.8 |
| probe | 103.3 |
| real_test | 78.8 |
| china_check | 23.3 |
| write_verified | 0.3 |
| generate | 13.0 |

## Protocol Distribution

| Protocol | Count |
| --- | --- |
| vless | 56287 |
| vmess | 17766 |
| shadowsocks | 12759 |
| trojan | 7585 |
| hysteria2 | 1376 |
| http | 324 |
| shadowsocksr | 171 |
| socks | 57 |
| anytls | 25 |
| hysteria | 18 |
| tuic | 6 |

## Ranking Weights

| Factor | Weight |
| --- | --- |
| latency | 25.0 |
| jitter | 15.0 |
| tcp | 10.0 |
| speed | 10.0 |
| fingerprint_resistance | 5.0 |
| protocol_history | 15.0 |
| source_history | 20.0 |

## Top Node Scores

| Score | Protocol | Latency(ms) | Jitter(ms) | Latency pts | Jitter pts | TCP pts | Protocol-history pts | Source-history pts | Source | Server |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 66.04 | vless | 290.0 | 719.1 | 21.07 | 0.0 | 7.56 | 6.55 | 10.86 | Au1rxx-base64 | 66.70.179.198 |
| 65.85 | trojan | 272.6 | 610.6 | 21.47 | 0.0 | 8.05 | 12.97 | 10.86 | Au1rxx-base64 | 216.152.155.54 |
| 65.67 | trojan | 280.1 | 628.5 | 21.29 | 0.0 | 8.05 | 12.97 | 10.86 | Au1rxx-base64 | 216.152.155.158 |
| 65.56 | trojan | 284.9 | 626.4 | 21.18 | 0.0 | 8.05 | 12.97 | 10.86 | Au1rxx-base64 | 216.152.155.176 |
| 65.33 | http | 363.4 | 835.9 | 19.37 | 0.0 | 0.0 | 12.5 | 16.96 | ermaozi | 206.223.161.47 |
| 65.15 | trojan | 278.4 | 613.4 | 21.33 | 0.0 | 7.49 | 12.97 | 10.86 | Au1rxx-base64 | 216.152.155.59 |
| 64.98 | trojan | 253.2 | 642.5 | 21.92 | 0.0 | 6.73 | 12.97 | 10.86 | Au1rxx-base64 | 66.163.122.25 |
| 64.8 | trojan | 261.0 | 649.2 | 21.74 | 0.0 | 6.73 | 12.97 | 10.86 | Au1rxx-base64 | 66.163.122.7 |
| 64.79 | vless | 314.3 | 735.8 | 20.5 | 0.0 | 8.82 | 6.55 | 10.86 | Au1rxx-base64 | 169.40.42.163 |
| 64.43 | vless | 331.5 | 717.9 | 20.1 | 0.0 | 8.11 | 6.55 | 10.86 | Au1rxx-base64 | 5.34.178.120 |
| 64.33 | trojan | 273.2 | 607.9 | 21.45 | 0.0 | 6.55 | 12.97 | 10.86 | Au1rxx-base64 | 216.152.155.23 |
| 64.17 | vless | 242.4 | 587.9 | 22.17 | 0.0 | 7.59 | 6.55 | 10.86 | Au1rxx-base64 | 195.123.235.183 |
| 63.46 | http | 369.6 | 850.3 | 19.22 | 0.0 | 0.0 | 12.5 | 16.96 | ermaozi | 12.202.180.118 |
| 63.15 | http | 359.8 | 836.0 | 19.45 | 0.0 | 0.0 | 12.5 | 16.96 | ermaozi | 206.223.183.13 |
| 63.08 | vless | 266.0 | 667.2 | 21.62 | 0.0 | 9.05 | 6.55 | 10.86 | Au1rxx-base64 | 159.89.87.21 |
| 62.61 | vless | 377.3 | 930.6 | 19.04 | 0.0 | 8.82 | 6.55 | 10.86 | Au1rxx-base64 | 169.40.42.90 |
| 62.26 | vless | 357.1 | 869.2 | 19.51 | 0.0 | 9.06 | 6.55 | 10.86 | Au1rxx-base64 | 169.40.42.35 |
| 62.16 | vless | 369.8 | 912.1 | 19.22 | 0.0 | 7.65 | 6.55 | 10.86 | Au1rxx-base64 | 169.40.42.231 |
| 62.0 | trojan | 310.7 | 690.0 | 20.59 | 0.0 | 7.34 | 12.97 | 10.86 | Au1rxx-base64 | 216.152.156.49 |
| 61.84 | http | 372.9 | 817.8 | 19.15 | 0.0 | 0.0 | 12.5 | 16.96 | ermaozi | 12.202.180.10 |

## Source Quality

| Source | Score | Pass Rate | Tested | Parsed Nodes | Recommendation |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.852 | 0.835 | 91 | 603 | prefer |
| Au1rxx-base64 | 0.623 | 0.555 | 357 | 1722 | observe |
| mheidari-all | 0.611 | 0.532 | 79 | 24516 | observe |
| Surfboard-tg-mixed | 0.286 | 0.231 | 13 | 7021 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4988 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 3004 | observe |
| Epodonios-all | 0.255 | None | 0 | 7509 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10295 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5284 | observe |
| barry-far-vless | 0.255 | None | 0 | 5620 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4573 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.244 | None | 0 | 1722 | observe |

## Real Test Failures

| Target | Reason | Status/Value | Count |
| --- | --- | --- | --- |
| geo | status | 403 | 68 |
| test_one_timeout | 15.0s | - | 60 |
| geo | status | 429 | 34 |
| speed | ClientOSError | - | 33 |
| 204 | ProxyError | - | 10 |
| 204 | ClientOSError | - | 6 |
| 204 | TimeoutError | - | 4 |
| cn-block | TimeoutError | - | 3 |
| geo | ClientOSError | - | 1 |
| geo | ProxyError | - | 1 |
| cn-block | ProxyError | - | 1 |

## Output Guard

| Prefix | Preserved previous | Previous count | Current proposed count | Retain ratio |
| --- | --- | --- | --- | --- |
| verified | False | 104 | 113 | - |
| global | False | 106 | 116 | - |

---

Generated by `core.report.write_health_report()`.
