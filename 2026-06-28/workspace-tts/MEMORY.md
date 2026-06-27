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

## Promoted From Short-Term Memory (2026-06-14)

<!-- openclaw-memory-promotion:memory:memory/2026-06-09.md:6:9 -->
- SOP v7.0 重写: 彻底解决 v6.0 的致命问题：TikTok 没有批量扫描接口; 新核心：Shopee 验证热销（shopee_product_search，可多维筛选）→ TikTok 验证趋势（tiktok_similar_product）→ 1688 利润终选; 越南毛利率门槛从 70% 降至 40%（实测越南发饰售价低，45%固定成本导致70%毛利不可能）; 删除"带货视频≥8"条件（越南数据为空） [score=0.900 recalls=0 avg=0.620 source=memory/2026-06-09.md:6-9]
<!-- openclaw-memory-promotion:memory:memory/2026-06-09.md:56:57 -->
- SOP v7.0 修订要点（复盘后）: 写入前查重（按商品名称过滤，已存在则跳过）; SOP 文档：/home/halei/workspace-tts/docs/SOP-v7.0.md [score=0.868 recalls=0 avg=0.620 source=memory/2026-06-09.md:56-57]

## Promoted From Short-Term Memory (2026-06-18)

<!-- openclaw-memory-promotion:memory:memory/2026-06-12.md:11:12 -->
- 待跟进: 等待 HALEI 决策：是换类目（美妆工具/厨房/母婴/宠物）还是调整发饰策略; 累计13条候选全部C级，0条达标（S/A/B级=0） [score=0.895 recalls=0 avg=0.620 source=memory/2026-06-12.md:11-12]
<!-- openclaw-memory-promotion:memory:memory/2026-06-13.md:31:33 -->
- 待跟进: [ ] HALEI 确认潜力评分权重倾向（销量/增长率/TK信号各占多少）; [ ] TK/1688 API 排查修复; [ ] cron 重建（v8.0 模式：扫描→候选池→推送HALEI审核） [score=0.895 recalls=0 avg=0.620 source=memory/2026-06-13.md:31-33]
<!-- openclaw-memory-promotion:memory:memory/2026-06-10.md:12:12 -->
- 待跟进: 等 HALEI 拍板 v8.0 策略方向 [score=0.888 recalls=0 avg=0.620 source=memory/2026-06-10.md:12-12]
<!-- openclaw-memory-promotion:memory:memory/2026-06-11.md:11:12 -->
- 待跟进: v8.0 策略调整等待 HALEI 确认; SOP 需更新，移除发饰品类或放宽毛利门槛 [score=0.844 recalls=0 avg=0.620 source=memory/2026-06-11.md:11-12]
<!-- openclaw-memory-promotion:memory:memory/2026-06-11.md:4:4 -->
- 今日概要: cron v7.0 继续执行，0产出。HALEI 未上线，无新指令。 [score=0.844 recalls=0 avg=0.620 source=memory/2026-06-11.md:4-4]
<!-- openclaw-memory-promotion:memory:memory/2026-06-11.md:7:8 -->
- 执行记录: 越南 cron (6ee6a981)：触发，0候选通过; 泰国 cron (dde46f87)：触发，0候选通过 [score=0.844 recalls=0 avg=0.620 source=memory/2026-06-11.md:7-8]
<!-- openclaw-memory-promotion:memory:memory/2026-06-12.md:4:4 -->
- 今日概要: cron v7.0 继续执行，0产出。系统层面无变化。 [score=0.844 recalls=0 avg=0.620 source=memory/2026-06-12.md:4-4]
<!-- openclaw-memory-promotion:memory:memory/2026-06-12.md:7:8 -->
- 执行记录: 越南 cron (6ee6a981)：触发，0候选通过; 泰国 cron (dde46f87)：触发，0候选通过 [score=0.844 recalls=0 avg=0.620 source=memory/2026-06-12.md:7-8]
<!-- openclaw-memory-promotion:memory:memory/2026-06-13.md:16:19 -->
- 候选池 Top 产品（Shopee VN nodeId=11035861）: 三角形蟹夹（44558141228）：月销77/增长+381%/评分4.93/上架2月 → 潜力分90; 100支U型发夹（57157766901）：月销163/增长+57%/评分5.00/上架2.5月 → 潜力分90; Eleanor蝴蝶结发夹（40910456124）：月销93/增长+145%/评分4.84/上架11月 → 潜力分72; Eleanor花形发夹（40161968970）：月销190/增长+14%/评分4.95/上架10月 → 潜力分65 [score=0.844 recalls=0 avg=0.620 source=memory/2026-06-13.md:16-19]
<!-- openclaw-memory-promotion:memory:memory/2026-06-13.md:20:20 -->
- 候选池 Top 产品（Shopee VN nodeId=11035861）: Eleanor珍珠发夹（29930267866）：月销551/增长+38%/评分4.99/上架15月 → 潜力分68 [score=0.844 recalls=0 avg=0.620 source=memory/2026-06-13.md:20-20]

