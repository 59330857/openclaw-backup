# TK选品 v7.0 — 越泰市场选品标准操作程序（修订版）

> 版本：7.0（修订，基于5/19-6/9 复盘）
> 市场：越南 VN / 泰国 TH
> 品类白名单：**美妆工具、厨房小件、母婴、宠物用品**（发饰品类已移除）
> 数据源：Shopee类目趋势 → Shopee热销 → TikTok验证 → 1688利润
> 输出终点：飞书多维表格

---

## 一、核心逻辑（修订版）

**旧逻辑（已废弃）：扫100个 →逐个过滤 → 结果全是C级 → 白耗配额**

**新逻辑（先看方向再动手）：**
1. `shopee_category_trend` → 找越南/泰国**哪些类目在涨**（增长率>0）
2. 锁定增长类目 → `shopee_product_search` → 扫具体产品
3. `tiktok_similar_product` → 验证 TK 上有同款
4. `ali1688_similar_product` → **毛利率≥70% 才写入**（≥$3.0 价格底线）
5. 飞书写入（含去重）
6. 汇报

---

## 二、铁律（5条，违反任何一条立即停止）

| # | 铁律 | 原因 |
|---|------|------|
| 1 | **毛利率必须 ≥70%**，不达标不入候选 | TK越泰平台扣40%+物流+仓储，70%是赚钱底线 |
| 2 | **价格底线 $3.0+**（不是 $1.5），折算本地货币后达标才扫 | $1.5 的品数学上不可能同时满足70%毛利 |
| 3 | **先看类目趋势，再扫产品**（执行顺序禁止倒置） | 方向错，扫越多越浪费配额 |
| 4 | **每次写入前查重**（按 product_id），已存在则跳过 | 6/7 同批写3次的 bug |
| 5 | **0产出也必须汇报**，不许闷头跑 | 闷头跑 = 浪费配额不反馈 |

---

## 三、先锋扫描：类目趋势判断（第0步）

**每次执行的第一步，先判断哪个类目在涨：**

### 3.1 越南类目扫描（3个候选类目）
```bash
# 美妆工具
curl -s -X POST "https://mcp.sorftime.com/" \
  -H "Authorization: Bearer $(cat /tmp/sorftime_key.txt)" \
  -H "accept: application/json, text/event-stream" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"shopee_product_search","arguments":{"site":"VN","monthSaleVolumeRangeMin":100,"priceRangeMin":50000,"page":1}},"id":1}'

# 厨房小件
curl -s -X POST "https://mcp.sorftime.com/" \
  -H "Authorization: Bearer $(cat /tmp/sorftime_key.txt)" \
  -H "accept: application/json, text/event-stream" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"shopee_product_search","arguments":{"site":"VN","monthSaleVolumeRangeMin":100,"priceRangeMin":50000,"page":1}},"id":2}'

# 母婴/宠物
curl -s -X POST "https://mcp.sorftime.com/" \
  -H "Authorization: Bearer $(cat /tmp/sorftime_key.txt)" \
  -H "accept: application/json, text/event-stream" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"shopee_product_search","arguments":{"site":"VN","monthSaleVolumeRangeMin":100,"priceRangeMin":50000,"page":1}},"id":3}'
```

**选择标准：找 MonthlySalesGrowth > 0 的类目（市场整体上行才有可能出黑马）**

---

## 四、选品标准（入场门槛）

### 4.1 Shopee 初筛

**通过条件（全部满足）：**
- 月销量 ≥ 50 单
- 7天销量 ≥ 月销量 × 15%
- 评分 ≥ 4.0
- 上架时间 ≤ 6个月
- 好评率 ≥ 90%

**价格底线（越南）：**
- ≥ 105,000 VND（≈$3.0，汇率3500）
- 泰国 ≥ 150 THB（≈$4.3）

**加分项（满足任一重点跟进）：**
- MonthlySalesGrowth ≥ 30%
- SalesCountOf7D ≥ 500

### 4.2 TikTok 趋势验证

用 `tiktok_similar_product` 搜 Shopee 标题关键词，验证 TK 上有同款在卖。

### 4.3 1688 利润终选

**毛利率公式：**
```
越南：毛利率 = 售价VND×55% - 1688价CNY×汇率 / 售价VND
泰国：毛利率 = 售价THB×52% - 1688价CNY×汇率5 / 售价THB
```

