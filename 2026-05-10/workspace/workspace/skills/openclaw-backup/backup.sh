#!/bin/bash
# OpenClaw Daily Backup Script
# Syncs local OpenClaw state to GitHub backup repo

BACKUP_REPO="/tmp/openclaw-backup-clone"
OPENCLAW_DIR="$HOME/.openclaw"
GIT_REF="main"

# Get GH token from gh config
GH_TOKEN=$(grep "oauth_token:" ~/.config/gh/hosts.yml | awk '{print $2}')

set -e

echo "[$(date)] Starting OpenClaw backup..."

# Sync from GitHub first (in case of changes from other machines)
cd "$BACKUP_REPO"
git checkout "$GIT_REF" 2>/dev/null || git clone "https://${GH_TOKEN}@github.com/59330857/openclaw-backup.git" "$BACKUP_REPO"
git pull origin "$GIT_REF" --quiet

# Sync key directories
rsync -a --delete \
  "$OPENCLAW_DIR/agents/" \
  "$BACKUP_REPO/agents/"

rsync -a --delete \
  "$OPENCLAW_DIR/workspace/" \
  "$BACKUP_REPO/workspace/"

rsync -a --delete \
  "$OPENCLAW_DIR/workspace-main/" \
  "$BACKUP_REPO/workspace-main/"

rsync -a --delete \
  "$OPENCLAW_DIR/workspace-selector/" \
  "$BACKUP_REPO/workspace-selector/"

rsync -a --delete \
  "$OPENCLAW_DIR/workspace/skills/" \
  "$BACKUP_REPO/workspace/skills/"

# Sync openviking extension config
rsync -a --delete \
  "$OPENCLAW_DIR/extensions/openviking/" \
  "$BACKUP_REPO/openviking/"

# Commit and push if there are changes
cd "$BACKUP_REPO"
if git diff --quiet && git diff --cached --quiet; then
  echo "[$(date)] No changes, skipping commit"
else
  git config user.email "backup@openclaw"
  git config user.name "OpenClaw Backup"
  git add -A
  git commit -m "Full backup $(date '+%Y-%m-%d %H:%M')"
  git push origin "$GIT_REF"
  echo "[$(date)] Backup pushed to GitHub"
fi
