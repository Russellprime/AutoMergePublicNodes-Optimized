# AutoNodes 每日报告

生成时间：2026-10-31 16:44:45

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 0/89 |
| 原始节点数 | 81266 |
| 去重后节点数 | 26297 |
| TCP 可达数 | 3000 |
| 真测通过数 | 65 |
| verified 输出数 | 65 |
| global 输出数 | 70 |
| all 输出数 | 26297 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 23.9 |
| fetch | 7.2 |
| generate | 13.5 |
| geo | 1.5 |
| probe | 101.2 |
| real_test | 75.6 |
| tcp | 78.1 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 4 | 1 | 3 | 25.0% |
| hysteria2 | 11 | 9 | 2 | 81.8% |
| shadowsocks | 96 | 27 | 69 | 28.1% |
| trojan | 112 | 63 | 49 | 56.2% |
| vless | 209 | 74 | 135 | 35.4% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:status | 68 |
| test_one_timeout:15.0s | 65 |
| geo:status | 63 |
| speed:ClientOSError | 37 |
| cn-block:TimeoutError | 8 |
| 204:ProxyError | 5 |
| 204:TimeoutError | 4 |
| geo:TimeoutError | 3 |
| cn-block:ProxyError | 2 |
| 204:ClientOSError | 1 |
| geo:ClientOSError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5950 |
| ConnectionRefusedError | 948 |
| OSError | 233 |
| gaierror | 168 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.507 | observe | 291 | 0.436 | 1751 |
| mheidari-all | 0.401 | observe | 132 | 0.318 | 14848 |
| DeltaKronecker-all | 0.349 | observe | 3 | 0.667 | 2848 |
| Surfboard-tg-mixed | 0.335 | observe | 1 | 1.0 | 7984 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| zhangkai | 0.257 | observe | 1 | 1.0 | 43 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4970 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10683 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5777 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Epodonios-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-oneclickvpnkeys | 0.131 | observe | 1 | 0.0 | 0 | 98 |
| ermaozi-get_subscribe | 0.144 | observe | 1 | 0.0 | 0 | 412 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-ConfigWireguard | 0.175 | observe | 0 | None | 0 | 2 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 475 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 366 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 361 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 244 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 222 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 221 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 213 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 191 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 186 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 110 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mahdibland-V2RayAggregator | 0.0 | 0 | 1 | 1 |
| tg-oneclickvpnkeys | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.318 | 42 | 90 | 132 |
| Au1rxx-base64 | 0.436 | 127 | 164 | 291 |
| DeltaKronecker-all | 0.667 | 2 | 1 | 3 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| Surfboard-tg-mixed | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14848 | yes | 4.96 | 0 |
| SoliSpirit-all | 10683 | yes | 3.14 | 0 |
| Surfboard-tg-mixed | 7984 | yes | 4.42 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.61 | 0 |
| barry-far-vless | 5990 | yes | 1.0 | 0 |
| Surfboard-tg-vless | 5777 | yes | 3.57 | 0 |
| 10ium-ScrapeCategorize-Vless | 4970 | yes | 0.79 | 0 |
| mahdibland-V2RayAggregator | 4635 | yes | 3.19 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.11 | 0 |
| DeltaKronecker-all | 2848 | yes | 6.12 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 136 |
| test_one_timeout | 65 |
| speed | 37 |
| 204 | 10 |
| cn-block | 10 |
