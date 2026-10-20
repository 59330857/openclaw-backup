---
name: openclaw-doctor
description: OpenClaw 诊断与维修工具。用于排查和修复 OpenClaw Gateway、通道、模型配置等问题。当用户报告 OpenClaw 无响应、功能异常、连接失败时使用此 Skill。
metadata:
  openclaw:
    triggers:
      - "openclaw 没响应"
      - "gateway 没响应"
      - "openclaw 故障"
      - "openclaw 维修"
      - "openclaw doctor"
      - "openclaw 问题"
      - "openclaw 错误"
      - "通道连接失败"
      - "飞书没响应"
      - "微信没响应"
---

# OpenClaw Doctor - 诊断与维修

当用户报告 OpenClaw 相关问题时，使用此 Skill 进行排查和修复。

## 诊断流程

### 1. 检查 Gateway 状态

首先检查 Gateway 是否运行：

```bash
openclaw gateway status
```

检查端口是否监听：

```bash
ss -tlnp | grep 18789
```

### 2. 检查进程

```bash
ps aux | grep openclaw
```

### 3. 查看日志

```bash
openclaw logs --limit 50
```

或者查看文件日志：

```bash
tail -100 /tmp/openclaw/openclaw-$(date +%Y-%m-%d).log
```

### 4. 运行 doctor

```bash
openclaw doctor
openclaw doctor --repair
```

### 5. 检查通道状态

```bash
openclaw channels status
```

### 6. 检查模型状态

```bash
openclaw models status
```

## 常见问题与解决方案

### 问题：Gateway 无响应

**诊断：**
```bash
openclaw gateway status
curl http://127.0.0.1:18789/
```

**解决方案：**
```bash
# 重启 Gateway
openclaw gateway restart

# 或者重新安装服务
openclaw gateway uninstall
openclaw gateway install
openclaw gateway start
```

### 问题：飞书通道连接失败

**诊断：**
```bash
openclaw channels logs --channel feishu --lines 50
```

**解决方案：**
```bash
# 重新登录飞书
openclaw channels logout --channel feishu
openclaw channels login --channel feishu

# 检查配置
openclaw config get channels.feishu
```

### 问题：微信通道 session 过期

**日志特征：**
```
weixin getUpdates: session expired (errcode -14), pausing bot for 60 min
```

**解决方案：**
```bash
# 需要重新获取微信登录态
# 查看配置
openclaw config get channels.openclaw-weixin
```

### 问题：模型认证失败

**诊断：**
```bash
openclaw models status --probe
```

**解决方案：**
```bash
# 重新配置模型认证
openclaw models auth add

# 或者使用 setup-token
openclaw models auth setup-token --provider anthropic
```

### 问题：端口被占用

**诊断：**
```bash
lsof -i :18789
```

**解决方案：**
```bash
# 杀掉占用进程
kill <pid>

# 或者使用 --force 启动
openclaw gateway run --force
```

### 问题：配置文件错误

**诊断：**
```bash
openclaw config validate
```

**解决方案：**
```bash
# 查看配置
openclaw config file
openclaw config get

# 重置配置
openclaw reset --scope config --yes
```

## 维修命令速查

| 操作 | 命令 |
|------|------|
| 检查状态 | `openclaw gateway status` |
| 重启 Gateway | `openclaw gateway restart` |
| 查看日志 | `openclaw logs --limit 50` |
| 通道状态 | `openclaw channels status` |
| 模型状态 | `openclaw models status` |
| 诊断修复 | `openclaw doctor --repair` |
| 通道日志 | `openclaw channels logs --lines 50` |

## 自动修复

当需要自动修复时，执行：

```bash
openclaw doctor --repair --force
```

这将尝试自动修复常见问题。
