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

## Promoted From Short-Term Memory (2026-06-16)

<!-- openclaw-memory-promotion:memory:memory/2026-06-13.md:23:25 -->
- 根因: **memory 系统本身正常**——dreaming 链路（dreaming → ingest daily → 提升进 MEMORY）是有效的; **问题在写入环节**：tts 这个 agent 6/10-6/13 没主动写过一次 daily.md，dreaming 就没东西可提升; session 文件本身完整保存（轨迹 jsonl 在），但 tts 没在对话结束前触发"写记忆" [score=0.815 recalls=0 avg=0.620 source=memory/2026-06-13.md:23-25]
<!-- openclaw-memory-promotion:memory:memory/2026-06-13.md:33:34 -->
- 待 HALEI 拍板: 是否要我代补 tts 的 memory？; 是否要让 agent-orchestrator 去改 tts SOUL.md 加"每场结束写 daily"铁律？ [score=0.815 recalls=0 avg=0.620 source=memory/2026-06-13.md:33-34]
<!-- openclaw-memory-promotion:memory:memory/2026-06-13.md:9:12 -->
- 排查过程: 看 tts workspace: `/home/halei/workspace-tts/`; tts MEMORY.md mtime = 06-13 03:00（dreaming 自动跑的），但内容只到 06-09.md; tts `memory/` 下只有 5/16、5/19、6/7、6/9 四个 daily —— **6/10-6/13 完全没有 daily**; `memory/.dreams/daily-ingestion.json` 显示 dreaming 在 06-13 03:00 只 ingest 了 06-07.md 和 06-09.md —— 06-10/11/12 没 daily 可读 [score=0.815 recalls=0 avg=0.620 source=memory/2026-06-13.md:9-12]

## Promoted From Short-Term Memory (2026-06-18)

<!-- openclaw-memory-promotion:memory:memory/2026-06-13.md:13:16 -->
- 排查过程: tts 6/12 cron（v7.0 越南/泰国选品扫描）跑了，session 文件在 `/home/halei/.openclaw/agents/tts/sessions/`，但 tts 自己没写 daily; 最新一次 session `b6884754...`（12:32-13:16Z = 北京 20:32-21:16）：; 用户说 "选品，给我选利润款"; tts 问"经营什么类目" → 暴露"VN 发饰主营"被忘掉 [score=0.876 recalls=0 avg=0.620 source=memory/2026-06-13.md:13-16]
<!-- openclaw-memory-promotion:memory:memory/2026-06-13.md:17:20 -->
- 排查过程: 用户吐槽记忆系统; 用户提出新策略：**SOP v8.0 动态选品算法**（潜力款宽进 + 人工初筛 + 后端拓品/组合/SKU/互补）; tts 输出完整 v8.0 草案，问"权重倾向" → 对话停在这里; **tts 没把这场对话的关键结论（v8.0 框架、VN 发饰主营）写入 memory** [score=0.876 recalls=0 avg=0.620 source=memory/2026-06-13.md:17-20]
<!-- openclaw-memory-promotion:memory:memory/2026-06-13.md:6:6 -->
- 现象: HALEI 反馈 "tts 怎么有的数据记不住"，说刚结束的对话里 tts 还问"经营什么类目"——但 tts 一直做越南发饰。 [score=0.876 recalls=0 avg=0.620 source=memory/2026-06-13.md:6-6]
<!-- openclaw-memory-promotion:memory:memory/2026-06-13.md:28:30 -->
- 修复方向（待与 HALEI 确认）: **短期**：我（main）代 tts 把 6/10-6/13 的关键事实补到它的 daily + MEMORY（VN 发饰主营、v8.0 草案、SOP 框架调整）; **中期**：要求 tts 每次 cron 跑完 / 每次对话结束前，**必须**写 daily.md（写进 tts SOUL.md 铁律）; **长期**：检查 dreaming 是否能 fallback 到从 session 自动提取关键事实（不依赖 agent 自己写 daily） [score=0.844 recalls=0 avg=0.620 source=memory/2026-06-13.md:28-30]

