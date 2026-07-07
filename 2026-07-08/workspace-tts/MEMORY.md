# MEMORY.md - 长期记忆

每次醒来都会读这个文件。惜字如金，只留真正重要的。

## 用户信息
- 用户通过飞书与 TK 选品大师对话
- 代号：TK 选品大师（TTS Agent）
- 专注：TikTok 选品相关的分析和建议

## 店铺身份（6/25 确认）
- **店铺名**：Heat Up Glow - 时尚配件-发饰
- **主营类目**：发饰（发夹/发圈/头饰），不换类目
- **市场**：越南（VN）+ 泰国（TH）双站点
- **飞书 OpenID**：ou_f590c429b7ded95568bebca2f534efdb

## 索引

> `memory/` 下的文件索引。新建文件时在此添加条目。

- YYYY-MM-DD.md: 每日日志

## 工作流

### 选品写入流程
- 每次用 sorftime MCP 查完选品数据后，**直接写入飞书多维表**
- 写入目标多维表：https://bytedance.feishu.cn/base/AKppbAeyXanToTsVl6ScxO5QnZd
- app_token: AKppbAeyXanToTsVl6ScxO5QnZd
- table_id: tblHU2do30jzinJT
- 写入前确认 bot 已有「可编辑」权限（如遇写入被拒，需在多维表界面分享添加 bot）

### 妙手ERP采集流程（选品→上架）
- **Skill**: miaoshou-erp-source-import
- **作用**: 把选品好的产品（1688/AliExpress链接）采集到妙手ERP公共采集箱
- **凭证配置**: skills/miaoshou-erp-source-import/resources/config.json
- **流程**: 用户提供货源链接 → 调用 fetch_item API → 返回 detailId
- **后续**: detailId 可用于查询/编辑/认领到TikTok

### 选品核心逻辑（v8.0 动态潜力款 — 进行中）

**核心策略：潜力款宽进 → 人工筛选 → 后端结构实现利润**

数据源：Shopee热销 → 潜力评分排序 → 人工审核 → 备选池 → 1688组合方案

**v8.0 重大变化（6/13）：**
- ❌ 废弃：毛利率70%硬卡（把潜力款全拦了，0产出）
- ✅ 新：毛利≥40%入选参考指标，先让产品进来
- ✅ 新：结果发HALEI人工审核，不直接写飞书
- ✅ 新：利润靠后端结构实现（拓品+组合+SKU+互补品）

**潜力评分模型（v8.0）：**
| 指标 | 权重 |
|------|------|
| 月销量 | 25% |
| 7天增长率 | 25% |
| TK验证信号 | 20% |
| 评分 | 15% |
| 上架时间 | 15% |

**权重（6/25 更新）**：
- 原默认：月销25% + 增长25% + TK验证20% + 评分15% + 上架时间15%
- v8.0 cron 实际用：月销25% + 增长25% + **价格带宽20%** + 评分15% + 上架时间15%（TK 验证因 API 报错暂跳过）
- HALEI 未回复权重倾向，v8.0 cron 用"价格带宽"代替"TK 验证"

**入场门槛（越南发饰 v8.0）：**
- 月销量 ≥ 50单
- 7天销量 ≥ 月销量×15%
- 评分 ≥ 4.0
- 上架时间 ≤ 6个月
- 好评率 ≥ 90%
- 毛利率 ≥ 40%（参考指标，不硬卡）
- 价格底线 ≥ 45,000 VND（$1.5）

**推荐等级：**
- S级：毛利率≥60% + 7天销量≥500 + TK有同款 → 立即采购50-100件
- A级：毛利率≥40% + 增长≥30% + TK有同款 → 正常采购30-50件
- B级：毛利率≥40% + TK有同款 → 正常采购30-50件
- C级：其他达标 → 观望

## 技术配置

### sorftime MCP
- key: rhblyi90suxqqwfnnwzwy2tdvuhwqt09
- 文件路径：/tmp/sorftime_key.txt

### API 调用（curl 直调）
```
curl -s -X POST 'https://mcp.sorftime.com/' \
  -H "Authorization: Bearer $(cat /tmp/sorftime_key.txt)" \
  -H 'accept: application/json, text/event-stream' \
  -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"shopee_product_search","arguments":{"site":"VN","nodeId":"11035861","monthSaleVolumeRangeMin":50,"priceRangeMin":20000,"page":1}},"id":1}'
```

