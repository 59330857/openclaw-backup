---
name: google-trends
version: 1.0.0
description: 监控 Google Trends——获取热门搜索、对比关键词、追踪搜索热度变化。适用于市场调研、内容规划和趋势分析。
author: Buba Draugelis
license: MIT
tags:
  - trends
  - marketing
  - research
  - seo
  - content
metadata:
  openclaw:
    emoji: "📈"
---

# Google Trends 监控

监控和分析 Google Trends 数据，用于市场调研、内容规划和趋势追踪。

## 功能

1. **每日热门搜索** - 获取任意国家/地区的当日热搜
2. **关键词热度趋势** - 关键词的历史趋势数据
3. **关键词对比** - 对比多个关键词的热度
4. **相关主题和查询** - 发现相关搜索
5. **地区热度分布** - 查看关键词在哪些地区最热门

## 使用方法

### 获取热门搜索（当日）

使用 web_fetch 获取 Google Trends RSS：

```bash
# 美国每日趋势
curl -s "https://trends.google.com/trending/rss?geo=US" | head -100

# 立陶宛
curl -s "https://trends.google.com/trending/rss?geo=LT" | head -100

# 全球
curl -s "https://trends.google.com/trending/rss?geo=" | head -100
```

### 查看关键词热度

如需详细的关键词分析，请使用 Google Trends 网站：

```bash
# 在浏览器中打开
open "https://trends.google.com/trends/explore?q=bitcoin&geo=US"

# 或通过 web_fetch 获取基本数据
web_fetch "https://trends.google.com/trends/explore?q=bitcoin"
```

### 对比关键词

```bash
# 对比多个搜索词（逗号分隔）
open "https://trends.google.com/trends/explore?q=bitcoin,ethereum,solana&geo=US"
```

## 脚本

### trends-daily.sh

获取当日热门搜索：

```bash
#!/bin/bash
# 用法: ./trends-daily.sh [国家代码]
# 示例: ./trends-daily.sh LT

GEO="${1:-US}"
curl -s "https://trends.google.com/trending/rss?geo=$GEO" | \
  grep -o '<title>[^<]*</title>' | \
  sed 's/<[^>]*>//g' | \
  tail -n +2 | \
  head -20
```

### trends-compare.sh

生成对比链接：

```bash
#!/bin/bash
# 用法: ./trends-compare.sh 关键词1 关键词2 关键词3
# 示例: ./trends-compare.sh bitcoin ethereum solana

KEYWORDS=$(echo "$@" | tr ' ' ',')
echo "https://trends.google.com/trends/explore?q=$KEYWORDS"
```

## 示例工作流

### 早间市场调研

```
1. 获取美国热门搜索
2. 获取立陶宛热门搜索
3. 检查是否有与我们业务相关的趋势
4. 报告有价值的发现
```

### 内容规划

```
1. 对比潜在的博客主题
2. 找出搜索热度更高的主题
3. 检查季节性规律
4. 决定内容重点方向
```

### 竞争对手监控

```
1. 对比品牌名称
2. 追踪热度随时间的变化
3. 识别竞争对手热度飙升的时间点
4. 调查原因
```

## 定时任务集成

设置自动化趋势监控：

```javascript
// 示例：每日趋势报告定时任务
{
  "name": "Daily Trends Report",
  "schedule": { "kind": "cron", "expr": "0 9 * * *" },
  "payload": {
    "kind": "agentTurn",
    "message": "Get today's Google Trends for US and LT. Summarize top 10 trends for each. Highlight any tech/business related trends."
  }
}
```

## 国家/地区

常用国家代码：
- US - 美国
- LT - 立陶宛
- DE - 德国
- GB - 英国
- FR - 法国
- JP - 日本
- （空）- 全球

## 限制

- Google Trends 不提供官方 API
- 频繁使用可能触发速率限制
- 数据为相对值（非绝对数字）
- 详细视图的历史数据限制约为 5 年

## 使用技巧

1. **使用具体搜索词** - 用 "iPhone 15 Pro" 而非仅用 "iPhone"
2. **关注季节性** - 某些趋势具有周期性
3. **与基准对比** - 使用一个稳定的搜索词作为参照
4. **查看相关查询** - 发现新机会
5. **监控竞争对手** - 追踪品牌热度随时间的变化
