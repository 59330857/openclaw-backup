# VibeSurf for OpenClaw

[![GitHub](https://img.shields.io/badge/GitHub-vibesurf--ai/VibeSurf-blue?logo=github)](https://github.com/vibesurf-ai/VibeSurf)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[English](README.md) | [简体中文](README_zh.md)

## Overview

VibeSurf skill for OpenClaw (Claw). Control browsers, search the web, extract data, and automate workflows through VibeSurf.

### What You Can Do

- **Browser Control** - Navigate websites, click elements, fill forms
- **Web Search** - AI-powered search with summarized results
- **Data Extraction** - Extract structured data, tables, lists from pages
- **Content Fetching** - Get webpage content as markdown
- **Screenshots** - Capture webpage visuals
- **Workflows** - Execute pre-built automation workflows
- **App Integrations** - Gmail, GitHub, Slack via Composio
- **File Management** - Upload and download files
- **Configuration** - Manage LLM profiles, MCP servers, schedules

## Prerequisites

### 1. Install VibeSurf

You must have VibeSurf running before using this skill.

#### Local Installation

```bash
# Install VibeSurf
uv tool install vibesurf

# Start VibeSurf server
vibesurf
```

#### Docker Installation

```bash
# Pull and run VibeSurf container
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

VibeSurf will be available at `http://127.0.0.1:9335` by default.

### 2. Set Environment Variable (Optional)

If VibeSurf is running on a different host/port:

```bash
# Linux/macOS
export VIBESURF_ENDPOINT=http://127.0.0.1:9335

# Windows PowerShell
$env:VIBESURF_ENDPOINT="http://127.0.0.1:9335"
```

## Installation

Install the VibeSurf skill using ClawHub:

```bash
npx clawhub@latest install vibesurf
```

Or manually copy the skill folder to your OpenClaw skills directory:

```bash
# Linux/macOS
cp -r vibesurf ~/.openclaw/skills/

# Windows
xcopy /E /I vibesurf %USERPROFILE%\.openclaw\skills\vibesurf
```

### Update

If you already have vibesurf installed and want to update to the latest version:

```bash
npx clawhub update vibesurf
```

To force update (overwrite local modifications):

```bash
npx clawhub update vibesurf --force
```

## Quick Start

After installation and starting VibeSurf, you can:

```
Search for latest AI news
```

```
Fetch content from https://example.com
```

```
Take a screenshot of https://google.com
```

```
Upload file /path/to/document.pdf
```

## Skill Structure

This skill uses **progressive disclosure** - the main `SKILL.md` contains quick reference tables, and detailed guides are in the `references/` folder:

| Task | Reference File |
|------|----------------|
| Web Search | `references/search.md` |
| Browser Control | `references/browser.md` |
| Data Extraction | `references/extraction.md` |
| File Upload/Download | `references/file.md` |
| LLM Configuration | `references/config-llm.md` |
| And more... | See `references/` folder |

## Available References

- **search.md** - AI web search
- **fetch.md** - Fetch URL content
- **crawl.md** - Extract article content
- **summary.md** - Page summarization
- **extraction.md** - Structured data extraction
- **screenshot.md** - Page screenshots
- **browser.md** - Direct browser control
- **browser-use.md** - AI browser automation
- **integrations.md** - External app integrations
- **workflows.md** - Pre-built workflows
- **website-api.md** - Social media platform APIs
- **file.md** - File upload/download
- **config-llm.md** - LLM profile configuration
- **config-mcp.md** - MCP server configuration
- **config-composio.md** - Composio toolkit configuration
- **config-schedule.md** - Workflow scheduling
- **config-vibesurf.md** - VibeSurf API key and workflows

## How It Works

1. **User Request** → OpenClaw reads `SKILL.md`
2. **Decision Table** → Match request to reference file
3. **Load Reference** → Read detailed guide from `references/`
4. **Execute** → Call VibeSurf API endpoints

## API Endpoints

All operations go through VibeSurf's HTTP API:

```
POST $VIBESURF_ENDPOINT/api/tool/execute
```

See individual reference files for specific endpoints and parameters.

## Troubleshooting

### VibeSurf Not Running

```bash
curl $VIBESURF_ENDPOINT/health
```

If this fails, start VibeSurf first:
```bash
vibesurf
```

### Skill Not Found

Make sure the skill is installed in the correct location:
- Global: `~/.openclaw/skills/vibesurf/`
- Workspace: `<project>/.openclaw/skills/vibesurf/`

## Contributing

Contributions welcome! This is a markdown-based skill - edit the SKILL.md and reference files directly.

## License

MIT License

## Related Projects

- [VibeSurf](https://github.com/vibesurf-ai/VibeSurf) - Browser automation framework
- [Claude-Surf](https://github.com/vibesurf-ai/claude-surf) - Claude Code plugin for VibeSurf
