# VibeSurf for OpenClaw

[![GitHub](https://img.shields.io/badge/GitHub-vibesurf--ai/VibeSurf-blue?logo=github)](https://github.com/vibesurf-ai/VibeSurf)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[English](README.md) | [简体中文](README_zh.md)

## 概述

适用于 OpenClaw (Claw) 的 VibeSurf 技能。通过 VibeSurf 控制浏览器、搜索网页、提取数据和自动化工作流。

### 你可以做什么

- **浏览器控制** - 导航网站、点击元素、填写表单
- **网页搜索** - AI 驱动的搜索并返回摘要结果
- **数据提取** - 从页面提取结构化数据、表格、列表
- **内容获取** - 将网页内容获取为 Markdown 格式
- **截图** - 捕获网页视觉内容
- **工作流** - 执行预构建的自动化工作流
- **应用集成** - 通过 Composio 集成 Gmail、GitHub、Slack
- **文件管理** - 上传和下载文件
- **配置管理** - 管理 LLM 配置、MCP 服务器、定时任务

## 前置条件

### 1. 安装 VibeSurf

在使用此技能之前，必须先运行 VibeSurf。

#### 本地安装

```bash
# 安装 VibeSurf
uv tool install vibesurf

# 启动 VibeSurf 服务器
vibesurf
```

#### Docker 安装

```bash
# 拉取并运行 VibeSurf 容器
docker pull ghcr.io/vibesurf-ai/vibesurf:latest

docker run --name vibesurf -d --restart unless-stopped \
  -p 9335:9335 \
  -p 6080:6080 \
  -p 5901:5901 \
  -v ./data:/data \
  -e IN_DOCKER=true \
  -e VIBESURF_BACKEND_PORT=9335 \
  -e VIBESURF_WORKSPACE=/data/vibesurf_workspace \
  -e RESOLUTION=1440x900x24 \
  --shm-size=4g \
  --cap-add=SYS_ADMIN \
  ghcr.io/vibesurf-ai/vibesurf:latest
```

默认情况下，VibeSurf 将在 `http://127.0.0.1:9335` 上可用。

### 2. 设置环境变量（可选）

如果 VibeSurf 运行在不同的主机/端口上：

```bash
# Linux/macOS
export VIBESURF_ENDPOINT=http://127.0.0.1:9335

# Windows PowerShell
$env:VIBESURF_ENDPOINT="http://127.0.0.1:9335"
```

## 安装

使用 ClawHub 安装 VibeSurf 技能：

```bash
npx clawhub@latest install vibesurf
```

或者手动将技能文件夹复制到 OpenClaw 技能目录：

```bash
# Linux/macOS
cp -r vibesurf ~/.openclaw/skills/

# Windows
xcopy /E /I vibesurf %USERPROFILE%\.openclaw\skills\vibesurf
```

### 更新

如果你已经安装了 vibesurf 并想更新到最新版本：

```bash
npx clawhub update vibesurf
```

强制更新（覆盖本地修改）：

```bash
npx clawhub update vibesurf --force
```

## 快速开始

安装并启动 VibeSurf 后，你可以：

```
搜索最新 AI 新闻
```

```
获取 https://example.com 的内容
```

```
截图 https://google.com
```

```
上传文件 /path/to/document.pdf
```

## 技能结构

此技能使用**渐进式披露**设计 - 主文件 `SKILL.md` 包含快速参考表，详细指南在 `references/` 文件夹中：

| 任务 | 参考文件 |
|------|----------|
| 网页搜索 | `references/search.md` |
| 浏览器控制 | `references/browser.md` |
| 数据提取 | `references/extraction.md` |
| 文件上传/下载 | `references/file.md` |
| LLM 配置 | `references/config-llm.md` |
| 更多... | 查看 `references/` 文件夹 |

## 可用参考文件

- **search.md** - AI 网页搜索
- **fetch.md** - 获取 URL 内容
- **crawl.md** - 提取文章内容
- **summary.md** - 页面摘要
- **extraction.md** - 结构化数据提取
- **screenshot.md** - 页面截图
- **browser.md** - 直接浏览器控制
- **browser-use.md** - AI 浏览器自动化
- **integrations.md** - 外部应用集成
- **workflows.md** - 预构建工作流
- **website-api.md** - 社交媒体平台 API
- **file.md** - 文件上传/下载
- **config-llm.md** - LLM 配置
- **config-mcp.md** - MCP 服务器配置
- **config-composio.md** - Composio 工具包配置
- **config-schedule.md** - 工作流定时调度
- **config-vibesurf.md** - VibeSurf API 密钥和工作流

## 工作原理

1. **用户请求** → OpenClaw 读取 `SKILL.md`
2. **决策表** → 将请求匹配到参考文件
3. **加载参考** → 从 `references/` 读取详细指南
4. **执行** → 调用 VibeSurf API 端点

## API 端点

所有操作都通过 VibeSurf 的 HTTP API：

```
POST $VIBESURF_ENDPOINT/api/tool/execute
```

查看各个参考文件了解具体的端点和参数。

## 故障排除

### VibeSurf 未运行

```bash
curl $VIBESURF_ENDPOINT/health
```

如果失败，先启动 VibeSurf：
```bash
vibesurf
```

### 技能未找到

确保技能安装在正确的位置：
- 全局：`~/.openclaw/skills/vibesurf/`
- 工作区：`<project>/.openclaw/skills/vibesurf/`

## 贡献

欢迎贡献！这是一个基于 Markdown 的技能 - 直接编辑 SKILL.md 和参考文件。

## 许可证

MIT 许可证

## 相关项目

- [VibeSurf](https://github.com/vibesurf-ai/VibeSurf) - 浏览器自动化框架
- [Claude-Surf](https://github.com/vibesurf-ai/claude-surf) - 适用于 Claude Code 的 VibeSurf 插件
