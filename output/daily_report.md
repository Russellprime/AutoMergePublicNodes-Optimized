# AutoNodes 每日报告

生成时间：2026-10-28 03:34:42

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 4/89 |
| 原始节点数 | 97741 |
| 去重后节点数 | 26800 |
| TCP 可达数 | 3000 |
| 真测通过数 | 93 |
| verified 输出数 | 93 |
| global 输出数 | 95 |
| all 输出数 | 26800 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 31.7 |
| fetch | 7.3 |
| generate | 13.4 |
| geo | 1.7 |
| probe | 105.4 |
| real_test | 88.6 |
| tcp | 83.0 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 59 | 56 | 3 | 94.9% |
| hysteria2 | 15 | 13 | 2 | 86.7% |
| shadowsocks | 95 | 41 | 54 | 43.2% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 122 | 113 | 9 | 92.6% |
| vless | 407 | 200 | 207 | 49.1% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 113 |
| geo:status | 87 |
| speed:ClientOSError | 43 |
| 204:TimeoutError | 9 |
| geo:status | 9 |
| cn-block:ClientOSError | 6 |
| 204:ProxyError | 3 |
| cn-block:TimeoutError | 2 |
| geo:ClientOSError | 1 |
| 204:ClientOSError | 1 |
| speed:ProxyError | 1 |
| geo:TimeoutError | 1 |
| speed:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6611 |
| ConnectionRefusedError | 1073 |
| OSError | 236 |
| gaierror | 210 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi-get_subscribe | 0.93 | prefer | 43 | 0.93 | 467 |
| zhangkai | 0.809 | prefer | 17 | 0.941 | 43 |
| Surfboard-tg-mixed | 0.755 | prefer | 115 | 0.678 | 7522 |
| DeltaKronecker-all | 0.752 | prefer | 117 | 0.675 | 3052 |
| Au1rxx-base64 | 0.648 | observe | 338 | 0.58 | 1724 |
| mheidari-all | 0.299 | observe | 71 | 0.211 | 24790 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 52 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4988 |
| Epodonios-all | 0.255 | observe | 0 | None | 8008 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-we | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-nodefree | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-yudou66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 462 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 353 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 348 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 231 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 209 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 208 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 200 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 178 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 173 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 97 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mheidari-all | 0.211 | 15 | 56 | 71 |
| Au1rxx-base64 | 0.58 | 196 | 142 | 338 |
| DeltaKronecker-all | 0.675 | 79 | 38 | 117 |
| Surfboard-tg-mixed | 0.678 | 78 | 37 | 115 |
| ermaozi-get_subscribe | 0.93 | 40 | 3 | 43 |
| zhangkai | 0.941 | 16 | 1 | 17 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24790 | yes | 6.3 | 0 |
| SoliSpirit-all | 10429 | yes | 2.93 | 0 |
| Epodonios-all | 8008 | yes | 6.63 | 0 |
| Surfboard-tg-mixed | 7522 | yes | 4.2 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.05 | 0 |
| barry-far-vless | 5751 | yes | 1.06 | 0 |
| Surfboard-tg-vless | 5538 | yes | 4.4 | 0 |
| 10ium-ScrapeCategorize-Vless | 4988 | yes | 1.33 | 0 |
| mahdibland-V2RayAggregator | 4500 | yes | 3.25 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 0.86 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 113 |
| geo | 98 |
| speed | 45 |
| 204 | 13 |
| cn-block | 8 |
