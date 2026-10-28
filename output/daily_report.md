# AutoNodes 每日报告

生成时间：2026-10-28 12:02:04

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 2/91 |
| 原始节点数 | 97827 |
| 去重后节点数 | 26591 |
| TCP 可达数 | 3000 |
| 真测通过数 | 100 |
| verified 输出数 | 100 |
| global 输出数 | 104 |
| all 输出数 | 26591 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 27.2 |
| fetch | 4.4 |
| generate | 8.4 |
| geo | 1.6 |
| probe | 90.5 |
| real_test | 88.7 |
| tcp | 84.2 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 91 | 79 | 12 | 86.8% |
| hysteria2 | 11 | 7 | 4 | 63.6% |
| shadowsocks | 116 | 30 | 86 | 25.9% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 76 | 45 | 31 | 59.2% |
| vless | 309 | 142 | 167 | 46.0% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 85 |
| geo:status | 79 |
| geo:status | 50 |
| 204:TimeoutError | 19 |
| speed:ClientOSError | 16 |
| 204:ProxyError | 15 |
| 204:ClientOSError | 10 |
| cn-block:TimeoutError | 9 |
| cn-block:ClientOSError | 5 |
| geo:ClientOSError | 4 |
| cn-block:ProxyError | 4 |
| geo:ProxyError | 3 |
| speed:TimeoutError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6724 |
| ConnectionRefusedError | 1084 |
| OSError | 239 |
| gaierror | 161 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi-get_subscribe | 0.861 | prefer | 74 | 0.851 | 467 |
| zhangkai | 0.785 | prefer | 19 | 0.842 | 43 |
| Au1rxx-base64 | 0.578 | observe | 286 | 0.507 | 1769 |
| DeltaKronecker-all | 0.463 | observe | 118 | 0.381 | 2801 |
| mheidari-all | 0.421 | observe | 6 | 0.667 | 24702 |
| Surfboard-tg-mixed | 0.37 | observe | 98 | 0.286 | 7544 |
| ninja-vless | 0.279 | observe | 2 | 0.5 | 1791 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 50 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5004 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-we | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-nodefree | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-yudou66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 463 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 354 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 349 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 232 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 210 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 209 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 201 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 179 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 174 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 98 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.286 | 28 | 70 | 98 |
| DeltaKronecker-all | 0.381 | 45 | 73 | 118 |
| ninja-vless | 0.5 | 1 | 1 | 2 |
| Au1rxx-base64 | 0.507 | 145 | 141 | 286 |
| mheidari-all | 0.667 | 4 | 2 | 6 |
| zhangkai | 0.842 | 16 | 3 | 19 |
| ermaozi-get_subscribe | 0.851 | 63 | 11 | 74 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24702 | yes | 3.72 | 0 |
| SoliSpirit-all | 10602 | yes | 2.51 | 0 |
| Epodonios-all | 8035 | yes | 3.83 | 0 |
| Surfboard-tg-mixed | 7544 | yes | 2.96 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.08 | 0 |
| barry-far-vless | 5789 | yes | 1.4 | 0 |
| Surfboard-tg-vless | 5575 | yes | 2.33 | 0 |
| 10ium-ScrapeCategorize-Vless | 5004 | yes | 1.29 | 0 |
| mahdibland-V2RayAggregator | 4500 | yes | 1.87 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.62 | 0 |

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
| geo | 136 |
| test_one_timeout | 85 |
| 204 | 44 |
| cn-block | 18 |
| speed | 18 |
