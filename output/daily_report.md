# AutoNodes 每日报告

生成时间：2026-10-29 22:23:27

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 2/91 |
| 原始节点数 | 99308 |
| 去重后节点数 | 27784 |
| TCP 可达数 | 3000 |
| 真测通过数 | 104 |
| verified 输出数 | 104 |
| global 输出数 | 111 |
| all 输出数 | 27784 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 29.5 |
| fetch | 8.1 |
| generate | 14.4 |
| geo | 1.6 |
| probe | 100.2 |
| real_test | 73.7 |
| tcp | 83.0 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 22 | 17 | 5 | 77.3% |
| hysteria2 | 15 | 10 | 5 | 66.7% |
| shadowsocks | 95 | 15 | 80 | 15.8% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 160 | 111 | 49 | 69.4% |
| vless | 264 | 97 | 167 | 36.7% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:status | 135 |
| geo:status | 74 |
| test_one_timeout:15.0s | 48 |
| speed:ClientOSError | 17 |
| 204:ProxyError | 8 |
| 204:TimeoutError | 6 |
| cn-block:TimeoutError | 6 |
| 204:ClientOSError | 3 |
| geo:ClientOSError | 2 |
| cn-block:ClientOSError | 2 |
| cn-block:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound: start inbound/socks[socks-in]: listen tcp 127.0.0.1:37080: bind: address already in use | 1 |
| speed:ProxyError | 1 |
| geo:ProxyError | 1 |
| speed:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6604 |
| ConnectionRefusedError | 1115 |
| gaierror | 331 |
| OSError | 237 |
| SSRFBlocked | 4 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.836 | prefer | 39 | 0.769 | 7837 |
| ermaozi | 0.77 | prefer | 22 | 0.773 | 510 |
| mheidari-all | 0.547 | observe | 163 | 0.466 | 33474 |
| Au1rxx-base64 | 0.45 | observe | 331 | 0.381 | 1725 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5005 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 2709 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10379 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5821 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-we | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.025 | observe | 0 | None | 1 | 0 |
| Epodonios-all | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-nodefree | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-yudou66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-oneclickvpnkeys | 0.131 | observe | 1 | 0.0 | 0 | 97 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 7 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 468 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 359 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 354 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 237 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 215 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 214 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 206 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 184 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 179 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 103 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-oneclickvpnkeys | 0.0 | 0 | 1 | 1 |
| Au1rxx-base64 | 0.381 | 126 | 205 | 331 |
| mheidari-all | 0.466 | 76 | 87 | 163 |
| Surfboard-tg-mixed | 0.769 | 30 | 9 | 39 |
| ermaozi | 0.773 | 17 | 5 | 22 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 33474 | yes | 6.54 | 0 |
| SoliSpirit-all | 10379 | yes | 4.16 | 0 |
| Surfboard-tg-mixed | 7837 | yes | 4.77 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.26 | 0 |
| barry-far-vless | 6033 | yes | 2.21 | 0 |
| Surfboard-tg-vless | 5821 | yes | 3.69 | 0 |
| 10ium-ScrapeCategorize-Vless | 5005 | yes | 3.73 | 0 |
| mahdibland-V2RayAggregator | 4444 | yes | 1.39 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 2.54 | 0 |
| DeltaKronecker-all | 2709 | yes | 5.49 | 0 |

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
| geo | 212 |
| test_one_timeout | 48 |
| speed | 19 |
| 204 | 17 |
| cn-block | 10 |
| sing-box exited 1 | 1 |
