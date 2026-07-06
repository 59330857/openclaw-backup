# MEMORY.md - 选品专家长期记忆

## 业务定位
专注 **TikTok Shop 东南亚发饰选品**，主力市场 **越南（VN）为主，泰国（TH）为辅**，主营品类：发夹、发箍、发圈、头绳、抓夹、发簪。

## 核心理念（亚声精铺模式）
- 重选品、轻运营
- 少而精，每月 5-10 款
- 综合评分 ≥80 才上架
- 数据驱动，避免主观判断

## ⭐ 三大核心打法

### 1. 变体堆叠（评论共享）
发饰天然适合：颜色5-10色、规格3+种、套装2+形式
→ 5个颜色变体只算一个链接，评论全部累计

### 2. 季节性+节日性
- 旺季同一起跑线，不拼老链接权重
- 越南节日：春节(1-2月)、情人节(2月)、妇女节(3月)、国庆(9.2)、圣诞(12月)
- 提前45-60天上架

### 3. 套装化高客单价
- 单件¥3-8 → 套装翻2-5倍
- 套装毛利率应≥40%

## 数据源
- **EchoTik**（echotik.live）：TikTok 商品销量/GMV/达人数据
- **1688**：供应链查价
- **Google Trends**：趋势验证

## 选品流程（v3.0 SOP）
1. EchoTik 新品榜/热销榜（TH+VN）
2. 变体/季节性/套装化初评估
3. 以图搜款找1688货源
4. 属性对比验证
5. 成本核算（越南平台费率41%+¥2）
6. 交叉验证（8维度矩阵，满分170）
7. 综合评分决策（≥130 S级）
8. 写入飞书 Bitable
9. 妙手ERP采集

## 否决项（直接放弃）
❌ 真实毛利率 < 20%
❌ 供应商评分 < 4.0
❌ Google Trends 下降>30%
❌ 品牌侵权
❌ 属性一致性差

## 越南成本模型（v3.0）
- 汇率：3570 VND/USD
- 平台费率：13%+5%+12%+1%+10% = 41% + ¥2固定
- 毛利要求：单件≥20%，套装≥40%

## 评分矩阵（满分170）
| 维度 | 分值 |
|------|------|
| 市场需求 | 25 |
| 竞争强度 | 25 |
| 利润空间 | 25 |
| 供应链稳定 | 15 |
| 合规风险 | 15 |
| 变体扩展潜力 | 25 |
| 季节性/节日性 | 25 |
| 套装化可行性 | 28 |

决策：≥130 S级 | 115-129 A级 | 100-114 B级 | <100 放弃

## 飞书 Bitable
- App Token：`AKppbAeyXanToTsVl6ScxO5QnZd`
- Table ID：`tblHU2do30jzinJT`

## Browser 控制
- 使用 `user` profile 连接 HALEI 的 Chrome
- 端口：9222（远程调试）
- 可通过 HTTP API 控制（需 Bearer token）

## Skill 状态
- ✅ `linkfox-echotik-product-search`：已安装
- ✅ `linkfox-echotik-new-product-rank`：新品榜
- `1688-product-search`：待配置 API Key

## Promoted From Short-Term Memory (2026-04-28)

<!-- openclaw-memory-promotion:memory:memory/2026-04-18.md:453:455 -->
- - Candidate: Possible Lasting Truths: ❌ 暂不推荐（不适用）: | cross-border-ecommerce-skill | 偏向市场准入/物流合规，非选品数据 | [confidence=0.58 evidence=memory/2026-04-10.md:32-32]; ❌ 暂不推荐（不适用）: | Skill | 原因 | |-------|------| | 1688-to-ozon | 针对OZON平台，不适合TikTok东南亚 | | taobao-shopping | 偏向购物决策辅助，非选品用途 | [confidence - confidence: 0.62 - evidence: memory/2026-04-17.md:461-463 [score=0.856 recalls=0 avg=0.620 source=memory/2026-04-18.md:23-25]
