# AutoNodes 每日报告

生成时间：2026-10-30 17:50:27

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 13/0 |
| 清理建议：优先/观察 | 1/93 |
| 原始节点数 | 100585 |
| 去重后节点数 | 27646 |
| TCP 可达数 | 3000 |
| 真测通过数 | 111 |
| verified 输出数 | 111 |
| global 输出数 | 112 |
| all 输出数 | 27646 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 26.0 |
| fetch | 7.6 |
| generate | 14.5 |
| geo | 1.5 |
| probe | 95.3 |
| real_test | 79.8 |
| tcp | 86.8 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 28 | 24 | 4 | 85.7% |
| hysteria2 | 13 | 10 | 3 | 76.9% |
| shadowsocks | 97 | 31 | 66 | 32.0% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 140 | 98 | 42 | 70.0% |
| vless | 201 | 74 | 127 | 36.8% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:status | 73 |
| geo:status | 62 |
| test_one_timeout:15.0s | 57 |
| speed:ClientOSError | 19 |
| 204:TimeoutError | 9 |
| 204:ClientOSError | 6 |
| 204:ProxyError | 6 |
| cn-block:TimeoutError | 4 |
| cn-block:ProxyError | 3 |
| geo:ClientOSError | 1 |
| geo:TimeoutError | 1 |
| speed:TimeoutError | 1 |
| cn-block:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6824 |
| ConnectionRefusedError | 1118 |
| gaierror | 258 |
| OSError | 242 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.855 | prefer | 28 | 0.857 | 550 |
| mheidari-all | 0.634 | observe | 63 | 0.556 | 34258 |
| Surfboard-tg-mixed | 0.536 | observe | 66 | 0.455 | 7967 |
| Au1rxx-base64 | 0.53 | observe | 320 | 0.459 | 1751 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4960 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10582 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5801 |
| barry-far-vless | 0.255 | observe | 0 | None | 6035 |

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
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 471 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 362 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 357 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 240 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 218 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 217 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 209 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 187 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 182 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 106 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.455 | 30 | 36 | 66 |
| Au1rxx-base64 | 0.459 | 147 | 173 | 320 |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.556 | 35 | 28 | 63 |
| ermaozi | 0.857 | 24 | 4 | 28 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 34258 | yes | 6.65 | 0 |
| SoliSpirit-all | 10582 | yes | 1.79 | 0 |
| Surfboard-tg-mixed | 7967 | yes | 3.58 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.52 | 0 |
| barry-far-vless | 6035 | yes | 0.83 | 0 |
| Surfboard-tg-vless | 5801 | yes | 4.03 | 0 |
| 10ium-ScrapeCategorize-Vless | 4960 | yes | 1.27 | 0 |
| mahdibland-V2RayAggregator | 4445 | yes | 3.08 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.35 | 0 |
| DeltaKronecker-all | 2724 | yes | 6.61 | 0 |

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
| geo | 137 |
| test_one_timeout | 57 |
| 204 | 21 |
| speed | 20 |
| cn-block | 8 |
