#!/bin/bash
# Capability Evolver Standalone Runner
# 独立运行 evolver，单独发飞书通知

LOG_FILE="/tmp/openclaw-evolver.log"
EVOLVER_DIR="/home/halei/skills/capability-evolver"

echo "[$(date)] Starting Capability Evolver..."

{
  cd "$EVOLVER_DIR"
  EVOLVE_STRATEGY=balanced node index.js run 2>&1
  EVOLVE_EXIT=$?
} > >(tee -a "$LOG_FILE")

echo "[$(date)] Capability evolver finished with exit $EVOLVE_EXIT"

# ── Send Feishu notification ──────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
if [ $EVOLVE_EXIT -eq 0 ]; then
  node "$SCRIPT_DIR/send-to-me.js" "🧬 Capability Evolver 完成（exit 0）" && echo "[$(date)] Evolver Feishu notification sent"
else
  node "$SCRIPT_DIR/send-to-me.js" "⚠️ Capability Evolver 有错误（exit $EVOLVE_EXIT）" && echo "[$(date)] Evolver Feishu notification sent"
fi
# ── End Feishu notification ────────────────────────────────────────
