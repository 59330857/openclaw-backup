#!/usr/bin/env python3
"""
searxng_search.py — Search via SearXNG instance
Usage:
  python3 search.py "query" [--host HOST] [--engines ENGINES] [--lang LANG] [--time-range TIME_RANGE] [--limit LIMIT]
  HOST defaults to http://localhost:8888
"""
import json
import sys
import urllib.request
import urllib.parse
import argparse


def search(query, host="http://192.168.31.146:8888", engines=None, categories=None,
           lang=None, time_range=None, limit=10):
    params = {
        "q": query,
        "format": "json",
        "pageno": 1,
    }
    if engines:
        params["engines"] = engines
    if categories:
        params["categories"] = categories
    if lang:
        params["language"] = lang
    if time_range:
        params["time_range"] = time_range

    url = host + "/search?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url, timeout=60) as resp:
            data = json.loads(resp.read().decode())
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

    results = data.get("results", [])[:limit]
    if not results:
        results = data.get("infoboxes", [])[:limit]

    output = []
    for r in results:
        output.append({
            "title": r.get("title", ""),
            "url": r.get("url", r.get("content", "")),
            "content": r.get("content", ""),
            "engine": r.get("engine", ""),
        })

    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search via SearXNG")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--host", default="http://192.168.31.146:8888", help="SearXNG host URL")
    parser.add_argument("--engines", help="Comma-separated engine names, e.g. google,bing")
    parser.add_argument("--categories", help="Comma-separated categories, e.g. general,images")
    parser.add_argument("--lang", help="Language code, e.g. zh,en,all")
    parser.add_argument("--time-range", dest="time_range", help="Time range: day,week,month,year")
    parser.add_argument("--limit", type=int, default=10, help="Max results (default 10)")
    args = parser.parse_args()

    search(
        args.query,
        host=args.host,
        engines=args.engines,
        categories=args.categories,
        lang=args.lang,
        time_range=args.time_range,
        limit=args.limit,
    )