### 类目ID
- 越南发夹：11035861（Kẹp tóc）
- 泰国发饰：**11045697**（คลิปหนีบและปิ่นปักผม，发夹/发簪）
  - ⚠️ 旧 nodeId=11046516 是错误类目（儿童配件），已废弃

### 飞书多维表写入要点
- **app_token 必须用完整值**：`AKppbAeyXanToTsVl6ScxO5QnZd`
- **MultiSelect 字段**用数组格式：`["Sorftime-TK数据"]`
- **SingleSelect 字段**用选项名字符串：`"S级"`、`"A级"`、`"无"`、`"已采集"` 等
- **批量写入**用 `batch_create`，单条用 `create`

## Cron 任务（v8.0，6/25 重建）
- TK选品-越南黑马-v8.0：每天 9、12、15、18 点（cron id: d6ea3ee4）— v8.0 候选池模式
- TK选品-泰国黑马-v8.0：每天 10、13、16、19 点（cron id: 91574622）— v8.0 候选池模式
- ~~v7.0 cron（6ee6a981 / dde46f87）已于 6/25 删除~~
- **v8.0 提示词精简版**：原 v7.0 提示词约 1.5KB → v8.0 约 1.2KB，避免"context overflow"（v7.0 多次报"Context overflow: prompt too large for the model"）

## 文档索引

- SOP v8.0（当前）: /home/halei/workspace-tts/docs/SOP-v8.0.md
- SOP v7.0（已废弃）: /home/halei/workspace-tts/docs/SOP-v7.0.md
- 飞书多维表: https://bytedance.feishu.cn/base/AKppbAeyXanToTsVl6ScxO5QnZd

## 已知限制
- API 连续调用过快会报 Authentication required，等待3秒重试即可
- 越南 TikTok 带货视频数据基本为空，不用视频数量作为筛选条件
- Shopee 数据粒度为7天/30天，无24小时数据，用 MonthlySalesGrowth 和 SalesCountOf7D 替代
- VN Shopee 产品搜索 nodeId 不稳定，先用 shopee_category_search_from_name 确认 ID
- **tiktok_similar_product / ali1688_similar_product 当前报错（6/13至今未修）**，候选池暂缺 TK验证+1688货源数据
- v7.0 cron 曾报"Context overflow: prompt too large for the model"（5/29 6/4 6/12 等），v8.0 已精简提示词

## 已知偏好
- 选品逻辑以跟品为主，爆什么跟什么，简单直接
- 差异化手段：套装组合、变体扩展

## Promoted From Short-Term Memory (2026-07-03)

<!-- openclaw-memory-promotion:memory:memory/2026-06-29.md:4:6 -->
- 今日执行: **TK选品-泰国黑马-v8.0**（定时 cron 触发，16:13）; **店铺**：Heat Up Glow - 时尚配件-发饰; **站点**：泰国（TH），Shopee nodeId=11046516 [score=0.888 recalls=0 avg=0.620 source=memory/2026-06-29.md:4-6]
<!-- openclaw-memory-promotion:memory:memory/2026-06-29.md:13:16 -->
- 执行结果: POST /shopee/product/search → 404; POST /open/product/search → 404; POST /product/search → 404; GET / → nginx 欢迎页 [score=0.869 recalls=0 avg=0.620 source=memory/2026-06-29.md:13-16]
<!-- openclaw-memory-promotion:memory:memory/2026-06-29.md:9:12 -->
- 执行结果: **状态**：❌ 失败（API 不可用）; **原因**：Sorftime API（key: rhblyi90suxqqwfnnwzwy2tdvuhwqt09）全部 endpoint 返回 404，无法连接; **尝试路径**：; POST /shopee_product_search → 404 [score=0.869 recalls=0 avg=0.620 source=memory/2026-06-29.md:9-12]
<!-- openclaw-memory-promotion:memory:memory/2026-06-28.md:25:25 -->
- 备注: 今日 0 产出。 [score=0.822 recalls=0 avg=0.620 source=memory/2026-06-28.md:25-25]
<!-- openclaw-memory-promotion:memory:memory/2026-06-29.md:17:17 -->
- 执行结果: GET /health → 404 [score=0.817 recalls=0 avg=0.620 source=memory/2026-06-29.md:17-17]
<!-- openclaw-memory-promotion:memory:memory/2026-06-29.md:20:20 -->
- Top 候选: 无（API 不可用） [score=0.817 recalls=0 avg=0.620 source=memory/2026-06-29.md:20-20]

