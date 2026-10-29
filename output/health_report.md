# AutoNodes Health Report

## Overview

| Metric | Value |
| --- | --- |
| Version | 2.5.0 |
| Updated | 2026-10-29 03:57:24 |
| Elapsed | 357.2s |
| Sources (total) | 107 |
| Sources (healthy) | 87 |
| Nodes (raw) | 99442 |
| Nodes (unique) | 27940 |
| Nodes (TCP pass) | 3000 |
| Nodes (probe pass) | 693 |
| Nodes (real-test pass) | 101 |
| Top links output | 101 |
| Clean IPs | 20 |
| Verified output | 101 |
| Global output | 104 |
| All output | 27940 |

## Stage Duration

| Stage | Seconds |
| --- | --- |
| fetch | 7.7 |
| geo | 1.7 |
| tcp | 87.8 |
| probe | 105.5 |
| real_test | 100.9 |
| china_check | 36.8 |
| write_verified | 0.1 |
| generate | 14.9 |

## Protocol Distribution

| Protocol | Count |
| --- | --- |
| vless | 62799 |
| vmess | 14180 |
| shadowsocks | 10805 |
| trojan | 8830 |
| hysteria2 | 2367 |
| http | 203 |
| shadowsocksr | 168 |
| socks | 49 |
| tuic | 16 |
| anytls | 14 |
| hysteria | 11 |

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
| 67.24 | vless | 212.8 | 503.8 | 22.85 | 0.0 | 9.81 | 5.86 | 8.72 | Au1rxx-base64 | 144.202.126.147 |
| 67.17 | http | 326.1 | 723.1 | 20.23 | 0.0 | 0.0 | 12.93 | 17.66 | ermaozi | 44.248.167.117 |
| 66.99 | trojan | 245.0 | 556.4 | 22.11 | 0.0 | 8.35 | 10.31 | 8.72 | Au1rxx-base64 | 66.163.112.171 |
| 66.92 | trojan | 242.5 | 550.2 | 22.16 | 0.0 | 8.35 | 10.31 | 8.72 | Au1rxx-base64 | 66.163.112.31 |
| 66.81 | trojan | 241.9 | 544.3 | 22.18 | 0.0 | 8.36 | 10.31 | 8.72 | Au1rxx-base64 | 66.163.112.76 |
| 66.62 | vless | 213.7 | 490.0 | 22.83 | 0.0 | 9.21 | 5.86 | 8.72 | Au1rxx-base64 | 45.63.53.81 |
| 65.98 | hysteria2 | 263.5 | 197.2 | 21.68 | 7.61 | 9.79 | 10.0 | 8.72 | Au1rxx-base64 | 45.32.10.7 |
| 65.1 | http | 306.4 | 672.8 | 20.69 | 0.0 | 0.0 | 12.93 | 17.66 | ermaozi | 149.22.88.65 |
| 64.7 | trojan | 280.9 | 616.6 | 21.27 | 0.0 | 9.27 | 10.31 | 8.72 | Au1rxx-base64 | 66.163.114.114 |
| 63.66 | vless | 236.7 | 552.5 | 22.3 | 0.0 | 9.78 | 5.86 | 8.72 | Au1rxx-base64 | 156.229.160.98 |
| 63.56 | trojan | 319.4 | 743.4 | 20.38 | 0.0 | 7.24 | 10.31 | 8.72 | Au1rxx-base64 | 66.163.114.106 |
| 63.55 | http | 346.7 | 654.3 | 19.75 | 0.0 | 0.0 | 12.93 | 17.66 | ermaozi | 64.98.50.100 |
| 63.44 | hysteria2 | 256.3 | 603.7 | 21.85 | 0.0 | 7.26 | 10.0 | 8.72 | Au1rxx-base64 | 66.94.121.46 |
| 62.98 | trojan | 275.6 | 604.2 | 21.4 | 0.0 | 7.25 | 10.31 | 8.72 | Au1rxx-base64 | 66.163.114.245 |
| 62.48 | http | 351.9 | 694.3 | 19.63 | 0.0 | 0.0 | 12.93 | 17.66 | ermaozi | 38.247.141.135 |
| 62.26 | trojan | 243.2 | 551.7 | 22.15 | 0.0 | 7.33 | 10.31 | 8.72 | Au1rxx-base64 | 66.163.112.242 |
| 61.38 | trojan | 281.2 | 615.9 | 21.27 | 0.0 | 9.27 | 10.31 | 8.72 | Au1rxx-base64 | 66.163.114.166 |
| 61.37 | trojan | 370.3 | 297.8 | 19.21 | 3.83 | 9.72 | 10.31 | 8.72 | Au1rxx-base64 | 45.32.52.173 |
| 61.15 | vless | 230.2 | 443.5 | 22.45 | 0.0 | 0.0 | 5.86 | 12.84 | mheidari-all | 47.251.108.158 |
| 61.01 | vless | 240.2 | 537.6 | 22.22 | 0.0 | 9.21 | 5.86 | 8.72 | Au1rxx-base64 | 156.229.164.160 |

## Source Quality

| Source | Score | Pass Rate | Tested | Parsed Nodes | Recommendation |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 1.0 | 0.972 | 36 | 7703 | prefer |
| ermaozi | 0.68 | 0.662 | 71 | 560 | observe |
| Au1rxx-base64 | 0.672 | 0.606 | 289 | 1692 | observe |
| mheidari-all | 0.506 | 0.425 | 294 | 34088 | observe |
| xiaoji235-airport-v2ray-all | 0.349 | 0.667 | 3 | 6752 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5004 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2801 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10346 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5686 | observe |
| barry-far-vless | 0.255 | None | 0 | 5902 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4323 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.243 | None | 0 | 1692 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## Real Test Failures

| Target | Reason | Status/Value | Count |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 118 |
| geo | status | 403 | 68 |
| speed | ClientOSError | - | 40 |
| geo | status | 429 | 32 |
| geo | ProxyError | - | 17 |
| 204 | ProxyError | - | 8 |
| cn-block | ProxyError | - | 6 |
| 204 | TimeoutError | - | 5 |
| speed | ProxyError | - | 4 |
| 204 | ClientOSError | - | 4 |
| cn-block | ClientOSError | - | 3 |
| geo | ClientOSError | - | 1 |
| geo | TimeoutError | - | 1 |
| speed | TimeoutError | - | 1 |
| cn-block | TimeoutError | - | 1 |

## Output Guard

| Prefix | Preserved previous | Previous count | Current proposed count | Retain ratio |
| --- | --- | --- | --- | --- |
| verified | False | 100 | 101 | - |
| global | False | 102 | 104 | - |

---

Generated by `core.report.write_health_report()`.
