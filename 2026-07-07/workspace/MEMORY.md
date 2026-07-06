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

## Promoted From Short-Term Memory (2026-07-02)

<!-- openclaw-memory-promotion:memory:memory/2026-06-29.md:29:30 -->
- 待 HALEI 决策: 这 2 个 skill 的归属由 HALEI 选定后，我再补一条 cron 或手工 upgrade; 升级脚本当前是 dumb，不能跨 owner 消歧；建议把 owner 写进 `lock.json` 的元数据里（需要修改 lockfile schema → 暂不动配置，等指令） [score=0.815 recalls=0 avg=0.620 source=memory/2026-06-29.md:29-30]
<!-- openclaw-memory-promotion:memory:memory/2026-06-29.md:33:34 -->
- 没动的 skill: 18 个非 lockfile skill：未尝试升级（clawhub 视角下不存在）; 不动 = 没动，跟「已是最新」是两种状态，不要混为一谈 [score=0.815 recalls=0 avg=0.620 source=memory/2026-06-29.md:33-34]
<!-- openclaw-memory-promotion:memory:memory/2026-06-29.md:5:5 -->
- 04:04 cron — 每日 skill 升级检查: **结果：本次 cron 未能完成自动升级。** [score=0.815 recalls=0 avg=0.620 source=memory/2026-06-29.md:5-5]

## Promoted From Short-Term Memory (2026-07-03)

<!-- openclaw-memory-promotion:memory:memory/2026-06-29.md:14:17 -->
- 失败明细: **context-engine**; 错误：`✖ Skill not found`; 含义：注册表已找不到该 slug（可能下架 / 重命名 / 私有）; 当前安装版本：2.1.1 [score=0.869 recalls=0 avg=0.620 source=memory/2026-06-29.md:14-17]
<!-- openclaw-memory-promotion:memory:memory/2026-06-29.md:20:23 -->
- 失败明细: **self-improving-agent**; 错误：`AMBIGUOUS_SKILL_SLUG`，注册表返回 3 个同名 slug：; `@pskoett/self-improving-agent`; `@kingaiwork/self-improving-agent` [score=0.869 recalls=0 avg=0.620 source=memory/2026-06-29.md:20-23]
<!-- openclaw-memory-promotion:memory:memory/2026-06-29.md:24:26 -->
- 失败明细: `@nguyenmanhdung-app/self-improving-agent`; 当前安装版本：3.0.24（lockfile 也没记录 owner，无法程序化判定）; 待办：需要 HALEI 确认要跟哪个 owner 的版本，再手工执行 `clawhub install @<owner>/self-improving-agent` [score=0.869 recalls=0 avg=0.620 source=memory/2026-06-29.md:24-26]
<!-- openclaw-memory-promotion:memory:memory/2026-06-29.md:18:18 -->
- 失败明细: 待办：去 clawhub.ai 搜索新 slug，或确认是否要换成新版本 [score=0.837 recalls=0 avg=0.620 source=memory/2026-06-29.md:18-18]
<!-- openclaw-memory-promotion:memory:memory/2026-06-29.md:8:10 -->
- 现状: `.clawhub/lock.json` 只追踪 2 个 skill：`context-engine 2.1.1` + `self-improving-agent 3.0.24`; `workspace/skills/` 下共 20 个 skill 文件夹，其余 18 个不在 clawhub lockfile 里（手工放置 / 不归 clawhub 管）; `clawhub update --all --no-input --force` 失败，触发单条流程也是失败 [score=0.837 recalls=0 avg=0.620 source=memory/2026-06-29.md:8-10]

## Promoted From Short-Term Memory (2026-07-06)

<!-- openclaw-memory-promotion:memory:memory/2026-07-04-director-tts-handoff.md:14:17 -->
- 【越南 #1】Valley Limit 熊形发夹: | 维度 | 评级 | 关键判断 | |------|------|----------| | 市场容量 | ⭐⭐⭐ 中 | 30天72单，稳定但非爆量（VN发饰月销天花板大致在100-200单/链接水平） | | 竞品态势 | ⭐⭐⭐⭐ 优 | Top3 居家占比低、店铺分散 → 尚未形成头部垄断，新进入者有缝隙 | [score=0.815 recalls=0 avg=0.620 source=memory/2026-07-04-director-tts-handoff.md:14-17]
<!-- openclaw-memory-promotion:memory:memory/2026-07-04-director-tts-handoff.md:18:20 -->
- 【越南 #1】Valley Limit 熊形发夹: | 差异化空间 | ⭐⭐⭐ 中 | 熊形公模，造型本身难差异化；可在颜色/包装/IP联名上做文章 | | 风险点 | 🟡 中 | 销量增长率 0%，属于"稳态款"非趋势款；如押注增长需另找爆点 | | 推荐度 | ⭐⭐⭐⭐ 4/5 | **可作为店铺基础款**——稳定单量+满分评分+TK易种草，适合养链接权重 | [score=0.815 recalls=0 avg=0.620 source=memory/2026-07-04-director-tts-handoff.md:18-20]
<!-- openclaw-memory-promotion:memory:memory/2026-07-04-director-tts-handoff.md:22:22 -->
- 【越南 #1】Valley Limit 熊形发夹: **决策建议：** 入选，但定位"打底款"而非"爆款"。第一批试投。 [score=0.815 recalls=0 avg=0.620 source=memory/2026-07-04-director-tts-handoff.md:22-22]

