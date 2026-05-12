# MEMORY.md - 长期记忆

每次醒来都会读这个文件。惜字如金，只留真正重要的。

## 记忆系统架构
- **memory-core**（OpenClaw 内置核心）
- **sqlite-vec**（内置本地向量索引）
- **MEMORY.md + daily.md**（长期文件记忆）
- **.dreams/** — 向量语料存储（session-corpus、short-term-recall 等）

## 用户信息
- HALEI，时间 Asia/Shanghai
- 沟通风格：高效、直接
- 飞书已授权，OpenID: ou_f590c429b7ded95568bebca2f534efdb

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

当前团队（10 个子 Agent）：

| Agent ID | 名称 | 职责 | 飞书账号 |
| -------- | ---- | ---- | -------- |
| tts | 🎯 TK 选品大师 | 选品调研、分析、评分 | tts |
| agent-orchestrator | ⚙️ Agent 编掔工程师 | 多 Agent 编排与协调 | agent-orchestrator |
| content | 🎬 内容专家 | 内容策划、文案、视频脚本 | content |
| koc | 🤝 达人运营 | 达人运营、BD、资源对接 | koc |
| traffic | 📢 投流专家 | 广告投放、流量策略 | traffic |
| ops | 📊 运营助手 | 日常运营、数据跟踪 | ops |
| director | 🧭 运营总监 | 全局统筹、决策审核 | director |
| finance | 💰 财务助手 | 账务、成本、ROI 分析 | finance |
| review | 💬 评论专家 | 评论分析、用户反馈 | review |

任务分配：
- 选品问题 → 分配给 tts
- 内容创作 → 分配给 content
- 达人相关 → 分配给 koc
- 投流投放 → 分配给 traffic
- 运营数据 → 分配给 ops/director
- 财务账目 → 分配给 finance
- 评论反馈 → 分配给 review
- Agent 编排问题 → 分配给 agent-orchestrator
- 通用问题 → 大总管自主处理或协调

## 编排模式

（验证过的有效协作模式。）

## 记忆

> 沉淀过的认知。决策、教训、重要偏好、关键上下文。memory/ 是笔记，这里是定稿。