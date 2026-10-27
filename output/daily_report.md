# AutoNodes 每日报告

生成时间：2026-10-27 08:03:31

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 13/0 |
| 清理建议：优先/观察 | 1/93 |
| 原始节点数 | 96374 |
| 去重后节点数 | 26563 |
| TCP 可达数 | 3000 |
| 真测通过数 | 113 |
| verified 输出数 | 113 |
| global 输出数 | 116 |
| all 输出数 | 26563 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 23.3 |
| fetch | 7.3 |
| generate | 13.0 |
| geo | 1.5 |
| probe | 103.3 |
| real_test | 78.8 |
| tcp | 79.8 |
| write_verified | 0.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 89 | 75 | 14 | 84.3% |
| hysteria2 | 11 | 10 | 1 | 90.9% |
| shadowsocks | 88 | 33 | 55 | 37.5% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 72 | 55 | 17 | 76.4% |
| vless | 278 | 145 | 133 | 52.2% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:status | 68 |
| test_one_timeout:15.0s | 60 |
| geo:status | 34 |
| speed:ClientOSError | 33 |
| 204:ProxyError | 10 |
| 204:ClientOSError | 6 |
| 204:TimeoutError | 4 |
| cn-block:TimeoutError | 3 |
| geo:ClientOSError | 1 |
| geo:ProxyError | 1 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6393 |
| ConnectionRefusedError | 1096 |
| gaierror | 284 |
| OSError | 239 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.852 | prefer | 91 | 0.835 | 603 |
| Au1rxx-base64 | 0.623 | observe | 357 | 0.555 | 1722 |
| mheidari-all | 0.611 | observe | 79 | 0.532 | 24516 |
| Surfboard-tg-mixed | 0.286 | observe | 13 | 0.231 | 7021 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4988 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 3004 |
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
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 457 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 348 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 343 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 226 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 204 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 203 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 195 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 173 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 168 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 92 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.231 | 3 | 10 | 13 |
| mheidari-all | 0.532 | 42 | 37 | 79 |
| Au1rxx-base64 | 0.555 | 198 | 159 | 357 |
| ermaozi | 0.835 | 76 | 15 | 91 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24516 | yes | 6.33 | 0 |
| SoliSpirit-all | 10295 | yes | 4.28 | 0 |
| Epodonios-all | 7509 | yes | 1.07 | 0 |
| Surfboard-tg-mixed | 7021 | yes | 3.59 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.34 | 0 |
| barry-far-vless | 5620 | yes | 3.23 | 0 |
| Surfboard-tg-vless | 5284 | yes | 4.53 | 0 |
| 10ium-ScrapeCategorize-Vless | 4988 | yes | 3.46 | 0 |
| mahdibland-V2RayAggregator | 4573 | yes | 3.66 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 3.03 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 104 |
| test_one_timeout | 60 |
| speed | 33 |
| 204 | 20 |
| cn-block | 4 |
