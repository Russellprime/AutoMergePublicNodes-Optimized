# AutoNodes 每日报告

生成时间：2026-10-30 03:59:36

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 86/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 2/91 |
| 原始节点数 | 99743 |
| 去重后节点数 | 27979 |
| TCP 可达数 | 3000 |
| 真测通过数 | 94 |
| verified 输出数 | 94 |
| global 输出数 | 101 |
| all 输出数 | 27979 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 28.3 |
| fetch | 6.2 |
| generate | 11.2 |
| geo | 1.5 |
| probe | 88.0 |
| real_test | 101.8 |
| tcp | 88.1 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 20 | 17 | 3 | 85.0% |
| hysteria2 | 14 | 12 | 2 | 85.7% |
| shadowsocks | 149 | 60 | 89 | 40.3% |
| trojan | 185 | 176 | 9 | 95.1% |
| vless | 359 | 140 | 219 | 39.0% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 106 |
| geo:status | 91 |
| speed:ClientOSError | 75 |
| geo:status | 18 |
| cn-block:ClientOSError | 8 |
| cn-block:TimeoutError | 5 |
| 204:TimeoutError | 5 |
| 204:ProxyError | 4 |
| cn-block:ProxyError | 4 |
| 204:ClientOSError | 3 |
| geo:ClientOSError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 7045 |
| ConnectionRefusedError | 1114 |
| OSError | 235 |
| gaierror | 215 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.839 | prefer | 20 | 0.85 | 515 |
| Au1rxx-base64 | 0.746 | prefer | 308 | 0.679 | 1722 |
| Surfboard-tg-mixed | 0.568 | observe | 166 | 0.488 | 7756 |
| mheidari-all | 0.499 | observe | 232 | 0.418 | 34034 |
| DeltaKronecker-all | 0.335 | observe | 1 | 1.0 | 2709 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5005 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10495 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5729 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-we | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.025 | observe | 0 | None | 1 | 0 |
| Epodonios-all | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-nodefree | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-yudou66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 469 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 360 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 355 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 238 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 216 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 215 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 207 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 185 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 180 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 104 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mheidari-all | 0.418 | 97 | 135 | 232 |
| Surfboard-tg-mixed | 0.488 | 81 | 85 | 166 |
| Au1rxx-base64 | 0.679 | 209 | 99 | 308 |
| ermaozi | 0.85 | 17 | 3 | 20 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| DeltaKronecker-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 34034 | yes | 5.33 | 0 |
| SoliSpirit-all | 10495 | yes | 3.23 | 0 |
| Surfboard-tg-mixed | 7756 | yes | 3.39 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.67 | 0 |
| barry-far-vless | 5941 | yes | 1.58 | 0 |
| Surfboard-tg-vless | 5729 | yes | 2.73 | 0 |
| 10ium-ScrapeCategorize-Vless | 5005 | yes | 1.84 | 0 |
| mahdibland-V2RayAggregator | 4444 | yes | 2.4 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.67 | 0 |
| DeltaKronecker-all | 2709 | yes | 5.35 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 112 |
| test_one_timeout | 106 |
| speed | 75 |
| cn-block | 17 |
| 204 | 12 |
