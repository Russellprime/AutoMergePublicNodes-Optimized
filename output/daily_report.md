# AutoNodes 每日报告

生成时间：2026-10-31 03:43:14

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 13/0 |
| 清理建议：优先/观察 | 2/92 |
| 原始节点数 | 80650 |
| 去重后节点数 | 26339 |
| TCP 可达数 | 3000 |
| 真测通过数 | 108 |
| verified 输出数 | 108 |
| global 输出数 | 111 |
| all 输出数 | 26339 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 32.4 |
| fetch | 5.2 |
| generate | 10.1 |
| geo | 1.4 |
| probe | 87.3 |
| real_test | 90.4 |
| tcp | 76.1 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 93 | 77 | 16 | 82.8% |
| hysteria2 | 12 | 10 | 2 | 83.3% |
| shadowsocks | 107 | 61 | 46 | 57.0% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 172 | 167 | 5 | 97.1% |
| vless | 296 | 113 | 183 | 38.2% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 77 |
| speed:ClientOSError | 64 |
| geo:status | 52 |
| geo:status | 41 |
| 204:ProxyError | 5 |
| cn-block:ClientOSError | 4 |
| 204:ClientOSError | 3 |
| geo:ClientOSError | 2 |
| geo:ProxyError | 2 |
| 204:TimeoutError | 2 |
| cn-block:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5807 |
| ConnectionRefusedError | 932 |
| OSError | 248 |
| gaierror | 213 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.848 | prefer | 94 | 0.83 | 622 |
| Au1rxx-base64 | 0.77 | prefer | 271 | 0.701 | 1751 |
| Surfboard-tg-mixed | 0.592 | observe | 164 | 0.512 | 7827 |
| mheidari-all | 0.583 | observe | 151 | 0.503 | 14594 |
| xiaoji235-airport-v2ray-all | 0.349 | observe | 3 | 0.667 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4960 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2724 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10521 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5680 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-we | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.025 | observe | 0 | None | 1 | 0 |
| Epodonios-all | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-nodefree | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-yudou66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 473 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 364 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 359 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 242 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 220 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 219 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 211 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 189 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 184 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 108 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mheidari-all | 0.503 | 76 | 75 | 151 |
| Surfboard-tg-mixed | 0.512 | 84 | 80 | 164 |
| xiaoji235-airport-v2ray-all | 0.667 | 2 | 1 | 3 |
| Au1rxx-base64 | 0.701 | 190 | 81 | 271 |
| ermaozi | 0.83 | 78 | 16 | 94 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14594 | yes | 3.57 | 0 |
| SoliSpirit-all | 10521 | yes | 2.44 | 0 |
| Surfboard-tg-mixed | 7827 | yes | 2.57 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.89 | 0 |
| barry-far-vless | 5990 | yes | 0.75 | 0 |
| Surfboard-tg-vless | 5680 | yes | 3.15 | 0 |
| 10ium-ScrapeCategorize-Vless | 4960 | yes | 0.92 | 0 |
| mahdibland-V2RayAggregator | 4459 | yes | 2.29 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 0.99 | 0 |
| DeltaKronecker-all | 2724 | yes | 4.41 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 97 |
| test_one_timeout | 77 |
| speed | 64 |
| 204 | 10 |
| cn-block | 5 |
