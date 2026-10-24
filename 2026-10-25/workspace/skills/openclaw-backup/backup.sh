#!/bin/bash
# OpenClaw Daily Backup Script (v3.1 — 2026-04-21)
# 只做备份，不跑 evolver

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
do_rsync "$HOME/workspace-tts/" "workspace-tts/"
do_rsync "$OPENCLAW_DIR/workspace-agent-orchestrator/" "workspace-agent-orchestrator/"
do_rsync "$OPENCLAW_DIR/workspace-main/" "workspace-main/"
do_rsync "$HOME/workspace-content/" "workspace-content/"
do_rsync "$HOME/workspace-koc/" "workspace-koc/"
do_rsync "$HOME/workspace-traffic/" "workspace-traffic/"
do_rsync "$HOME/workspace-ops/" "workspace-ops/"
do_rsync "$HOME/workspace-director/" "workspace-director/"
do_rsync "$HOME/workspace-finance/" "workspace-finance/"
do_rsync "$HOME/workspace-review/" "workspace-review/"
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

  # ── Send Feishu notification ──────────────────────────────────────
  SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
  node "$SCRIPT_DIR/send-to-me.js" "✅ 每日备份完成\n📦 备份 → 已推送至 openclaw-backup" && echo "[$(date)] Backup Feishu notification sent" || echo "[$(date)] Failed to send Feishu notification"
  # ── End Feishu notification ────────────────────────────────────────
else
  echo "[$(date)] No changes, skipping commit"
fi