## Promoted From Short-Term Memory (2026-06-28)

<!-- openclaw-memory-promotion:memory:memory/2026-06-25.md:24:26 -->
- 边界（我守住的）: 改 tts SOUL/MEMORY 时跟 HALEI 确认了"是动灵魂"; 删旧 cron/建新 cron 前跟 HALEI 确认了"v7.0 是否保留"; 没碰 HALEI 的 Chrome 登录流程 [score=0.815 recalls=0 avg=0.620 source=memory/2026-06-25.md:24-26]
<!-- openclaw-memory-promotion:memory:memory/2026-06-25.md:29:31 -->
- 待办: [ ] 观察 16:00 v8.0 cron 首次跑（越南 16:00 / 泰国 16:00）; [ ] 如果 16:00 跑成功，跟 HALEI 确认权重倾向 + API 修复方向; [ ] 自己的 MEMORY.md 是否要更新（店铺名 Heat Up Glow 现在归到 tts，不归我） [score=0.815 recalls=0 avg=0.620 source=memory/2026-06-25.md:29-31]
<!-- openclaw-memory-promotion:memory:memory/2026-06-25.md:4:4 -->
- 今日概要: **tts agent 系统性修复日**。HALEI 拍板后，我一次性完成 SOUL + daily + cron + MEMORY 四件事。 [score=0.815 recalls=0 avg=0.620 source=memory/2026-06-25.md:4-4]

## Promoted From Short-Term Memory (2026-06-29)

<!-- openclaw-memory-promotion:memory:memory/2026-06-25.md:13:16 -->
- 推进过程: **SOUL.md 加铁律**：记忆铁律（每场结束写 daily）+ 店铺身份（不发明类目）; **补 6/10-6/13 daily**：tts 那四天完全空白（dreaming 没问题，问题在 tts 自己没写）; **删 v7.0 cron**：两条（id 6ee6a981 越南 / dde46f87 泰国）; **建 v8.0 cron**：两条新（id d6ea3ee4 越南 9/12/15/18 / id 91574622 泰国 10/13/16/19） [score=0.828 recalls=0 avg=0.620 source=memory/2026-06-25.md:13-16]
<!-- openclaw-memory-promotion:memory:memory/2026-06-25.md:17:17 -->
- 推进过程: **更新 MEMORY.md**：店铺身份 / Cron 任务 / 已知限制 / 权重调整 [score=0.828 recalls=0 avg=0.620 source=memory/2026-06-25.md:17-17]
<!-- openclaw-memory-promotion:memory:memory/2026-06-25.md:20:21 -->
- 遇到的小波折: HALEI 一开始以为让我直接动 SOUL，我说"重新打开浏览器"——中间插了一轮 Chrome 启动（HALEI 自己点登录卡片）; v7.0 cron "Context overflow: prompt too large for the model" → v8.0 提示词从 ~1.5KB 精简到 ~1.2KB [score=0.828 recalls=0 avg=0.620 source=memory/2026-06-25.md:20-21]
<!-- openclaw-memory-promotion:memory:memory/2026-06-25.md:34:35 -->
- 自我反思: HALEI 说"我是让你重新打开浏览器"——我一开始误解为"动手干 SOUL"。教训：上下文里有"桌面""操作"时，先确认意图再行动。; "我看到桌面了"这句话的隐含信息：HALEI 已经看到结果了 → 我应该去启动/确认，不要绕。 [score=0.828 recalls=0 avg=0.620 source=memory/2026-06-25.md:34-35]
<!-- openclaw-memory-promotion:memory:memory/2026-06-25.md:7:10 -->
- HALEI 拍板的关键决策: 店铺名：**Heat Up Glow - 时尚配件-发饰**; 主营：发饰（不换）; v7.0 cron（毛利率≥70% 硬卡）全部废弃 → v8.0（候选池+人工审核）上线; HALEI 自己操作 Chrome 登录"店铺专用" profile [score=0.828 recalls=0 avg=0.620 source=memory/2026-06-25.md:7-10]

## Promoted From Short-Term Memory (2026-06-30)

