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
APP_ID="cli_a93650c6fc785bce"
APP_SECRET="I6PGaAjXEqMW81COlOcRzc7zpdd2qqOV"
USER_OPEN_ID="ou_f590c429b7ded95568bebca2f534efdb"

TOKEN_RESP=$(curl -s -X POST "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal" \
  -H "Content-Type: application/json" \
  -d "{\"app_id\":\"$APP_ID\",\"app_secret\":\"$APP_SECRET\"}")
ACCESS_TOKEN=$(echo $TOKEN_RESP | python3 -c "import json,sys; print(json.load(sys.stdin).get('tenant_access_token',''))")

if [ -n "$ACCESS_TOKEN" ]; then
  # Extract summary from log
  EVOLVE_SUMMARY=$(grep -E "Mutation directive|Signal Hints|recommended_intent|result|状态" "$LOG_FILE" | tail -3 | sed 's/"/\\"/g' | tr '\n' ' ')
  if [ -z "$EVOLVE_SUMMARY" ]; then
    EVOLVE_SUMMARY="运行完成"
  fi

  if [ $EVOLVE_EXIT -eq 0 ]; then
    NOTIF_MSG="🧬 Capability Evolver 完成\n\n$EVOLVE_SUMMARY"
  else
    NOTIF_MSG="⚠️ Capability Evolver 有错误（exit $EVOLVE_EXIT）\n\n$EVOLVE_SUMMARY"
  fi

  curl -s -X POST "https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=open_id" \
    -H "Authorization: Bearer $ACCESS_TOKEN" \
    -H "Content-Type: application/json" \
    -d "{
      \"receive_id\":\"$USER_OPEN_ID\",
      \"msg_type\":\"text\",
      \"content\":\"{\\\"text\\\":\\\"$NOTIF_MSG\\\"}\"
    }" > /dev/null 2>&1
  echo "[$(date)] Evolver Feishu notification sent"
else
  echo "[$(date)] Failed to get access token, skipping Feishu notification"
fi
# ── End Feishu notification ────────────────────────────────────────