## Promoted From Short-Term Memory (2026-07-07)

<!-- openclaw-memory-promotion:memory:memory/2026-07-04-director-tts-handoff.md:23:24 -->
- 【越南 #1】Valley Limit 熊形发夹: 包装差异化（礼盒/IP联名）可拉升溢价; TK 视频数 API 修复后回补验证 [score=0.869 recalls=0 avg=0.620 source=memory/2026-07-04-director-tts-handoff.md:23-24]
<!-- openclaw-memory-promotion:memory:memory/2026-07-04-director-tts-handoff.md:34:36 -->
- 【越南 #2】Satin 花卉顶髻夹: | 差异化空间 | ⭐⭐⭐⭐ 优 | Satin+珍珠材质本身有质感门槛，包装+花型组合是天然差异化抓手 | | 风险点 | 🟡 中 | "爆量上新"也可能是补单后回落；需观察 7D→14D 衰减情况 | | 推荐度 | ⭐⭐⭐ 3/5 | **趋势候选，观察 14 天**——当前数据是机会信号但样本太短 | [score=0.869 recalls=0 avg=0.620 source=memory/2026-07-04-director-tts-handoff.md:34-36]
<!-- openclaw-memory-promotion:memory:memory/2026-07-04-director-tts-handoff.md:38:38 -->
- 【越南 #2】Satin 花卉顶髻夹: **决策建议：** 暂列入"观察池"，等 Sorftime 下一轮 14D 数据确认是否真正起势再决定。 [score=0.869 recalls=0 avg=0.620 source=memory/2026-07-04-director-tts-handoff.md:38-38]
<!-- openclaw-memory-promotion:memory:memory/2026-07-04-director-tts-handoff.md:104:107 -->
- 给 kiit 的交付摘要: **越南可立即执行：** TMR 包发夹（主推） + Valley Limit 熊夹（基础款） 两款立项; **观察池：** Satin 花卉顶髻等下一轮 14D 数据; **暂缓：** AISHG 三角心形（毛利未验证）; **泰国：** 暂无发饰评分结论，需走 Shopee 手动查询补齐 [score=0.837 recalls=0 avg=0.620 source=memory/2026-07-04-director-tts-handoff.md:104-107]
<!-- openclaw-memory-promotion:memory:memory/2026-07-04-director-tts-handoff.md:108:108 -->
- 给 kiit 的交付摘要: **卡点：** 1688 / TK 视频数 / 泰国发饰数据 三项 API 不可用 → 立项时必须标注"待数据补全后回评" [score=0.837 recalls=0 avg=0.620 source=memory/2026-07-04-director-tts-handoff.md:108-108]
<!-- openclaw-memory-promotion:memory:memory/2026-07-04-director-tts-handoff.md:112:112 -->
- 给 kiit 的交付摘要: **director 任务完成。** 结果回传 kiit 汇总。 [score=0.837 recalls=0 avg=0.620 source=memory/2026-07-04-director-tts-handoff.md:112-112]
<!-- openclaw-memory-promotion:memory:memory/2026-07-04-director-tts-handoff.md:30:33 -->
- 【越南 #2】Satin 花卉顶髻夹: | 维度 | 评级 | 关键判断 | |------|------|----------| | 市场容量 | ⭐⭐⭐ 中 | 30天60单，但 7D=60单 = 月销100% 全部发生在最近7天 → **爆量上新**信号 | | 竞品态势 | ⭐⭐ 弱 | ShopLoc=未知，无法判断集中度（**数据缺口**） | [score=0.837 recalls=0 avg=0.620 source=memory/2026-07-04-director-tts-handoff.md:30-33]
<!-- openclaw-memory-promotion:memory:memory/2026-07-04-director-tts-handoff.md:4:6 -->
- 输入盘点: tts 已交付越南 4 个候选 + 泰国 1 个非发饰参考; 数据缺口：TK 视频数 / 1688 货源 / 泰国发饰销量（3 项 API 不可用）; 越南数据完整，泰国仅"数据缺口说明 + 替代路径建议"，不强行打分 [score=0.837 recalls=0 avg=0.620 source=memory/2026-07-04-director-tts-handoff.md:4-6]
<!-- openclaw-memory-promotion:memory:memory/2026-07-04-director-tts-handoff.md:44:47 -->
- 【越南 #3】AISHG 三角心形爪夹: | 维度 | 评级 | 关键判断 | |------|------|----------| | 市场容量 | ⭐⭐ 弱 | 30天54单，销量基数低 | | 竞品态势 | ⭐⭐⭐⭐ 优 | 店铺较分散，无明显头部 | [score=0.837 recalls=0 avg=0.620 source=memory/2026-07-04-director-tts-handoff.md:44-47]
<!-- openclaw-memory-promotion:memory:memory/2026-07-04-director-tts-handoff.md:48:50 -->
- 【越南 #3】AISHG 三角心形爪夹: | 差异化空间 | ⭐⭐ 中 | 三角+心形几何组合较常见，造型公模化程度高，颜色差异化空间有限 | | 风险点 | 🔴 高 | 客单价 $1.01 接近 VN 均价下限，**利润空间薄**；+$0.3 成本波动即吃掉毛利 | | 推荐度 | ⭐⭐ 2/5 | **不建议首批**——毛利天花板太低，除非 1688 货源价能压到 ≤¥2 | [score=0.837 recalls=0 avg=0.620 source=memory/2026-07-04-director-tts-handoff.md:48-50]
