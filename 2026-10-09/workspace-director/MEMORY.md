# Long-Term Memory


## Promoted From Short-Term Memory (2026-06-05)

<!-- openclaw-memory-promotion:memory:memory/2026-05-10.md:5:8 -->
- 今天发生的事: 我（舟🐟）正式上线; 老板首次对话，说以后用中文沟通; 帮我取了名字「舟」，定位是运营总监风格; 设定了基本沟通风格：沉稳、有谋略、言简意赅 [score=0.836 recalls=0 avg=0.620 source=memory/2026-05-10.md:5-8]
<!-- openclaw-memory-promotion:memory:memory/2026-05-10.md:12:13 -->
- 待补充: 老板的具体背景和业务; 我负责的运营范围 [score=0.836 recalls=0 avg=0.620 source=memory/2026-05-10.md:12-13]

## Promoted From Short-Term Memory (2026-07-07)

<!-- openclaw-memory-promotion:memory:memory/2026-07-04.md:23:24 -->
- 妙手 ERP: HALEI 提到妙手 ERP 可实现：采集→编辑→发布，已接入但未集成进 TTS 流程; 需要单独研究接入方式 [score=0.815 recalls=0 avg=0.620 source=memory/2026-07-04.md:23-24]
<!-- openclaw-memory-promotion:memory:memory/2026-07-04.md:32:35 -->
- 待办: [ ] 修复 TTS Agent 的 Sorftime 调用方式（改为 mcporter call）; [ ] 确认泰国类目正确 nodeId; [ ] 排查 1688/TikTok MCP 报错原因; [ ] 和 HALEI 确认投流 Agent 位置和能力 [score=0.815 recalls=0 avg=0.620 source=memory/2026-07-04.md:32-35]
<!-- openclaw-memory-promotion:memory:memory/2026-07-04.md:36:38 -->
- 待办: [ ] 妙手 ERP Skill 接入研究; [ ] 建立选品→采集→上传 SOP 全链路; [ ] 浏览器启动 + TikTok Seller Center 登录 [score=0.815 recalls=0 avg=0.620 source=memory/2026-07-04.md:36-38]

## Promoted From Short-Term Memory (2026-07-08)

<!-- openclaw-memory-promotion:memory:memory/2026-07-04.md:14:16 -->
- 选品库状态: 表格：TTS-东南亚-发饰店铺一张表 v2.0（AKppbAeyXanToTsVl6ScxO5QnZd）; 选品库：34条记录，字段完整（日期/商品名称/月销量/增长率/利润率/1688链接/三级类目/站点/推荐等级/行动建议等）; 写入问题：之前写入失败，疑为数据格式/字段映射问题 [score=0.869 recalls=0 avg=0.620 source=memory/2026-07-04.md:14-16]
<!-- openclaw-memory-promotion:memory:memory/2026-07-04.md:19:20 -->
- 投流 Agent: 未在当前 sessions 列表中看到，可能在其他 channel 或尚未建立; 需要和 HALEI 确认投流 Agent 的位置和现有能力 [score=0.869 recalls=0 avg=0.620 source=memory/2026-07-04.md:19-20]
<!-- openclaw-memory-promotion:memory:memory/2026-07-04.md:27:29 -->
- OpenClaw 浏览器能力: Chrome 已检测到（/usr/bin/google-chrome-stable），browser 工具可用; 可用于：TikTok Seller Center 后台数据抓取、广告计划监控; 需 HALEI 提供登录态或登录方式 [score=0.869 recalls=0 avg=0.620 source=memory/2026-07-04.md:27-29]
<!-- openclaw-memory-promotion:memory:memory/2026-07-04.md:6:9 -->
- TTS 选品 Agent 诊断: TTS Agent 存在，有越南/泰国两条选品 cron（v8.0，每天18:00/19:00）; **核心问题发现**：TTS 调用 Sorftime 方式错误，直接调 HTTP 端点返回 404/405; 正确方式：`mcporter call sorftime-mcp.<tool>` — 已验证完全可用; Sorftime 越南 API 实测正常（shopee_product_search 返回 iLita 月销1380） [score=0.837 recalls=0 avg=0.620 source=memory/2026-07-04.md:6-9]
<!-- openclaw-memory-promotion:memory:memory/2026-07-04.md:10:11 -->
- TTS 选品 Agent 诊断: 泰国问题：nodeId=11046516 失效，需要重新找正确类目ID; 1688货源、TikTok验证 仍报错（6/13起） [score=0.837 recalls=0 avg=0.620 source=memory/2026-07-04.md:10-11]

## Promoted From Short-Term Memory (2026-07-16)

<!-- openclaw-memory-promotion:memory:memory/2026-07-13.md:11:14 -->
- HALEI 核心诉求（紧急）: 现状：只有一个产品能卖，快要放弃; 需求：让店铺能**持续补充新选品**，目前产品线断档; 新策略参考：反向选品（跟头部店铺新品 + 挖新店小爆品）; 还需要：打通 TikTok Seller Center 后台数据获取 [score=0.815 recalls=0 avg=0.620 source=memory/2026-07-13.md:11-14]
<!-- openclaw-memory-promotion:memory:memory/2026-07-13.md:17:20 -->
- 待研究/待办: [ ] 研究反向选品实操 SOP，结合发饰类目落地; [ ] 浏览器自动化：TikTok Seller Center 后台登录 + 数据获取; [ ] 为什么只有一个品能卖——需要看后台数据诊断; [ ] TTS cron 明天是否正常出候选池（18:00 越南，19:00 泰国） [score=0.815 recalls=0 avg=0.620 source=memory/2026-07-13.md:17-20]
<!-- openclaw-memory-promotion:memory:memory/2026-07-13.md:23:24 -->
- 关键决策: 越南价格下限从 $1.5 调到 10000 VND（$0.4），取消上限; 跟品策略改为"不卡价格，只卡流量信号"，聚焦中高端新品 [score=0.815 recalls=0 avg=0.620 source=memory/2026-07-13.md:23-24]

## Promoted From Short-Term Memory (2026-07-17)

<!-- openclaw-memory-promotion:memory:memory/2026-07-13.md:6:8 -->
- TTS 选品 Agent 修复: **问题诊断**：两个 cron 跑了两周选品无效，根因是 site 参数格式错误（"TH"应为"204"，"VN"应为"201"）+ 调用方式错（用 curl 调 HTTP 端点而非 mcporter）+ delivery.to 未指定; **已修复**：泰国越南两个 cron 的 prompt、toolsAllow、delivery 配置全部更新完毕; **验证**：实测 `mcporter call sorftime-mcp shopee_product_search` 可正常返回数据 [score=0.869 recalls=0 avg=0.620 source=memory/2026-07-13.md:6-8]
