# AutoNodes 每日报告

生成时间：2026-10-29 03:57:50

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 1/92 |
| 原始节点数 | 99442 |
| 去重后节点数 | 27940 |
| TCP 可达数 | 3000 |
| 真测通过数 | 101 |
| verified 输出数 | 101 |
| global 输出数 | 104 |
| all 输出数 | 27940 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 36.8 |
| fetch | 7.7 |
| generate | 14.9 |
| geo | 1.7 |
| probe | 105.5 |
| real_test | 100.9 |
| tcp | 87.8 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 71 | 47 | 24 | 66.2% |
| hysteria2 | 13 | 12 | 1 | 92.3% |
| shadowsocks | 99 | 42 | 57 | 42.4% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 126 | 115 | 11 | 91.3% |
| vless | 383 | 168 | 215 | 43.9% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 118 |
| geo:status | 68 |
| speed:ClientOSError | 40 |
| geo:status | 32 |
| geo:ProxyError | 17 |
| 204:ProxyError | 8 |
| cn-block:ProxyError | 6 |
| 204:TimeoutError | 5 |
| speed:ProxyError | 4 |
| 204:ClientOSError | 4 |
| cn-block:ClientOSError | 3 |
| geo:ClientOSError | 1 |
| geo:TimeoutError | 1 |
| speed:TimeoutError | 1 |
| cn-block:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6957 |
| ConnectionRefusedError | 1075 |
| gaierror | 260 |
| OSError | 238 |
| SSRFBlocked | 5 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 1.0 | prefer | 36 | 0.972 | 7703 |
| ermaozi | 0.68 | observe | 71 | 0.662 | 560 |
| Au1rxx-base64 | 0.672 | observe | 289 | 0.606 | 1692 |
| mheidari-all | 0.506 | observe | 294 | 0.425 | 34088 |
| xiaoji235-airport-v2ray-all | 0.349 | observe | 3 | 0.667 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5004 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2801 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10346 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5686 |

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
| Pawdroid | 0.175 | observe | 0 | None | 0 | 8 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 466 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 357 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 352 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 235 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 213 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 212 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 204 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 182 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 177 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 101 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mheidari-all | 0.425 | 125 | 169 | 294 |
| Au1rxx-base64 | 0.606 | 175 | 114 | 289 |
| ermaozi | 0.662 | 47 | 24 | 71 |
| xiaoji235-airport-v2ray-all | 0.667 | 2 | 1 | 3 |
| Surfboard-tg-mixed | 0.972 | 35 | 1 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 34088 | yes | 6.27 | 0 |
| SoliSpirit-all | 10346 | yes | 5.82 | 0 |
| Surfboard-tg-mixed | 7703 | yes | 4.07 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.79 | 0 |
| barry-far-vless | 5902 | yes | 2.67 | 0 |
| Surfboard-tg-vless | 5686 | yes | 4.27 | 0 |
| 10ium-ScrapeCategorize-Vless | 5004 | yes | 2.9 | 0 |
| mahdibland-V2RayAggregator | 4323 | yes | 3.06 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 2.99 | 0 |
| DeltaKronecker-all | 2801 | yes | 6.71 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 119 |
| test_one_timeout | 118 |
| speed | 45 |
| 204 | 17 |
| cn-block | 10 |
