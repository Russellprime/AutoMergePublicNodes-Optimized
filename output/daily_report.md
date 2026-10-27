# AutoNodes 每日报告

生成时间：2026-10-27 06:08:46

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 13/0 |
| 清理建议：优先/观察 | 1/93 |
| 原始节点数 | 96324 |
| 去重后节点数 | 26586 |
| TCP 可达数 | 3000 |
| 真测通过数 | 104 |
| verified 输出数 | 104 |
| global 输出数 | 106 |
| all 输出数 | 26586 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 28.6 |
| fetch | 7.0 |
| generate | 13.4 |
| geo | 1.5 |
| probe | 103.0 |
| real_test | 93.2 |
| tcp | 79.6 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 88 | 74 | 14 | 84.1% |
| hysteria2 | 16 | 11 | 5 | 68.8% |
| shadowsocks | 99 | 34 | 65 | 34.3% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 57 | 50 | 7 | 87.7% |
| vless | 344 | 150 | 194 | 43.6% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:status | 81 |
| test_one_timeout:15.0s | 80 |
| speed:ClientOSError | 59 |
| geo:status | 44 |
| 204:ProxyError | 7 |
| 204:TimeoutError | 3 |
| cn-block:TimeoutError | 3 |
| 204:ClientOSError | 2 |
| cn-block:ProxyError | 2 |
| cn-block:ClientOSError | 2 |
| geo:ClientOSError | 1 |
| speed:ProxyError | 1 |
| speed:ClientPayloadError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6408 |
| ConnectionRefusedError | 1097 |
| gaierror | 290 |
| OSError | 240 |
| SSRFBlocked | 4 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.848 | prefer | 89 | 0.831 | 603 |
| mheidari-all | 0.565 | observe | 134 | 0.485 | 24431 |
| Au1rxx-base64 | 0.543 | observe | 377 | 0.475 | 1700 |
| Surfboard-tg-mixed | 0.3 | observe | 5 | 0.4 | 7021 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4988 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 3004 |
| Epodonios-all | 0.255 | observe | 0 | None | 7632 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5284 |
| barry-far-vless | 0.255 | observe | 0 | None | 5620 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-we | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-nodefree | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-yudou66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ArV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 456 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 347 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 342 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 225 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 203 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 202 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 194 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 172 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 167 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 91 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| SoliSpirit-all | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.4 | 2 | 3 | 5 |
| Au1rxx-base64 | 0.475 | 179 | 198 | 377 |
| mheidari-all | 0.485 | 65 | 69 | 134 |
| ermaozi | 0.831 | 74 | 15 | 89 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24431 | yes | 5.99 | 0 |
| SoliSpirit-all | 10267 | yes | 5.62 | 0 |
| Epodonios-all | 7632 | yes | 0.91 | 0 |
| Surfboard-tg-mixed | 7021 | yes | 4.94 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.38 | 0 |
| barry-far-vless | 5620 | yes | 1.95 | 0 |
| Surfboard-tg-vless | 5284 | yes | 3.72 | 0 |
| 10ium-ScrapeCategorize-Vless | 4988 | yes | 3.28 | 0 |
| mahdibland-V2RayAggregator | 4573 | yes | 0.99 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 4.32 | 0 |

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
| geo | 126 |
| test_one_timeout | 80 |
| speed | 61 |
| 204 | 12 |
| cn-block | 7 |
