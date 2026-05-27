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

（设计过的多 Agent 系统架构。）

## 编排模式

（验证过的有效协作模式。）

## 记忆

> 沉淀过的认知。决策、教训、重要偏好、关键上下文。memory/ 是笔记，这里是定稿。

## 指挥/通知优先级规则
- 当你让我「通知、指挥、调度」某个 Agent 时，**优先使用 `sessions_send` 内部通信**，不走飞书外部消息
- 内部通信不可用时，再降级到飞书消息 API
- 飞书消息仅用于：外部联系人、用户明确要求通过飞书传达的场景

## Promoted From Short-Term Memory (2026-05-19)

<!-- openclaw-memory-promotion:memory:memory/2026-05-10.md:5:5 -->
- 完成了全量 Agent 团队（10 个）的配置，所有 Bot 均已绑定独立飞书账号： [score=0.812 recalls=0 avg=0.620 source=memory/2026-05-10.md:5-5]
<!-- openclaw-memory-promotion:memory:memory/2026-05-10.md:18:18 -->
- 同步更新了 AGENTS.md 和 MEMORY.md 中的团队信息和任务分配映射。 [score=0.812 recalls=0 avg=0.620 source=memory/2026-05-10.md:18-18]
