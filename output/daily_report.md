# AutoNodes 每日报告

生成时间：2026-10-30 12:03:05

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 1/92 |
| 原始节点数 | 100173 |
| 去重后节点数 | 27741 |
| TCP 可达数 | 3000 |
| 真测通过数 | 77 |
| verified 输出数 | 77 |
| global 输出数 | 79 |
| all 输出数 | 27741 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 30.1 |
| fetch | 6.1 |
| generate | 11.8 |
| geo | 1.5 |
| probe | 89.0 |
| real_test | 82.1 |
| tcp | 88.9 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 20 | 16 | 4 | 80.0% |
| hysteria2 | 13 | 9 | 4 | 69.2% |
| shadowsocks | 154 | 47 | 107 | 30.5% |
| trojan | 156 | 109 | 47 | 69.9% |
| vless | 212 | 102 | 110 | 48.1% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:status | 74 |
| test_one_timeout:15.0s | 72 |
| geo:status | 66 |
| speed:ClientOSError | 23 |
| 204:ProxyError | 10 |
| cn-block:TimeoutError | 6 |
| cn-block:ClientOSError | 5 |
| 204:TimeoutError | 4 |
| 204:ClientOSError | 4 |
| cn-block:ProxyError | 3 |
| geo:status | 2 |
| geo:ClientOSError | 1 |
| geo:ProxyError | 1 |
| geo:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 7129 |
| ConnectionRefusedError | 1092 |
| OSError | 241 |
| gaierror | 203 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.793 | prefer | 20 | 0.8 | 515 |
| Au1rxx-base64 | 0.668 | observe | 331 | 0.598 | 1751 |
| Surfboard-tg-mixed | 0.436 | observe | 130 | 0.354 | 7902 |
| mheidari-all | 0.372 | observe | 70 | 0.286 | 34171 |
| DeltaKronecker-all | 0.349 | observe | 3 | 0.667 | 2724 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4960 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10513 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5822 |

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
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 470 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 361 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 356 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 239 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 217 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 216 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 208 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 186 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 181 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 105 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mheidari-all | 0.286 | 20 | 50 | 70 |
| Surfboard-tg-mixed | 0.354 | 46 | 84 | 130 |
| Au1rxx-base64 | 0.598 | 198 | 133 | 331 |
| DeltaKronecker-all | 0.667 | 2 | 1 | 3 |
| ermaozi | 0.8 | 16 | 4 | 20 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 34171 | yes | 5.43 | 0 |
| SoliSpirit-all | 10513 | yes | 2.39 | 0 |
| Surfboard-tg-mixed | 7902 | yes | 4.12 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.79 | 0 |
| barry-far-vless | 5942 | yes | 0.72 | 0 |
| Surfboard-tg-vless | 5822 | yes | 3.22 | 0 |
| 10ium-ScrapeCategorize-Vless | 4960 | yes | 0.9 | 0 |
| mahdibland-V2RayAggregator | 4445 | yes | 0.12 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.18 | 0 |
| DeltaKronecker-all | 2724 | yes | 5.49 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 145 |
| test_one_timeout | 72 |
| speed | 23 |
| 204 | 18 |
| cn-block | 14 |
