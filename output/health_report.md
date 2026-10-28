# AutoNodes Health Report

## Overview

| Metric | Value |
| --- | --- |
| Version | 2.5.0 |
| Updated | 2026-10-28 22:10:28 |
| Elapsed | 303.2s |
| Sources (total) | 107 |
| Sources (healthy) | 87 |
| Nodes (raw) | 99302 |
| Nodes (unique) | 27863 |
| Nodes (TCP pass) | 3000 |
| Nodes (probe pass) | 522 |
| Nodes (real-test pass) | 100 |
| Top links output | 100 |
| Clean IPs | 20 |
| Verified output | 100 |
| Global output | 102 |
| All output | 27863 |

## Stage Duration

| Stage | Seconds |
| --- | --- |
| fetch | 6.9 |
| geo | 1.7 |
| tcp | 86.2 |
| probe | 93.1 |
| real_test | 69.0 |
| china_check | 30.8 |
| write_verified | 0.1 |
| generate | 13.4 |

## Protocol Distribution

| Protocol | Count |
| --- | --- |
| vless | 62975 |
| vmess | 14226 |
| shadowsocks | 10772 |
| trojan | 8699 |
| hysteria2 | 2259 |
| shadowsocksr | 165 |
| http | 116 |
| socks | 52 |
| tuic | 16 |
| hysteria | 11 |
| anytls | 11 |

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
| 67.46 | http | 319.7 | 809.9 | 20.38 | 0.0 | 0.0 | 12.5 | 17.08 | ermaozi | 38.247.141.135 |
| 64.3 | vless | 265.3 | 517.1 | 21.64 | 0.0 | 10.0 | 5.61 | 8.76 | Au1rxx-base64 | 45.63.53.81 |
| 64.16 | vless | 275.5 | 506.3 | 21.4 | 0.0 | 10.0 | 5.61 | 8.76 | Au1rxx-base64 | 144.202.126.147 |
| 63.32 | trojan | 258.4 | 579.7 | 21.8 | 0.0 | 9.19 | 6.07 | 8.76 | Au1rxx-base64 | 66.163.114.106 |
| 63.21 | hysteria2 | 323.5 | 536.3 | 20.29 | 0.0 | 8.09 | 10.38 | 8.76 | Au1rxx-base64 | 66.94.121.46 |
| 63.21 | http | 324.3 | 630.7 | 20.27 | 0.0 | 0.0 | 12.5 | 17.08 | ermaozi | 64.98.50.100 |
| 63.2 | trojan | 263.6 | 579.2 | 21.68 | 0.0 | 9.19 | 6.07 | 8.76 | Au1rxx-base64 | 66.163.114.114 |
| 61.68 | trojan | 338.5 | 836.9 | 19.94 | 0.0 | 9.91 | 6.07 | 8.76 | Au1rxx-base64 | 66.23.203.21 |
| 61.67 | trojan | 270.7 | 602.9 | 21.51 | 0.0 | 9.51 | 6.07 | 8.76 | Au1rxx-base64 | 66.163.114.245 |
| 61.14 | http | 362.5 | 612.0 | 19.39 | 0.0 | 0.0 | 12.5 | 17.08 | ermaozi | 44.248.167.117 |
| 60.91 | trojan | 279.3 | 541.5 | 21.31 | 0.0 | 9.74 | 6.07 | 8.76 | Au1rxx-base64 | 66.163.112.171 |
| 60.64 | trojan | 276.0 | 542.8 | 21.39 | 0.0 | 9.74 | 6.07 | 8.76 | Au1rxx-base64 | 66.163.112.31 |
| 60.45 | http | 421.3 | 895.9 | 18.02 | 0.0 | 0.0 | 12.5 | 17.08 | ermaozi | 121.127.34.82 |
| 60.38 | vless | 365.0 | 733.9 | 19.33 | 0.0 | 9.58 | 5.61 | 8.76 | Au1rxx-base64 | 5.34.178.120 |
| 59.82 | hysteria2 | 294.3 | 693.9 | 20.96 | 0.0 | 6.22 | 10.38 | 8.76 | Au1rxx-base64 | 129.213.91.185 |
| 59.66 | trojan | 322.2 | 699.3 | 20.32 | 0.0 | 9.39 | 6.07 | 8.76 | Au1rxx-base64 | 216.238.80.100 |
| 59.21 | trojan | 272.1 | 558.4 | 21.48 | 0.0 | 9.43 | 6.07 | 8.76 | Au1rxx-base64 | 66.163.112.76 |
| 58.86 | vless | 370.8 | 789.3 | 19.2 | 0.0 | 9.54 | 5.61 | 8.76 | Au1rxx-base64 | 195.123.235.183 |
| 58.06 | trojan | 292.7 | 644.9 | 21.0 | 0.0 | 6.87 | 6.07 | 8.76 | Au1rxx-base64 | 66.163.112.242 |
| 58.0 | trojan | 271.6 | 592.3 | 21.49 | 0.0 | 9.18 | 6.07 | 8.76 | Au1rxx-base64 | 66.163.114.166 |

## Source Quality

| Source | Score | Pass Rate | Tested | Parsed Nodes | Recommendation |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.883 | 0.889 | 27 | 513 | prefer |
| mheidari-all | 0.642 | 0.563 | 103 | 33849 | observe |
| Surfboard-tg-mixed | 0.586 | 0.506 | 85 | 7686 | observe |
| Au1rxx-base64 | 0.436 | 0.365 | 304 | 1755 | observe |
| DeltaKronecker-all | 0.335 | 1.0 | 1 | 2801 | observe |
| xiaoji235-airport-v2ray-all | 0.287 | 0.5 | 2 | 6752 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5004 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10359 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5749 | observe |
| barry-far-vless | 0.255 | None | 0 | 5963 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4323 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1755 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## Real Test Failures

| Target | Reason | Status/Value | Count |
| --- | --- | --- | --- |
| geo | status | 429 | 125 |
| geo | status | 403 | 73 |
| test_one_timeout | 15.0s | - | 40 |
| speed | ClientOSError | - | 23 |
| 204 | TimeoutError | - | 5 |
| 204 | ClientOSError | - | 5 |
| cn-block | TimeoutError | - | 4 |
| cn-block | ProxyError | - | 3 |
| 204 | ProxyError | - | 2 |
| geo | TimeoutError | - | 2 |
| geo | ClientOSError | - | 1 |
| geo | ProxyError | - | 1 |

## Output Guard

| Prefix | Preserved previous | Previous count | Current proposed count | Retain ratio |
| --- | --- | --- | --- | --- |
| verified | False | 73 | 100 | - |
| global | False | 74 | 102 | - |

---

Generated by `core.report.write_health_report()`.