<!-- openclaw-memory-promotion:memory:memory/2026-06-27.md:12:15 -->
- 根因: 这台机器出公网，**`github.com` 主站的 `20.205.243.166:443` 走不通**（curl 超时 15s，IP 直连同样超时）; 但 `api.github.com`（`20.205.243.168:443`）和 `raw.githubusercontent.com` 0.5s 通; 典型"主站 IP 被墙、API 放行"; 脚本里 hardcode `https://${GH_TOKEN}@github.com/...` 正好命中坏路径 [score=0.815 recalls=0 avg=0.620 source=memory/2026-06-27.md:12-15]
<!-- openclaw-memory-promotion:memory:memory/2026-06-27.md:23:26 -->
- 修复方案（待 HALEI 拍板）: 给这台机器生成新 SSH key（`ssh-keygen -t ed25519 -C "openclaw-backup@halei"`，不设 passphrase 便于 cron）; HALEI 把公钥加到 GitHub 账号 `59330857` 的 SSH keys; 改 `backup.sh`：; remote URL 换成 `git@github.com:59330857/openclaw-backup.git` [score=0.815 recalls=0 avg=0.620 source=memory/2026-06-27.md:23-26]
<!-- openclaw-memory-promotion:memory:memory/2026-06-27.md:32:33 -->
- 安全 / 敏感信息: `~/.config/gh/hosts.yml` 里的 `oauth_token`（gho_***）当前已失效（401）; 处理：建议一并清理或 rotate [score=0.815 recalls=0 avg=0.620 source=memory/2026-06-27.md:32-33]

## Promoted From Short-Term Memory (2026-07-01)

<!-- openclaw-memory-promotion:memory:memory/2026-06-27.md:18:20 -->
- SSH 状况: `ssh -T git@github.com` → `Permission denied (publickey)`，连接层成功（**22 端口没被墙**）; `~/.ssh/` 里有 `known_hosts` 但**没有任何私钥**（id_ed25519 / id_rsa / id_ecdsa 都没有）; `gh` 配的 `oauth_token` 当前 API 401（Bad credentials），备份脚本也没用这个 token 走 API [score=0.837 recalls=0 avg=0.620 source=memory/2026-06-27.md:18-20]
<!-- openclaw-memory-promotion:memory:memory/2026-06-27.md:27:29 -->
- 修复方案（待 HALEI 拍板）: 移除 `GH_TOKEN` 那段（不再需要 PAT）; 手动跑一次脚本验证 + 立刻补一次 5.29~6.27 漏掉的备份（增量同步本地状态到 GitHub）; 长期：脚本里加 connectivity probe（`github.com` 不可达时不要直接 git pull 撞墙，记一条明显的 error） [score=0.837 recalls=0 avg=0.620 source=memory/2026-06-27.md:27-29]
<!-- openclaw-memory-promotion:memory:memory/2026-06-27.md:4:7 -->
- github 备份中断排查: 现象：HALEI 反馈 `59330857/openclaw-backup` 仓库最后 commit 是 `2026-05-28 03:24`，30 天没新提交; cron 入口：`0 3 * * * /home/halei/.openclaw/workspace/skills/openclaw-backup/backup.sh`（脚本 v3.1 / 2026-04-21 写）; 本地日志 `/tmp/openclaw-full-backup.log` 只剩 6/26、6/27 两天（5.29 之后的历史被 rotate）; 6/26、6/27 报错一致： [score=0.837 recalls=0 avg=0.620 source=memory/2026-06-27.md:4-7]
<!-- openclaw-memory-promotion:memory:memory/2026-06-27.md:8:9 -->
- github 备份中断排查: `fatal: 无法访问 'https://github.com/59330857/openclaw-backup.git/'：GnuTLS recv error (-110): The TLS connection was non-properly terminated.`; `fatal: 不是 git 仓库（或者任何父目录）：.git`（因为 git clone 失败，`/tmp/openclaw-backup-clone/` 不是 git repo） [score=0.837 recalls=0 avg=0.620 source=memory/2026-06-27.md:8-9]
