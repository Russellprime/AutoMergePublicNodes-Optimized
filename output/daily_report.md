# AutoNodes 每日报告

生成时间：2026-10-28 22:10:51

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 1/92 |
| 原始节点数 | 99302 |
| 去重后节点数 | 27863 |
| TCP 可达数 | 3000 |
| 真测通过数 | 100 |
| verified 输出数 | 100 |
| global 输出数 | 102 |
| all 输出数 | 27863 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 30.8 |
| fetch | 6.9 |
| generate | 13.4 |
| geo | 1.7 |
| probe | 93.1 |
| real_test | 69.0 |
| tcp | 86.2 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 27 | 24 | 3 | 88.9% |
| hysteria2 | 10 | 7 | 3 | 70.0% |
| shadowsocks | 93 | 16 | 77 | 17.2% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 126 | 87 | 39 | 69.0% |
| vless | 264 | 103 | 161 | 39.0% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:status | 125 |
| geo:status | 73 |
| test_one_timeout:15.0s | 40 |
| speed:ClientOSError | 23 |
| 204:TimeoutError | 5 |
| 204:ClientOSError | 5 |
| cn-block:TimeoutError | 4 |
| cn-block:ProxyError | 3 |
| 204:ProxyError | 2 |
| geo:TimeoutError | 2 |
| geo:ClientOSError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6896 |
| ConnectionRefusedError | 1083 |
| gaierror | 307 |
| OSError | 239 |
| SSRFBlocked | 4 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.883 | prefer | 27 | 0.889 | 513 |
| mheidari-all | 0.642 | observe | 103 | 0.563 | 33849 |
| Surfboard-tg-mixed | 0.586 | observe | 85 | 0.506 | 7686 |
| Au1rxx-base64 | 0.436 | observe | 304 | 0.365 | 1755 |
| DeltaKronecker-all | 0.335 | observe | 1 | 1.0 | 2801 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5004 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10359 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5749 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-we | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.025 | observe | 0 | None | 1 | 0 |
| Epodonios-all | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-nodefree | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-yudou66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 465 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 356 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 351 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 234 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 212 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 211 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 203 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 181 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 176 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 100 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.365 | 111 | 193 | 304 |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.506 | 43 | 42 | 85 |
| mheidari-all | 0.563 | 58 | 45 | 103 |
| ermaozi | 0.889 | 24 | 3 | 27 |
| DeltaKronecker-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 33849 | yes | 6.03 | 0 |
| SoliSpirit-all | 10359 | yes | 2.94 | 0 |
| Surfboard-tg-mixed | 7686 | yes | 3.65 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.19 | 0 |
| barry-far-vless | 5963 | yes | 1.92 | 0 |
| Surfboard-tg-vless | 5749 | yes | 3.83 | 0 |
| 10ium-ScrapeCategorize-Vless | 5004 | yes | 2.11 | 0 |
| mahdibland-V2RayAggregator | 4323 | yes | 2.86 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 2.62 | 0 |
| DeltaKronecker-all | 2801 | yes | 6.13 | 0 |

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
| geo | 202 |
| test_one_timeout | 40 |
| speed | 23 |
| 204 | 12 |
| cn-block | 7 |