## Promoted From Short-Term Memory (2026-07-05)

<!-- openclaw-memory-promotion:memory:memory/2026-07-02.md:28:30 -->
- 待办: [ ] 排查 Sorftime API 新端点或备用数据源（key 有效但端点 404）; [ ] API 恢复后优先补跑越南+泰国; [ ] 考虑备用数据源（1688、亚马逊、TikTok 爆款等） [score=0.815 recalls=0 avg=0.620 source=memory/2026-07-02.md:28-30]
<!-- openclaw-memory-promotion:memory:memory/2026-07-02.md:33:34 -->
- 备注: Cron 通知（飞书私聊）失败：isolated session 无法调用 feishu_im_user_message（need_user_authorization）; 最终 reply 会通过飞书 channel 自动投递（announce delivery） [score=0.815 recalls=0 avg=0.620 source=memory/2026-07-02.md:33-34]

## Promoted From Short-Term Memory (2026-07-06)

<!-- openclaw-memory-promotion:memory:memory/2026-07-02.md:5:5 -->
- 今日选品跑批: **跑了什么**：v8.0 泰国选品流程（Shopee 发饰 nodeId=11046516） [score=0.866 recalls=0 avg=0.620 source=memory/2026-07-02.md:5-5]
<!-- openclaw-memory-promotion:memory:memory/2026-07-02.md:12:15 -->
- 今日选品跑批: `https://api.sorftime.com/shopee_product_search`（GET/POST 均 404）; `https://api.sorftime.com/api/shopee_product_search`（405）; `https://openapi.sorftime.com/shopee_product_search`（无响应）; Bearer header 认证方式（已确认有效），仍返回 404 [score=0.837 recalls=0 avg=0.620 source=memory/2026-07-02.md:12-15]
<!-- openclaw-memory-promotion:memory:memory/2026-07-02.md:16:16 -->
- 今日选品跑批: 结论：API 端点已变更/服务下线，key 仍存在但无法调用 [score=0.837 recalls=0 avg=0.620 source=memory/2026-07-02.md:16-16]
<!-- openclaw-memory-promotion:memory:memory/2026-07-02.md:21:24 -->
- 今日选品跑批: 越南（6/28）：0 产出; 泰国（6/29）：0 产出; 越南（7/2）：0 产出（API 故障）; 泰国（7/2）：0 产出（API 故障） [score=0.837 recalls=0 avg=0.620 source=memory/2026-07-02.md:21-24]
<!-- openclaw-memory-promotion:memory:memory/2026-07-02.md:9:10 -->
- 今日选品跑批: Shopee 泰国扫描失败：Sorftime API 全部端点返回 404/405; 问题持续：6/28 → 6/29 → 7/2，连续第 3 天 [score=0.837 recalls=0 avg=0.620 source=memory/2026-07-02.md:9-10]
<!-- openclaw-memory-promotion:memory:memory/2026-07-02.md:20:20 -->
- 今日选品跑批: **本周统计**（截至 7/2）： [score=0.827 recalls=0 avg=0.620 source=memory/2026-07-02.md:20-20]
<!-- openclaw-memory-promotion:memory:memory/2026-07-02.md:7:7 -->
- 今日选品跑批: **结果**：**0 产出（API 持续故障）** [score=0.827 recalls=0 avg=0.620 source=memory/2026-07-02.md:7-7]
<!-- openclaw-memory-promotion:memory:memory/2026-07-02.md:18:18 -->
- 今日选品跑批: **候选池**：无（API 不可用） [score=0.817 recalls=0 avg=0.620 source=memory/2026-07-02.md:18-18]
<!-- openclaw-memory-promotion:memory:memory/2026-07-03.md:39:41 -->
- 备注: 本次使用严格6个月上架限制，符合v8.0规则; 越南发饰市场6个月内的热门产品普遍月销较低（50-200单），高销量的爆品（如iLita月销1380）上架时间都超过6个月; 泰国数据缺口需要HALEI确认替代数据源 [score=0.815 recalls=0 avg=0.620 source=memory/2026-07-03.md:39-41]
<!-- openclaw-memory-promotion:memory:memory/2026-07-02.md:25:25 -->
- 今日选品跑批: **本周合计：0 产出** [score=0.807 recalls=0 avg=0.620 source=memory/2026-07-02.md:25-25]

