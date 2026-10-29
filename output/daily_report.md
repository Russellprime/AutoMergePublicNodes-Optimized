# AutoNodes 每日报告

生成时间：2026-10-29 12:10:40

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 1/92 |
| 原始节点数 | 99820 |
| 去重后节点数 | 28351 |
| TCP 可达数 | 3000 |
| 真测通过数 | 98 |
| verified 输出数 | 98 |
| global 输出数 | 100 |
| all 输出数 | 28351 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 36.1 |
| fetch | 4.0 |
| generate | 8.4 |
| geo | 1.5 |
| probe | 76.1 |
| real_test | 82.9 |
| tcp | 92.8 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 71 | 62 | 9 | 87.3% |
| hysteria2 | 12 | 6 | 6 | 50.0% |
| shadowsocks | 132 | 39 | 93 | 29.5% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 106 | 82 | 24 | 77.4% |
| vless | 199 | 98 | 101 | 49.2% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:status | 72 |
| test_one_timeout:15.0s | 56 |
| geo:status | 53 |
| speed:ClientOSError | 21 |
| 204:TimeoutError | 9 |
| 204:ProxyError | 6 |
| cn-block:TimeoutError | 4 |
| cn-block:ProxyError | 4 |
| cn-block:ClientOSError | 3 |
| geo:ProxyError | 2 |
| 204:ClientOSError | 2 |
| geo:ClientOSError | 1 |
| geo:TimeoutError | 1 |
| speed:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 7452 |
| ConnectionRefusedError | 1066 |
| OSError | 237 |
| gaierror | 160 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.885 | prefer | 71 | 0.873 | 560 |
| Au1rxx-base64 | 0.636 | observe | 280 | 0.568 | 1716 |
| mheidari-all | 0.54 | observe | 48 | 0.458 | 34088 |
| Surfboard-tg-mixed | 0.44 | observe | 123 | 0.358 | 7779 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5005 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2709 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10421 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5820 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-we | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.025 | observe | 0 | None | 1 | 0 |
| Epodonios-all | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-nodefree | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-yudou66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 7 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 467 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 358 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 353 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 236 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 214 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 213 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 205 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 183 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 178 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 102 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.358 | 44 | 79 | 123 |
| mheidari-all | 0.458 | 22 | 26 | 48 |
| Au1rxx-base64 | 0.568 | 159 | 121 | 280 |
| ermaozi | 0.873 | 62 | 9 | 71 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 34088 | yes | 3.27 | 0 |
| SoliSpirit-all | 10421 | yes | 1.85 | 0 |
| Surfboard-tg-mixed | 7779 | yes | 1.78 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.25 | 0 |
| barry-far-vless | 5941 | yes | 1.28 | 0 |
| Surfboard-tg-vless | 5820 | yes | 2.05 | 0 |
| 10ium-ScrapeCategorize-Vless | 5005 | yes | 1.23 | 0 |
| mahdibland-V2RayAggregator | 4444 | yes | 1.5 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.52 | 0 |
| DeltaKronecker-all | 2709 | yes | 3.34 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 129 |
| test_one_timeout | 56 |
| speed | 22 |
| 204 | 17 |
| cn-block | 11 |
