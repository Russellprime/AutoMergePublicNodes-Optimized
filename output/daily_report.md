# AutoNodes 每日报告

生成时间：2026-10-31 11:37:36

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 13/0 |
| 清理建议：优先/观察 | 1/93 |
| 原始节点数 | 81178 |
| 去重后节点数 | 26408 |
| TCP 可达数 | 3000 |
| 真测通过数 | 110 |
| verified 输出数 | 110 |
| global 输出数 | 114 |
| all 输出数 | 26408 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 33.3 |
| fetch | 6.9 |
| generate | 13.7 |
| geo | 1.5 |
| probe | 102.9 |
| real_test | 94.7 |
| tcp | 76.8 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 88 | 70 | 18 | 79.5% |
| hysteria2 | 17 | 10 | 7 | 58.8% |
| shadowsocks | 155 | 41 | 114 | 26.5% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 163 | 110 | 53 | 67.5% |
| vless | 249 | 103 | 146 | 41.4% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:status | 102 |
| test_one_timeout:15.0s | 94 |
| speed:ClientOSError | 64 |
| geo:status | 33 |
| 204:ProxyError | 15 |
| 204:TimeoutError | 14 |
| cn-block:TimeoutError | 7 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 3 |
| geo:ClientOSError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5824 |
| ConnectionRefusedError | 966 |
| OSError | 234 |
| gaierror | 210 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.816 | prefer | 89 | 0.798 | 622 |
| Au1rxx-base64 | 0.65 | observe | 300 | 0.58 | 1751 |
| DeltaKronecker-all | 0.533 | observe | 14 | 0.571 | 2848 |
| mheidari-all | 0.469 | observe | 111 | 0.387 | 14723 |
| xiaoji235-airport-v2ray-all | 0.349 | observe | 3 | 0.667 | 6752 |
| Surfboard-tg-mixed | 0.325 | observe | 157 | 0.242 | 7861 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4970 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10588 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5698 |

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
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 474 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 365 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 360 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 243 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 221 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 220 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 212 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 190 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 185 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 109 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.242 | 38 | 119 | 157 |
| mheidari-all | 0.387 | 43 | 68 | 111 |
| DeltaKronecker-all | 0.571 | 8 | 6 | 14 |
| Au1rxx-base64 | 0.58 | 174 | 126 | 300 |
| xiaoji235-airport-v2ray-all | 0.667 | 2 | 1 | 3 |
| ermaozi | 0.798 | 71 | 18 | 89 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14723 | yes | 6.03 | 0 |
| SoliSpirit-all | 10588 | yes | 2.91 | 0 |
| Surfboard-tg-mixed | 7861 | yes | 4.37 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.52 | 0 |
| barry-far-vless | 5912 | yes | 1.2 | 0 |
| Surfboard-tg-vless | 5698 | yes | 3.57 | 0 |
| 10ium-ScrapeCategorize-Vless | 4970 | yes | 1.51 | 0 |
| mahdibland-V2RayAggregator | 4635 | yes | 3.29 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.29 | 0 |
| DeltaKronecker-all | 2848 | yes | 6.05 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 138 |
| test_one_timeout | 94 |
| speed | 64 |
| 204 | 32 |
| cn-block | 10 |
