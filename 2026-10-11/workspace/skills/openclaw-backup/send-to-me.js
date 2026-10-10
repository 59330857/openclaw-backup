#!/usr/bin/env node
/**
 * send-to-me.js — 通过 kiit 的 feishu 会话发消息
 * 用法: node send-to-me.js "消息内容"
 */
const https = require('https');

const config = {
  appId: 'cli_a93650c6fc785bce',
  appSecret: 'I6PGaAjXEqMW81COlOcRzc7zpdd2qqOV',
  userOpenId: 'ou_f590c429b7ded95568bebca2f534efdb'
};

async function getToken() {
  return new Promise((resolve, reject) => {
    const body = JSON.stringify({ app_id: config.appId, app_secret: config.appSecret });
    const options = {
      hostname: 'open.feishu.cn',
      path: '/open-apis/auth/v3/tenant_access_token/internal',
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(body) }
    };
    const req = https.request(options, res => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        const json = JSON.parse(data);
        resolve(json.tenant_access_token || '');
      });
    });
    req.on('error', reject);
    req.write(body);
    req.end();
  });
}

async function sendMessage(token, text) {
  return new Promise((resolve, reject) => {
    const payload = {
      receive_id: config.userOpenId,
      msg_type: 'text',
      content: JSON.stringify({ text })
    };
    const body = JSON.stringify(payload);
    const options = {
      hostname: 'open.feishu.cn',
      path: '/open-apis/im/v1/messages?receive_id_type=open_id',
      method: 'POST',
      headers: {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(body)
      }
    };
    const req = https.request(options, res => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => resolve(JSON.parse(data)));
    });
    req.on('error', reject);
    req.write(body);
    req.end();
  });
}

async function main() {
  const text = process.argv.slice(2).join(' ');
  if (!text) { console.error('Usage: node send-to-me.js "message"'); process.exit(1); }
  const token = await getToken();
  if (!token) { console.error('Failed to get access token'); process.exit(1); }
  const result = await sendMessage(token, text);
  if (result.code !== 0) {
    console.error('Failed to send message:', result.msg);
    process.exit(1);
  }
  console.log('Message sent:', result.data.message_id);
}

main().catch(e => { console.error(e); process.exit(1); });