**通过条件：**
- 1688 采购价 ≤ ¥10（放宽了，原来≤¥5 筛选太严）
- **毛利率 ≥ 70%**（硬指标，不满足直接放弃）
- 能找到货源链接

### 4.4 推荐等级

| 等级 | 条件 | 行动 |
|------|------|------|
| **S级** | 毛利率≥70% + 7天销量≥500 + TK有同款 | 立即采购50-100件 |
| **A级** | 毛利率≥70% + 增长≥30% + TK有同款 | 正常采购30-50件 |
| **B级** | 毛利率≥70% + TK有同款 | 正常采购30-50件 |
| **C级** | 其他达标（毛利≥70%但无TK验证）| 观望 |
| **不跟进** | 毛利率<70% | 放弃 |

---

## 五、飞书多维表格写入规范

**目标表：** https://bytedance.feishu.cn/base/AKppbAeyXanToTsVl6ScxO5QnZd  
**Table ID：** tblHU2do30jzinJT

**写入前必须查重：**
```
调用 feishu_bitable_app_table_record action=list，过滤条件：
{field_name: "商品名称", operator: "is", value: ["产品名称"]}
```
如果记录已存在（任何等级），**跳过写入**，防止6/7 同批写3次的 bug。

**字段（20个全填）：**

| 字段名 | 类型 | 示例 |
|--------|------|------|
| 日期 | 毫秒时间戳 | 1749465600000 |
| 商品名称 | 文本 | 产品标题 |
| 站点 | 单选 | 越南 / 泰国 |
| 选品来源 | 多选数组 | ["Sorftime-TK数据"] |
| 采集状态 | 单选 | 已采集 |
| 三级类目 | 单选 |厨房小件 / 美妆工具 |
| 增长率 | 数字 | 35 |
| 月销量 | 数字 | 5000 |
| 售价（本地货币） | 数字 | 200000（VND）/ 200（THB） |
| 利润率(%) | 数字 | 72 |
| 预估利润 | 数字 | 计算值 |
| 1688价格(CNY) | 数字 | 8.5 |
| 1688同款链接 | 超链接 | https://detail.1688.com/offer/... |
| 1688产品主图 | 超链接 | https://cbu01.alicdn.com/... |
| 产品连接 | 超链接 | Shopee商品链接 |
| 推荐等级 | 单选 | S级/A级/B级/C级 |
| IP风险 | 单选 | 无 |
| 行动建议 | 单选 | 立即采购首单50-100件 |

---

## 六、毛利率参考对照表（快速判断）

| 售价 | 越南固定成本45% | 1688价¥3 | 1688价¥5 | 1688价¥8 | 1688价¥10 |
|------|----------------|---------|---------|---------|---------|
| $2.0 | $0.90 | 55% | 45% | 35% | 25% |
| $3.0 | $1.35 | 72% | 66% | 60% | 54% |
| $4.0 | $1.80 | 78% | 74% | 70% | 66% |
| $5.0 | $2.25 | 82% | 79% | 76% | 73% |

**结论：$3.0 以上 + 1688≤¥8 才能稳过70%红线。**

---

## 七、已知问题与限制

1. **越南 TK带货视频数据为空**：不用视频数作为筛选条件
2. **API 连续调用报 Auth**：等3秒重试，建议用 curl
3. **Cron payload 不能太长**：超过模型上下文会报 overflow，当前消息控制在500字以内
4. **发饰品类已移除**：越南发饰数学上不可能同时满足 $1.5+70% 毛利，不纳入扫描

---

## 八、Cron 配置

**当前状态：两个 cron 均已暂停（6/9），等 HALEI 拍板后重建。**

重建时 payload 消息必须精简（≤500字），不附代码示例，只写关键参数和判断标准。

---

## 九、执行自检清单（每次执行前过一遍）

- [ ] 价格底线：越南≥105,000 VND / 泰国≥150 THB
- [ ] 毛利率门槛：≥70%（硬指标，不满足直接放弃）
- [ ] 增长率>0（市场要是上行的，不是下行的）
- [ ] 写入前查重（已存在的 product_id 跳过）
- [ ] 0产出也汇报（不允许闷头跑）
- [ ] 每次执行汇报：扫描数量 / 通过数量 / 等级分布 / 配额消耗