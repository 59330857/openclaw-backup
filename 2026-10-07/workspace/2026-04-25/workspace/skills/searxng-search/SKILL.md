---
name: searxng-search
description: SearXNG 元搜索引擎搜索。当用户需要搜索网络信息时使用，支持指定引擎、语言、时间范围、分类。不需要 API key，完全私有。支持普通搜索、图片搜索、新闻搜索。触发场景：(1) 用户说"搜索一下..."、"帮我查一下..." (2) 需要多引擎聚合结果时 (3) 替代 Google/Bing 单引擎搜索。
---

# SearXNG Search Skill

通过自托管的 SearXNG 实例进行聚合搜索，完全私有，不追踪，不依赖商业搜索引擎 API。

## 快速使用

```bash
python3 /home/halei/.openclaw/workspace/skills/searxng-search/scripts/search.py "搜索内容"
```

## 核心参数

| 参数 | 说明 |
|------|------|
| `--host` | SearXNG 地址，默认 `http://192.168.31.146:8888` |
| `--engines` | 指定引擎，逗号分隔，如 `google,bing` |
| `--categories` | 指定分类，如 `general,images` |
| `--lang` | 语言，如 `zh`、`en`、`all` |
| `--time-range` | 时间范围：`day`、`week`、`month`、`year` |
| `--limit` | 结果数量，默认 10 |

## SearXNG 实例部署

Docker 部署（已配置国内镜像）：

```bash
docker run -d \
  --name searxng \
  -p 8888:8888 \
  -e SEARXNG_BASE_URL="http://localhost:8888/" \
  -v ./searxng:/etc/searxng \
  --restart unless-stopped \
  searxng/searxng
```

首次启动后访问 `http://localhost:8888` 完成初始配置，启用需要的搜索引擎。

## API 格式（参考）

搜索接口：`GET /search?q=...&format=json`

返回格式：
```json
{
  "results": [
    {
      "title": "结果标题",
      "url": "https://...",
      "content": "摘要内容",
      "engine": "google"
    }
  ],
  "infoboxes": []
}
```

## 使用示例

```bash
# 基础搜索
python3 search.py "openclaw 使用教程"

# 指定语言和中文
python3 search.py "TikTok 选品工具" --lang zh --limit 5

# 指定引擎和时间内
python3 search.py "AI agent 最新进展" --engines google,bing --time-range month

# 图片搜索
python3 search.py "产品图片" --categories images --limit 8
```
