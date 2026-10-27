# AutoNodes 每日报告

生成时间：2026-10-27 08:17:13

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 13/0 |
| 清理建议：优先/观察 | 2/92 |
| 原始节点数 | 96374 |
| 去重后节点数 | 26565 |
| TCP 可达数 | 3000 |
| 真测通过数 | 108 |
| verified 输出数 | 108 |
| global 输出数 | 114 |
| all 输出数 | 26565 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 37.8 |
| fetch | 6.5 |
| generate | 11.7 |
| geo | 1.6 |
| probe | 99.7 |
| real_test | 77.3 |
| tcp | 83.1 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 87 | 73 | 14 | 83.9% |
| hysteria2 | 12 | 8 | 4 | 66.7% |
| shadowsocks | 84 | 34 | 50 | 40.5% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 83 | 66 | 17 | 79.5% |
| vless | 273 | 142 | 131 | 52.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:status | 65 |
| test_one_timeout:15.0s | 48 |
| geo:status | 47 |
| speed:ClientOSError | 27 |
| 204:ClientOSError | 11 |
| cn-block:TimeoutError | 5 |
| 204:ProxyError | 4 |
| 204:TimeoutError | 4 |
| geo:ClientOSError | 2 |
| cn-block:ClientOSError | 2 |
| cn-block:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound: start inbound/socks[socks-in]: listen tcp 127.0.0.1:30990: bind: address already in use | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6654 |
| ConnectionRefusedError | 1084 |
| OSError | 238 |
| gaierror | 196 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.848 | prefer | 89 | 0.831 | 603 |
| Surfboard-tg-mixed | 0.716 | prefer | 20 | 0.65 | 7021 |
| DeltaKronecker-all | 0.664 | observe | 9 | 1.0 | 3004 |
| Au1rxx-base64 | 0.61 | observe | 342 | 0.541 | 1722 |
| mheidari-all | 0.61 | observe | 81 | 0.531 | 24516 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4988 |
| Epodonios-all | 0.255 | observe | 0 | None | 7509 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10295 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5284 |

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
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 458 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 349 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 344 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 227 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 205 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 204 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 196 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 174 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 169 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 93 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.531 | 43 | 38 | 81 |
| Au1rxx-base64 | 0.541 | 185 | 157 | 342 |
| Surfboard-tg-mixed | 0.65 | 13 | 7 | 20 |
| ermaozi | 0.831 | 74 | 15 | 89 |
| DeltaKronecker-all | 1.0 | 9 | 0 | 9 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24516 | yes | 5.66 | 0 |
| SoliSpirit-all | 10295 | yes | 2.88 | 0 |
| Epodonios-all | 7509 | yes | 3.11 | 0 |
| Surfboard-tg-mixed | 7021 | yes | 4.7 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.74 | 0 |
| barry-far-vless | 5620 | yes | 0.92 | 0 |
| Surfboard-tg-vless | 5284 | yes | 3.81 | 0 |
| 10ium-ScrapeCategorize-Vless | 4988 | yes | 1.31 | 0 |
| mahdibland-V2RayAggregator | 4573 | yes | 2.79 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 1.08 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 114 |
| test_one_timeout | 48 |
| speed | 27 |
| 204 | 19 |
| cn-block | 9 |
| sing-box exited 1 | 1 |
