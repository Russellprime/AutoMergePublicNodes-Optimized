# AutoNodes 每日报告

生成时间：2026-10-27 11:29:28

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 13/0 |
| 清理建议：优先/观察 | 1/93 |
| 原始节点数 | 96332 |
| 去重后节点数 | 26667 |
| TCP 可达数 | 3000 |
| 真测通过数 | 143 |
| verified 输出数 | 143 |
| global 输出数 | 148 |
| all 输出数 | 26667 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 29.7 |
| fetch | 7.7 |
| generate | 13.6 |
| geo | 1.5 |
| probe | 106.1 |
| real_test | 91.7 |
| tcp | 85.5 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 88 | 73 | 15 | 83.0% |
| hysteria2 | 10 | 9 | 1 | 90.0% |
| shadowsocks | 139 | 39 | 100 | 28.1% |
| socks | 3 | 0 | 3 | 0.0% |
| trojan | 99 | 80 | 19 | 80.8% |
| vless | 434 | 175 | 259 | 40.3% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:status | 97 |
| speed:ClientOSError | 90 |
| geo:status | 84 |
| test_one_timeout:15.0s | 84 |
| 204:TimeoutError | 8 |
| 204:ProxyError | 7 |
| geo:ProxyError | 7 |
| 204:ClientOSError | 6 |
| cn-block:TimeoutError | 5 |
| geo:TimeoutError | 3 |
| geo:ClientOSError | 2 |
| cn-block:ProxyError | 2 |
| speed:ProxyError | 1 |
| cn-block:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6810 |
| ConnectionRefusedError | 1057 |
| OSError | 236 |
| gaierror | 149 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.828 | prefer | 90 | 0.811 | 603 |
| mheidari-all | 0.568 | observe | 8 | 0.875 | 24516 |
| Au1rxx-base64 | 0.56 | observe | 321 | 0.489 | 1774 |
| DeltaKronecker-all | 0.5 | observe | 236 | 0.419 | 3052 |
| Surfboard-tg-mixed | 0.425 | observe | 117 | 0.342 | 7021 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 52 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4988 |
| Epodonios-all | 0.255 | observe | 0 | None | 7509 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10244 |

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
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 459 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 350 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 345 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 228 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 206 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 205 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 197 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 175 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 170 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 94 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.342 | 40 | 77 | 117 |
| DeltaKronecker-all | 0.419 | 99 | 137 | 236 |
| Au1rxx-base64 | 0.489 | 157 | 164 | 321 |
| ermaozi | 0.811 | 73 | 17 | 90 |
| mheidari-all | 0.875 | 7 | 1 | 8 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24516 | yes | 6.45 | 0 |
| SoliSpirit-all | 10244 | yes | 1.9 | 0 |
| Epodonios-all | 7509 | yes | 3.55 | 0 |
| Surfboard-tg-mixed | 7021 | yes | 4.63 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.2 | 0 |
| barry-far-vless | 5497 | yes | 1.55 | 0 |
| Surfboard-tg-vless | 5284 | yes | 4.89 | 0 |
| 10ium-ScrapeCategorize-Vless | 4988 | yes | 1.31 | 0 |
| mahdibland-V2RayAggregator | 4573 | yes | 2.6 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 2.47 | 0 |

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
| geo | 193 |
| speed | 91 |
| test_one_timeout | 84 |
| 204 | 21 |
| cn-block | 8 |
