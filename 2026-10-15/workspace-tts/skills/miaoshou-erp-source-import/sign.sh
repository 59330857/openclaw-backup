#!/bin/bash
# 妙手ERP签名工具
# 用法: ./miaoshou-sign.sh <path> <body_json>
# 或直接 source 导入函数: source miaoshou-sign.sh

CONFIG_FILE="$(dirname "$0")/resources/config.json"

get_config() {
  local key="$1"
  grep -o "\"${key}\"[[:space:]]*:[[:space:]]*\"[^\"]*\"" "$CONFIG_FILE" | head -1 | sed 's/.*:[[:space:]]*"//' | sed 's/"$//'
}

APP_KEY="${MIAOSHOU_APP_KEY:-$(get_config 'app_key')}"
APP_SECRET="${MIAOSHOU_APP_SECRET:-$(get_config 'app_secret')}"
BASE_URL="${MIAOSHOU_BASE_URL:-$(grep 'base_url' "$CONFIG_FILE" | cut -d'"' -f4)}"

if [ -z "$APP_KEY" ] || [ -z "$APP_SECRET" ]; then
  echo "Error: MIAOSHOU_APP_KEY and MIAOSHOU_APP_SECRET must be set or in config.json" >&2
  exit 1
fi

sign_request() {
  local path="$1"
  local body="$2"
  local timestamp
  timestamp=$(date +%s)
  
  local data="${APP_SECRET}${path}${timestamp}${APP_KEY}${body}${APP_SECRET}"
  local sign
  sign=$(echo -n "$data" | openssl dgst -sha256 -hmac "$APP_SECRET" | awk '{print $2}')
  
  echo "$timestamp:$sign"
}

if [ "$#" -ge 2 ]; then
  result=$(sign_request "$1" "$2")
  timestamp=$(echo "$result" | cut -d: -f1)
  sign=$(echo "$result" | cut -d: -f2)
  echo "x-app-key: $APP_KEY"
  echo "x-timestamp: $timestamp"
  echo "x-sign: $sign"
fi