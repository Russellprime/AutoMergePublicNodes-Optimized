# AutoNodes 每日报告

生成时间：2026-10-27 17:16:50

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 87/107 |
| 清理建议：禁用/降权 | 13/0 |
| 清理建议：优先/观察 | 1/93 |
| 原始节点数 | 96480 |
| 去重后节点数 | 26787 |
| TCP 可达数 | 3000 |
| 真测通过数 | 76 |
| verified 输出数 | 76 |
| global 输出数 | 80 |
| all 输出数 | 26787 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 20.5 |
| fetch | 8.2 |
| generate | 13.6 |
| geo | 1.3 |
| probe | 103.7 |
| real_test | 56.9 |
| tcp | 79.1 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 28 | 22 | 6 | 78.6% |
| hysteria2 | 14 | 9 | 5 | 64.3% |
| shadowsocks | 65 | 21 | 44 | 32.3% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 68 | 54 | 14 | 79.4% |
| vless | 230 | 76 | 154 | 33.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:status | 67 |
| speed:ClientOSError | 58 |
| geo:status | 46 |
| test_one_timeout:15.0s | 32 |
| 204:TimeoutError | 5 |
| 204:ProxyError | 4 |
| cn-block:ProxyError | 4 |
| cn-block:TimeoutError | 2 |
| cn-block:ClientOSError | 2 |
| 204:ClientOSError | 2 |
| geo:ClientOSError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6418 |
| ConnectionRefusedError | 1106 |
| gaierror | 303 |
| OSError | 241 |
| SSRFBlocked | 4 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.815 | prefer | 27 | 0.815 | 535 |
| mheidari-all | 0.58 | observe | 40 | 0.5 | 24511 |
| Au1rxx-base64 | 0.484 | observe | 317 | 0.413 | 1757 |
| Surfboard-tg-mixed | 0.446 | observe | 5 | 0.8 | 7059 |
| DeltaKronecker-all | 0.332 | observe | 14 | 0.286 | 3052 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 52 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4988 |
| Epodonios-all | 0.255 | observe | 0 | None | 7531 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10393 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-we | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-nodefree | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-yudou66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ArV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 460 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 351 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 346 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 229 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 207 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 206 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 198 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 176 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 171 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 95 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 1 | 1 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.286 | 4 | 10 | 14 |
| Au1rxx-base64 | 0.413 | 131 | 186 | 317 |
| mheidari-all | 0.5 | 20 | 20 | 40 |
| Surfboard-tg-mixed | 0.8 | 4 | 1 | 5 |
| ermaozi | 0.815 | 22 | 5 | 27 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24511 | yes | 5.8 | 0 |
| SoliSpirit-all | 10393 | yes | 4.85 | 0 |
| Epodonios-all | 7531 | yes | 6.1 | 0 |
| Surfboard-tg-mixed | 7059 | yes | 3.8 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.08 | 0 |
| barry-far-vless | 5532 | yes | 2.35 | 0 |
| Surfboard-tg-vless | 5319 | yes | 3.57 | 0 |
| 10ium-ScrapeCategorize-Vless | 4988 | yes | 3.31 | 0 |
| mahdibland-V2RayAggregator | 4573 | yes | 1.76 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 3.4 | 0 |

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
| geo | 115 |
| speed | 58 |
| test_one_timeout | 32 |
| 204 | 11 |
| cn-block | 8 |