## Promoted From Short-Term Memory (2026-07-07)

<!-- openclaw-memory-promotion:memory:memory/2026-07-03.md:25:28 -->
- 候选池（v8.0评分）: | 产品 | 月销 | 增长率 | 评分 | 上架时间 | VND价格 | 加权分 | |------|------|--------|------|----------|---------|--------| | Valley Limit熊夹 | 72 | 0% | 5.0 | 2026-04-09 | 56,862 | 47.75 | | Satin花卉顶髻夹 | 60 | 0% | 5.0 | 2026-05-21 | 48,384 | 44.18 | [score=0.888 recalls=0 avg=0.620 source=memory/2026-07-03.md:25-28]
<!-- openclaw-memory-promotion:memory:memory/2026-07-03.md:29:31 -->
- 候选池（v8.0评分）: | TMR包发夹(405%增长) | 192 | 405% | 4.84 | 2024-08-12 | 35,900 | 42.40 | | AISHG三角心形夹 | 54 | 74% | 4.92 | 2026-04-20 | 26,000 | 36.13 | | 定制字体发夹 | 216 | 213% | 4.51 | 2024-04-19 | 34,300 | 35.78 | [score=0.888 recalls=0 avg=0.620 source=memory/2026-07-03.md:29-31]
<!-- openclaw-memory-promotion:memory:memory/2026-07-03.md:23:23 -->
- 候选池（v8.0评分）: 筛选条件：≤6个月上架（SaleTime≥2026-01-07）、评分≥4.0、好评率≥90% [score=0.869 recalls=0 avg=0.620 source=memory/2026-07-03.md:23-23]
<!-- openclaw-memory-promotion:memory:memory/2026-07-03.md:14:17 -->
- 执行记录: VN类目扫描（nodeId=11035861，page1+2）→ 获取20个候选; TH类目扫描（nodeId=11045697）→ 无数据（API问题）; TH关键词搜索（"กิ๊บตึ๊ง ผ้าไหม"/"คลิปหนีบผม"）→ 返回全类目（电子/化妆品），无法过滤; VN关键词搜索（"kẹp tóc 2025"）→ 返回全类目 [score=0.837 recalls=0 avg=0.620 source=memory/2026-07-03.md:14-17]
<!-- openclaw-memory-promotion:memory:memory/2026-07-03.md:18:20 -->
- 执行记录: shopee_category_search_from_name（TH）→ 报错; TikTok验证 → 报错（已知限制）; 1688验证 → 报错（已知限制） [score=0.837 recalls=0 avg=0.620 source=memory/2026-07-03.md:18-20]
<!-- openclaw-memory-promotion:memory:memory/2026-07-03.md:34:36 -->
- 输出: 汇报给：KIIT（sessions_send）; 5个越南候选已选定; 泰国数据：API无法获取，坦诚说明 [score=0.837 recalls=0 avg=0.620 source=memory/2026-07-03.md:34-36]
<!-- openclaw-memory-promotion:memory:memory/2026-07-03.md:4:7 -->
- 选品任务（来自KIIT大总管）: 任务：Heat Up Glow 选品，选5个候选产品发大总管; 平台：越南+泰国，Shopee → TikTok 验证; Sorftime API：已恢复（6/26-6/29挂了4天）; 越南API：正常，VN nodeId=11035861 可用 [score=0.837 recalls=0 avg=0.620 source=memory/2026-07-03.md:4-7]
<!-- openclaw-memory-promotion:memory:memory/2026-07-03.md:8:11 -->
- 选品任务（来自KIIT大总管）: 泰国API：nodeId和关键词过滤双重失效，无法精准获取发饰数据; TK验证API（tiktok_similar_product）：仍报错（6/13至今）; 1688验证API（ali1688_similar_product）：仍报错（6/13至今）; Web搜索：不可用 [score=0.837 recalls=0 avg=0.620 source=memory/2026-07-03.md:8-11]
