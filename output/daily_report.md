# AutoNodes 每日报告

生成时间：2026-10-28 17:57:40

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 1/92 |
| 原始节点数 | 107541 |
| 去重后节点数 | 27945 |
| TCP 可达数 | 3000 |
| 真测通过数 | 73 |
| verified 输出数 | 73 |
| global 输出数 | 74 |
| all 输出数 | 27945 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 21.6 |
| fetch | 6.1 |
| generate | 8.6 |
| geo | 1.4 |
| probe | 73.2 |
| real_test | 66.6 |
| tcp | 88.6 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 28 | 24 | 4 | 85.7% |
| hysteria2 | 11 | 8 | 3 | 72.7% |
| shadowsocks | 90 | 21 | 69 | 23.3% |
| trojan | 87 | 35 | 52 | 40.2% |
| vless | 204 | 76 | 128 | 37.3% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:status | 78 |
| geo:status | 74 |
| test_one_timeout:15.0s | 66 |
| 204:TimeoutError | 11 |
| speed:ClientOSError | 9 |
| 204:ProxyError | 6 |
| cn-block:ProxyError | 4 |
| geo:TimeoutError | 2 |
| cn-block:TimeoutError | 2 |
| geo:ClientOSError | 1 |
| 204:ClientOSError | 1 |
| cn-block:ClientOSError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 7175 |
| ConnectionRefusedError | 1117 |
| OSError | 241 |
| gaierror | 228 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.854 | prefer | 28 | 0.857 | 513 |
| Au1rxx-base64 | 0.438 | observe | 290 | 0.366 | 1777 |
| Surfboard-tg-mixed | 0.424 | observe | 30 | 0.333 | 7672 |
| mheidari-all | 0.399 | observe | 70 | 0.314 | 33924 |
| DeltaKronecker-all | 0.335 | observe | 1 | 1.0 | 2801 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5004 |
| Epodonios-all | 0.255 | observe | 0 | None | 8008 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10430 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-we | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-nodefree | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-yudou66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 9 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 464 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 355 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 350 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 233 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 211 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 210 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 202 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 180 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 175 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 99 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mheidari-all | 0.314 | 22 | 48 | 70 |
| Surfboard-tg-mixed | 0.333 | 10 | 20 | 30 |
| Au1rxx-base64 | 0.366 | 106 | 184 | 290 |
| ermaozi | 0.857 | 24 | 4 | 28 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| DeltaKronecker-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 33924 | yes | 3.73 | 0 |
| SoliSpirit-all | 10430 | yes | 3.19 | 0 |
| Epodonios-all | 8008 | yes | 1.9 | 0 |
| Surfboard-tg-mixed | 7672 | yes | 2.36 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.15 | 0 |
| barry-far-vless | 5916 | yes | 1.37 | 0 |
| Surfboard-tg-vless | 5703 | yes | 2.47 | 0 |
| 10ium-ScrapeCategorize-Vless | 5004 | yes | 1.26 | 0 |
| mahdibland-V2RayAggregator | 4500 | yes | 1.71 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 1.09 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 156 |
| test_one_timeout | 66 |
| 204 | 18 |
| speed | 9 |
| cn-block | 7 |
