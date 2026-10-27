# AutoNodes 每日报告

生成时间：2026-10-27 21:46:12

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 13/0 |
| 清理建议：优先/观察 | 2/92 |
| 原始节点数 | 96134 |
| 去重后节点数 | 26669 |
| TCP 可达数 | 3000 |
| 真测通过数 | 87 |
| verified 输出数 | 87 |
| global 输出数 | 88 |
| all 输出数 | 26669 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 36.3 |
| fetch | 7.4 |
| generate | 13.8 |
| geo | 1.5 |
| probe | 102.2 |
| real_test | 58.8 |
| tcp | 83.1 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 28 | 22 | 6 | 78.6% |
| hysteria2 | 11 | 9 | 2 | 81.8% |
| shadowsocks | 97 | 20 | 77 | 20.6% |
| trojan | 97 | 74 | 23 | 76.3% |
| vless | 191 | 78 | 113 | 40.8% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:status | 94 |
| geo:status | 75 |
| test_one_timeout:15.0s | 31 |
| speed:ClientOSError | 5 |
| 204:ClientOSError | 3 |
| geo:ProxyError | 2 |
| geo:TimeoutError | 2 |
| 204:ProxyError | 2 |
| cn-block:ProxyError | 2 |
| 204:TimeoutError | 2 |
| cn-block:TimeoutError | 2 |
| geo:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6526 |
| ConnectionRefusedError | 1073 |
| gaierror | 254 |
| OSError | 238 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.88 | prefer | 23 | 0.826 | 3052 |
| ermaozi | 0.788 | prefer | 28 | 0.786 | 535 |
| Au1rxx-base64 | 0.525 | observe | 279 | 0.455 | 1730 |
| Surfboard-tg-mixed | 0.503 | observe | 24 | 0.417 | 7059 |
| mheidari-all | 0.441 | observe | 70 | 0.357 | 24397 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 52 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4988 |
| Epodonios-all | 0.255 | observe | 0 | None | 7530 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10257 |

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
| Pawdroid | 0.175 | observe | 0 | None | 0 | 8 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 461 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 352 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 347 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 230 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 208 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 207 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 199 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 177 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 172 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 96 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mheidari-all | 0.357 | 25 | 45 | 70 |
| Surfboard-tg-mixed | 0.417 | 10 | 14 | 24 |
| Au1rxx-base64 | 0.455 | 127 | 152 | 279 |
| ermaozi | 0.786 | 22 | 6 | 28 |
| DeltaKronecker-all | 0.826 | 19 | 4 | 23 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24397 | yes | 5.03 | 0 |
| SoliSpirit-all | 10257 | yes | 2.37 | 0 |
| Epodonios-all | 7530 | yes | 6.38 | 0 |
| Surfboard-tg-mixed | 7059 | yes | 3.72 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.16 | 0 |
| barry-far-vless | 5531 | yes | 0.96 | 0 |
| Surfboard-tg-vless | 5319 | yes | 3.49 | 0 |
| 10ium-ScrapeCategorize-Vless | 4988 | yes | 1.19 | 0 |
| mahdibland-V2RayAggregator | 4500 | yes | 3.09 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.31 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 174 |
| test_one_timeout | 31 |
| 204 | 7 |
| speed | 5 |
| cn-block | 4 |
