# MEMORY.md - 长期记忆

每次醒来都会读这个文件。惜字如金，只留真正重要的。

## 记忆系统架构
- **memory-core**（OpenClaw 2026.5.20 内置核心，enabled）— 短时 dreaming + 文件级记忆
- 可选后端：**@openclaw/memory-lancedb**（官方插件，未装；minHostVersion >=2026.4.10；LanceDB 向量库 + auto-recall/capture；darwin-x64 不支持）
- **MEMORY.md + daily.md**（长期文件记忆）
- **.dreams/** — dreaming 语料存储
- 备注：早期记忆里"sqlite-vec"那条是过时的，2026.5.20 的 memory-core 实际不用 sqlite-vec
- **复查触发条件**（任一满足再考虑装 lancedb）：①Agent 数量 ≥ 5；②`memory/` 累计文件 > 100 个或单文件 > 50KB；③出现召回不准/想不起以前聊过啥的反馈；④LCM recall 链路成为瓶颈

## 全局插件/工具配置
- **SearXNG web_search**（2026-06-09 由 agent-orchestrator 配置并验证）
  - 插件：`@agentclaws/openclaw-searxng`
  - 配置：`plugins.entries.searxng.config.webSearch.baseUrl = http://127.0.0.1:8888`
  - 已加入 `plugins.allow`
  - 范围：全局生效，10 个 agent 共享同一 gateway config 都可用
  - 验证：`web_search` 返回带 "功能来自 searxng" 标识，约 7.8s
  - 注：未来全局插件/工具变更也记到这里

## Agent 花名册（HALEI 6/13 确认）

> 以后所有 agent / 飞书机器人都用中文名，agent_id 在内部通信用。

| agent_id | 名字 | 飞书 bot | IDENTITY emoji |
|----------|------|----------|----------------|
| main | KIIT（大总管） | kiit | 🪶 |
| agent-orchestrator | Agent 编排工程师 | —（无对外 bot） | 🔧 |
| tts | TK 选品大师 | tts | — |
| content | TK 内容专家 | content | 🎬 |
| koc | TK 达人运营 | koc | 🤝 |
| traffic | TK 投流专家 | traffic | 🚀 |
| ops | TK 运营助手 | ops | ✅ |
| director | TK 运营总监 | director | 📊 |
| finance | TK 财务助手 | finance | 💰 |
| review | TK 客服专家 | review | 💬 |

**口头称呼习惯**：
- 我自称 KIIT / 大总管
- agent-orchestrator → Agent 编排工程师
- 其他 8 个直接叫"TK 选品大师""TK 投流专家"等中文名，不说 agent_id

## 用户信息
- HALEI，时间 Asia/Shanghai
- 沟通风格：高效、直接
- 飞书已授权，OpenID: ou_f590c429b7ded95568bebca2f534efdb

## 已卸载/禁用的功能
- Capability Evolver — 已卸载，不再使用

## 学习计划
- coding plan 套餐：晚上可用来学习探索更多的技能帮助用户提高生产力

## 索引

> `memory/` 下的文件索引。新建文件时在此添加条目。需要详情时再读取对应文件。

- YYYY-MM-DD.md: 每日日志
- learnings/：自我改进日志
  - LEARNINGS.md: 教训和发现（纠正、知识盲区、最佳实践）
  - ERRORS.md: 操作失败和异常记录
  - FEATURE_REQUESTS.md: 用户请求的缺失能力

## Agent 架构

10 个 Agent + 大总管（详细表格见 SOUL.md 团队协作）：

- main (KIIT) — 大总管，**只做业务任务调度**；不直接改 agent 设置
- agent-orchestrator — **Agent 编排工程师**，管所有 agent 的 config/SOUL/MEMORY/cron/workspace/models/auth
- 8 个执行 Agent：tts / content / koc / traffic / ops / director / finance / review
- 铁规则：调整 agent 设置 → agent-orchestrator；业务任务 → main 调度 → 分发给执行 Agent
- 边界：main 可以读 agent 状态做诊断，但**修改动作交 agent-orchestrator**

## 编排模式

（验证过的有效协作模式。）

## 记忆

> 沉淀过的认知。决策、教训、重要偏好、关键上下文。memory/ 是笔记，这里是定稿。

## 指挥/通知优先级规则
- 当你让我「通知、指挥、调度」某个 Agent 时，**优先使用 `sessions_send` 内部通信**，不走飞书外部消息
- 内部通信不可用时，再降级到飞书消息 API
- 飞书消息仅用于：外部联系人、用户明确要求通过飞书传达的场景

## Promoted From Short-Term Memory (2026-07-08)

<!-- openclaw-memory-promotion:memory:memory/2026-07-04-director-tts-handoff.md:52:52 -->
- 【越南 #3】AISHG 三角心形爪夹: **决策建议：** 1688 货源 API 修复后第一时间验成本；如到货价 ≤¥2 可重评，否则弃。 [score=0.860 recalls=0 avg=0.620 source=memory/2026-07-04-director-tts-handoff.md:52-52]
<!-- openclaw-memory-promotion:memory:memory/2026-07-04-director-tts-handoff.md:58:61 -->
- 【越南 #4】TMR 包发夹（闷骚造型）: | 维度 | 评级 | 关键判断 | |------|------|----------| | 市场容量 | ⭐⭐⭐⭐⭐ 强 | 30天192单，**月销爆增 +405%**——4 个候选里唯一量级+趋势双优 | | 竞品态势 | ⭐⭐⭐⭐ 优 | 店铺分散，新进入者仍有红利窗口 | [score=0.860 recalls=0 avg=0.620 source=memory/2026-07-04-director-tts-handoff.md:58-61]
<!-- openclaw-memory-promotion:memory:memory/2026-07-04-director-tts-handoff.md:62:64 -->
- 【越南 #4】TMR 包发夹（闷骚造型）: | 差异化空间 | ⭐⭐⭐⭐ 优 | 闷骚风是越南本土审美，**自带文化适配**；颜色+套装组合可放大差异 | | 风险点 | 🟡 中 | +405% 增长含"低基数放大"成分（基数小，百分比容易虚高）；需看绝对增量是否健康 | | 推荐度 | ⭐⭐⭐⭐⭐ 5/5 | **首批主推款**——增长信号+市场容量+本土审美三位一体 | [score=0.860 recalls=0 avg=0.620 source=memory/2026-07-04-director-tts-handoff.md:62-64]
<!-- openclaw-memory-promotion:memory:memory/2026-07-04-director-tts-handoff.md:66:66 -->
- 【越南 #4】TMR 包发夹（闷骚造型）: **决策建议：** 越南站首批主推，权重最高。 [score=0.860 recalls=0 avg=0.620 source=memory/2026-07-04-director-tts-handoff.md:66-66]
<!-- openclaw-memory-promotion:memory:memory/2026-07-04-director-tts-handoff.md:67:69 -->
- 【越南 #4】TMR 包发夹（闷骚造型）: 抢窗口期：增长率 +405% 意味着对手也在涌入，越早进入越能卡位; 内容侧建议走"越南本土审美+套装组合"路线，避开纯价格战; 配套要求：1688 货源价（毛利验证）必须 7 月内出结果 [score=0.860 recalls=0 avg=0.620 source=memory/2026-07-04-director-tts-handoff.md:67-69]
<!-- openclaw-memory-promotion:memory:memory/2026-07-04-director-tts-handoff.md:75:78 -->
- 越南汇总：首批投放矩阵: | 优先级 | 候选 | 角色定位 | 行动 | |--------|------|----------|------| | 🥇 主推 | TMR 包发夹 | 抢窗口期的爆款候选 | 立即立项，跟进 1688 货源 | | 🥈 基础款 | Valley Limit 熊夹 | 养链接权重、稳单量 | 同步立项，走礼盒/IP 差异化 | [score=0.860 recalls=0 avg=0.620 source=memory/2026-07-04-director-tts-handoff.md:75-78]
<!-- openclaw-memory-promotion:memory:memory/2026-07-04-director-tts-handoff.md:79:80 -->
- 越南汇总：首批投放矩阵: | 👀 观察 | Satin 花卉顶髻 | 验证 14D 趋势 | 等下一轮数据，不急 | | ❌ 暂缓 | AISHG 三角心形 | 毛利天花板低 | 等 1688 数据，否则弃 | [score=0.860 recalls=0 avg=0.620 source=memory/2026-07-04-director-tts-handoff.md:79-80]
<!-- openclaw-memory-promotion:memory:memory/2026-07-04-director-tts-handoff.md:87:88 -->
- 现状: Sorftime TH API 类目过滤失效，返回的"候选"是口腔清洁片（Polident），**非发饰，不纳入评分**; 任何对泰国发饰的销量/增长率/竞品判断都**无可靠数据支撑** [score=0.860 recalls=0 avg=0.620 source=memory/2026-07-04-director-tts-handoff.md:87-88]
<!-- openclaw-memory-promotion:memory:memory/2026-07-04-director-tts-handoff.md:92:95 -->
- 建议（kiit 决策项）: | 路径 | 工作量 | 价值 | 建议度 | |------|--------|------|--------| | **A. 手动查 Shopee TH 发饰类目 Top100** | 1-2h | 高 | ⭐⭐⭐⭐⭐ 立即执行 | | **B. 修复 Sorftime TH 节点配置** | 未知，可能需要联系服务商 | 长期解 | ⭐⭐⭐ 中期推进 | [score=0.860 recalls=0 avg=0.620 source=memory/2026-07-04-director-tts-handoff.md:92-95]
<!-- openclaw-memory-promotion:memory:memory/2026-07-04-director-tts-handoff.md:96:96 -->
- 建议（kiit 决策项）: | **C. 用越南数据外推泰国** | 0h | 低（市场审美差异大） | ⭐ 不建议 | [score=0.860 recalls=0 avg=0.620 source=memory/2026-07-04-director-tts-handoff.md:96-96]

## Promoted From Short-Term Memory (2026-07-09)

<!-- openclaw-memory-promotion:memory:memory/2026-07-03.md:13:13 -->
- 我的理解: 失败保持 open 人工追 [score=0.871 recalls=0 avg=0.620 source=memory/2026-07-03.md:13-13]
<!-- openclaw-memory-promotion:memory:memory/2026-07-03.md:16:19 -->
- 待 HALEI 确认的 4 个问题: **飞书任务承接载体**：; A. 每个 agent 一个清单（推荐）; B. 一个总清单; C. 按业务域分 [score=0.871 recalls=0 avg=0.620 source=memory/2026-07-03.md:16-19]
<!-- openclaw-memory-promotion:memory:memory/2026-07-03.md:20:23 -->
- 待 HALEI 确认的 4 个问题: **同步机制**：; A. cron 末尾直接调飞书 API（改 cron 提示词）; B. main 每天汇总一次批量写（有延迟）; **范围**：只同步当前在跑的（推荐）/ 历史全部追溯 [score=0.871 recalls=0 avg=0.620 source=memory/2026-07-03.md:20-23]
<!-- openclaw-memory-promotion:memory:memory/2026-07-03.md:24:24 -->
- 待 HALEI 确认的 4 个问题: **勾选节奏**：实时勾 / 每日一次 [score=0.871 recalls=0 avg=0.620 source=memory/2026-07-03.md:24-24]
<!-- openclaw-memory-promotion:memory:memory/2026-07-03.md:27:30 -->
- 初步方案: 每 agent 一个清单：「[agent名] 每日任务」; 每个 cron job → 该 agent 清单下的 recurring 任务; cron 跑完 → 飞书 API 勾选 + 记录完成时间; 失败 → 不勾选，人工介入 [score=0.871 recalls=0 avg=0.620 source=memory/2026-07-03.md:27-30]
<!-- openclaw-memory-promotion:memory:memory/2026-07-03.md:34:36 -->
- 落地方向: 等 HALEI 拍板 4 个问题; 由 agent-orchestrator 出执行清单; main 不直接动 agent 配置（边界） [score=0.871 recalls=0 avg=0.620 source=memory/2026-07-03.md:34-36]
<!-- openclaw-memory-promotion:memory:memory/2026-07-03.md:5:6 -->
- 21:23 — HALEI 提的需求：停 cron 通知 + 飞书任务同步: **HALEI 原话**： > 你不要发cron job的通知给我了。是不是可以把这个任务同步也加入到飞书的任务中，执行一个勾选一个，我也可以通过任务来查看，让所有的agent 每天执行的cron job这些任务都能和飞书的任务同步是否可以好？ [score=0.871 recalls=0 avg=0.620 source=memory/2026-07-03.md:5-6]
<!-- openclaw-memory-promotion:memory:memory/2026-07-03.md:9:11 -->
- 我的理解: **停 cron 完成通知**（除非异常/failed）; **所有 agent 的每日 cron job 同步到飞书任务清单**：; 结构化、可勾选、可查看历史 [score=0.871 recalls=0 avg=0.620 source=memory/2026-07-03.md:9-11]
<!-- openclaw-memory-promotion:memory:memory/2026-07-03.md:31:31 -->
- 初步方案: 通知 → 仅 failed 时推送 [score=0.861 recalls=0 avg=0.620 source=memory/2026-07-03.md:31-31]
<!-- openclaw-memory-promotion:memory:memory/2026-07-03.md:39:39 -->
- 状态: ⏸️ 等待 HALEI 确认 4 个问题 [score=0.861 recalls=0 avg=0.620 source=memory/2026-07-03.md:39-39]

## Promoted From Short-Term Memory (2026-07-10)

<!-- openclaw-memory-promotion:memory:memory/2026-07-04-director-tts-handoff.md:98:98 -->
- 建议（kiit 决策项）: **执行建议：** A 路径由 director 或 tts 在 7/5 前完成，输出至少 5 个泰国发饰候选；B 路径走修复工单。 [score=0.810 recalls=0 avg=0.620 source=memory/2026-07-04-director-tts-handoff.md:98-98]