## Promoted From Short-Term Memory (2026-06-19)

<!-- openclaw-memory-promotion:memory:memory/2026-06-13.md:28:28 -->
- 文件更新: SOP v8.0：`/home/halei/workspace-tts/docs/SOP-v8.0.md` [score=0.906 recalls=0 avg=0.620 source=memory/2026-06-13.md:28-28]
<!-- openclaw-memory-promotion:memory:memory/2026-06-13.md:4:4 -->
- 今日概要: **重大策略调整日**。HALEI 明确：发饰是主营类目，不换；v8.0 动态潜力款模式确认。 [score=0.906 recalls=0 avg=0.620 source=memory/2026-06-13.md:4-4]
<!-- openclaw-memory-promotion:memory:memory/2026-06-13.md:23:25 -->
- API 问题: tiktok_similar_product：❌ 报错，无法验证 TK 同款; ali1688_similar_product：❌ 报错，无法查 1688 货源; 候选池仅用 Shopee 数据，TK/1688 验证待修复 [score=0.874 recalls=0 avg=0.620 source=memory/2026-06-13.md:23-25]
<!-- openclaw-memory-promotion:memory:memory/2026-06-13.md:9:12 -->
- v8.0 动态选品算法（确认）: **核心改变**：毛利从硬卡70% → ≥40%入选参考指标；价格底线 $3.0 → $1.5; **新增人工审核环节**：候选池结果发 HALEI 审，不直接写飞书; **利润靠后端实现**：拓品+组合套装+SKU改造+互补品搭配; **潜力评分模型**：月销量25%+增长率25%+TK验证20%+评分15%+上架时间15% [score=0.874 recalls=0 avg=0.620 source=memory/2026-06-13.md:9-12]
<!-- openclaw-memory-promotion:memory:memory/2026-06-10.md:4:4 -->
- 今日概要: cron v7.0 按计划执行，越南/泰国各跑一轮。v7.0 规则下（毛利≥70%硬卡）预计产出仍然为0。无新增决策。 [score=0.869 recalls=0 avg=0.620 source=memory/2026-06-10.md:4-4]
<!-- openclaw-memory-promotion:memory:memory/2026-06-10.md:7:9 -->
- 执行记录: 越南 cron (6ee6a981)：触发，未出有效候选; 泰国 cron (dde46f87)：触发，未出有效候选; 原因：v7.0 毛利率70%硬卡，越南发饰市场价位不支持 [score=0.837 recalls=0 avg=0.620 source=memory/2026-06-10.md:7-9]

## Promoted From Short-Term Memory (2026-06-28)

<!-- openclaw-memory-promotion:memory:memory/2026-06-25.md:14:15 -->
- 待办: [ ] 联系 HALEI 确认 Sorftime API key 存放位置; [ ] 修复后重新扫描泰国发饰候选池 [score=0.815 recalls=0 avg=0.620 source=memory/2026-06-25.md:14-15]
<!-- openclaw-memory-promotion:memory:memory/2026-06-25.md:4:4 -->
- 今日任务: TK选品-泰国黑马-v8.0（cron 触发） [score=0.815 recalls=0 avg=0.620 source=memory/2026-06-25.md:4-4]
