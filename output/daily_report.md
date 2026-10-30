# AutoNodes 每日报告

生成时间：2026-10-30 21:56:14

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 13/0 |
| 清理建议：优先/观察 | 1/93 |
| 原始节点数 | 80827 |
| 去重后节点数 | 26314 |
| TCP 可达数 | 3000 |
| 真测通过数 | 105 |
| verified 输出数 | 105 |
| global 输出数 | 107 |
| all 输出数 | 26314 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 29.8 |
| fetch | 5.0 |
| generate | 10.3 |
| geo | 1.5 |
| probe | 82.6 |
| real_test | 59.6 |
| tcp | 76.1 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 0 | 1 | 0.0% |
| http | 28 | 24 | 4 | 85.7% |
| hysteria2 | 14 | 11 | 3 | 78.6% |
| shadowsocks | 97 | 21 | 76 | 21.6% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 173 | 110 | 63 | 63.6% |
| vless | 245 | 101 | 144 | 41.2% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:status | 136 |
| geo:status | 66 |
| test_one_timeout:15.0s | 34 |
| speed:ClientOSError | 30 |
| 204:TimeoutError | 7 |
| 204:ProxyError | 5 |
| cn-block:ClientOSError | 4 |
| 204:ClientOSError | 3 |
| cn-block:TimeoutError | 3 |
| geo:TimeoutError | 2 |
| geo:ProxyError | 2 |
| geo:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5751 |
| ConnectionRefusedError | 953 |
| gaierror | 249 |
| OSError | 236 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.855 | prefer | 28 | 0.857 | 550 |
| Surfboard-tg-mixed | 0.692 | observe | 47 | 0.617 | 7917 |
| mheidari-all | 0.56 | observe | 177 | 0.48 | 14611 |
| Au1rxx-base64 | 0.489 | observe | 306 | 0.418 | 1751 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4960 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2724 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10588 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5777 |

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
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 472 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 363 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 358 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 241 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 219 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 218 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 210 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 188 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 183 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 107 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.418 | 128 | 178 | 306 |
| mheidari-all | 0.48 | 85 | 92 | 177 |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.617 | 29 | 18 | 47 |
| ermaozi | 0.857 | 24 | 4 | 28 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14611 | yes | 3.46 | 0 |
| SoliSpirit-all | 10588 | yes | 3.73 | 0 |
| Surfboard-tg-mixed | 7917 | yes | 2.7 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.81 | 0 |
| barry-far-vless | 6013 | yes | 2.26 | 0 |
| Surfboard-tg-vless | 5777 | yes | 2.5 | 0 |
| 10ium-ScrapeCategorize-Vless | 4960 | yes | 2.42 | 0 |
| mahdibland-V2RayAggregator | 4459 | yes | 2.23 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.48 | 0 |
| DeltaKronecker-all | 2724 | yes | 4.31 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| anytls | 0.0 |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 207 |
| test_one_timeout | 34 |
| speed | 30 |
| 204 | 15 |
| cn-block | 7 |
