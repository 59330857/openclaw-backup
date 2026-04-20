#!/bin/bash
# OpenClaw Daily Backup Script (v3 — 2026-04-19)

BACKUP_REPO="/tmp/openclaw-backup-clone"
OPENCLAW_DIR="$HOME/.openclaw"
GIT_REF="main"
DATE_DIR=$(date '+%Y-%m-%d')

GH_TOKEN=$(grep "oauth_token:" ~/.config/gh/hosts.yml | awk '{print $2}')

echo "[$(date)] Starting OpenClaw backup..."

# Clone or update backup repo
if [ -d "$BACKUP_REPO/.git" ]; then
  cd "$BACKUP_REPO"
  git checkout "$GIT_REF" 2>/dev/null
  git pull origin "$GIT_REF" --quiet
else
  rm -rf "$BACKUP_REPO"
  git clone "https://${GH_TOKEN}@github.com/59330857/openclaw-backup.git" "$BACKUP_REPO" --quiet
fi

# Fresh date dir (replace old snapshot entirely)
rm -rf "$BACKUP_REPO/$DATE_DIR"
mkdir -p "$BACKUP_REPO/$DATE_DIR"

# rsync helper: dest always inside $DATE_DIR/
do_rsync() {
  local src="$1"
  local dst="$2"   # relative to $DATE_DIR/
  if [ -e "$src" ]; then
    rsync -a --exclude='.git' "$src" "$BACKUP_REPO/$DATE_DIR/$dst"
  fi
}

# 1. Core config files (no trailing slash = copy as file)
do_rsync "$OPENCLAW_DIR/openclaw.json" ""
do_rsync "$OPENCLAW_DIR/openclaw.json.bak" ""
do_rsync "$OPENCLAW_DIR/openclaw.json.bak.1" ""
do_rsync "$OPENCLAW_DIR/openviking.env" ""

# 2. Directories (trailing slash = copy contents)
do_rsync "$OPENCLAW_DIR/agents/" "agents/"
do_rsync "$OPENCLAW_DIR/credentials/" "credentials/"
do_rsync "$OPENCLAW_DIR/cron/" "cron/"
do_rsync "$OPENCLAW_DIR/devices/" "devices/"
do_rsync "$OPENCLAW_DIR/flows/" "flows/"
do_rsync "$OPENCLAW_DIR/identity/" "identity/"
do_rsync "$OPENCLAW_DIR/feishu/" "feishu/"
do_rsync "$OPENCLAW_DIR/subagents/" "subagents/"
do_rsync "$OPENCLAW_DIR/extensions/" "extensions/"
do_rsync "$OPENCLAW_DIR/skills/" "skills/"
do_rsync "$OPENCLAW_DIR/workspace/" "workspace/"
do_rsync "$OPENCLAW_DIR/workspace-main/" "workspace-main/"
do_rsync "$OPENCLAW_DIR/memory/" "memory/"
do_rsync "$HOME/.evomap/" "evomap/"
do_rsync "$OPENCLAW_DIR/qqbot/" "qqbot/"
do_rsync "$OPENCLAW_DIR/openclaw-weixin/" "openclaw-weixin/"

# Commit and push
cd "$BACKUP_REPO"
if [ -n "$(git status --porcelain)" ]; then
  git config user.email "backup@openclaw"
  git config user.name "OpenClaw Backup"
  git add -A
  git commit -m "Full backup $DATE_DIR $(date '+%H:%M')"
  git push origin "$GIT_REF"
  echo "[$(date)] Backup pushed to GitHub"

  # ── Run Capability Evolver ───────────────────────────────────────
  echo "[$(date)] Starting capability evolver..."
  EVOLVE_OUTPUT=$(cd /home/halei/skills/capability-evolver && EVOLVE_STRATEGY=balanced node index.js run 2>&1)
  EVOLVE_EXIT=$?
  echo "$EVOLVE_OUTPUT"
  if [ $EVOLVE_EXIT -eq 0 ]; then
    EVOLVE_STATUS="✅ Evolution 完成"
    # Extract key info from evolver output
    EVOLVE_SUMMARY=$(echo "$EVOLVE_OUTPUT" | grep -E "Mutation directive|Signal Hints|recommended_intent|finished" | head -5 | tr '\n' ' ')
  else
    EVOLVE_STATUS="⚠️ Evolution 有错误（exit $EVOLVE_EXIT）"
    EVOLVE_SUMMARY=$(echo "$EVOLVE_OUTPUT" | tail -3 | tr '\n' ' ')
  fi
  echo "[$(date)] Capability evolver finished with exit $EVOLVE_EXIT"
  # ── End Capability Evolver ────────────────────────────────────────

  # ── Send Feishu notification ──────────────────────────────────────
  APP_ID="cli_a93650c6fc785bce"
  APP_SECRET="I6PGaAjXEqMW81COlOcRzc7zpdd2qqOV"
  USER_OPEN_ID="ou_f590c429b7ded95568bebca2f534efdb"

  # Get tenant access token
  TOKEN_RESP=$(curl -s -X POST "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal" \
    -H "Content-Type: application/json" \
    -d "{\"app_id\":\"$APP_ID\",\"app_secret\":\"$APP_SECRET\"}")
  ACCESS_TOKEN=$(echo $TOKEN_RESP | python3 -c "import json,sys; print(json.load(sys.stdin).get('tenant_access_token',''))")

  if [ -n "$ACCESS_TOKEN" ]; then
    BACKUP_TIME=$(date '+%Y-%m-%d %H:%M:%S')
    NOTIF_MSG="✅ 每日任务完成\n\n📦 备份 → 已推送至 openclaw-backup\n$EVOLVE_STATUS"
    curl -s -X POST "https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=open_id" \
      -H "Authorization: Bearer $ACCESS_TOKEN" \
      -H "Content-Type: application/json" \
      -d "{
        \"receive_id\":\"$USER_OPEN_ID\",
        \"msg_type\":\"text\",
        \"content\":\"{\\\"text\\\":\\\"$NOTIF_MSG\\\"}\"
      }" > /dev/null 2>&1
    echo "[$(date)] Feishu notification sent"
  else
    echo "[$(date)] Failed to get access token, skipping Feishu notification"
  fi
  # ── End Feishu notification ────────────────────────────────────────
else
  echo "[$(date)] No changes, skipping commit"
fi
