#!/bin/bash
# OpenClaw Daily Backup Script
# Syncs local OpenClaw state to GitHub backup repo

BACKUP_REPO="/tmp/openclaw-backup-clone"
OPENCLAW_DIR="$HOME/.openclaw"
GIT_REF="main"
GH_TOKEN="$(gh auth token 2>/dev/null)"

set -e

echo "[$(date)] Starting OpenClaw backup..."

# Sync from GitHub first (in case of changes from other machines)
cd "$BACKUP_REPO"
git checkout "$GIT_REF" 2>/dev/null || git clone "https://$GH_TOKEN@github.com/59330857/openclaw-backup.git" "$BACKUP_REPO"
git pull origin "$GIT_REF" --quiet

# Sync key directories
rsync -a --delete \
  "$OPENCLAW_DIR/agents/" \
  "$OPENCLAW_DIR/workspace/" \
  "$OPENCLAW_DIR/workspace-main/" \
  "$OPENCLAW_DIR/workspace-selector/" \
  "$OPENCLAW_DIR/agents/tts/" \
  "$BACKUP_REPO/"

# Also backup skills (workspace-skills only, not the global ones)
rsync -a --delete \
  "$OPENCLAW_DIR/workspace/skills/" \
  "$BACKUP_REPO/"

# Sync openviking config (not the full db, just config)
rsync -a --delete \
  "$OPENCLAW_DIR/openviking/" \
  "$BACKUP_REPO/"

# Commit and push if there are changes
cd "$BACKUP_REPO"
if git diff --quiet && git diff --cached --quiet; then
  echo "[$(date)] No changes, skipping commit"
else
  git add -A
  git commit -m "Full backup $(date '+%Y-%m-%d %H:%M')"
  git push origin "$GIT_REF"
  echo "[$(date)] Backup pushed to GitHub"
fi
