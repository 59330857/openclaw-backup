---
name: openclaw-repair
description: 诊断和修复 OpenClaw 各种问题，包括配置错误、服务故障、连接问题等。提供系统健康检查、自动修复和故障排除功能。
tags: [openclaw, repair, diagnostics, troubleshooting, fix]
permissions: [network, shell]
metadata:
  capabilities:
    allow:
      - execute: [openclaw, node, npm, git]
      - read: [~/.openclaw/**]
      - write: [~/.openclaw/**]
    deny:
      - execute: ["!openclaw", "!node", "!npm", "!git"]
---

# OpenClaw Repair

这个 skill 用于诊断和修复 OpenClaw 的各种问题。

## 常用诊断命令

### 健康检查
```bash
openclaw doctor
openclaw doctor --deep
openclaw status
openclaw health
```

### 检查配置
```bash
openclaw config validate
openclaw config get
```

### 检查服务状态
```bash
openclaw gateway status
openclaw logs --limit 50
```

### 检查插件
```bash
openclaw plugins list
openclaw plugins doctor
```

### 检查技能
```bash
openclaw skills list
openclaw skills check
```

## 常见问题修复

### Gateway 无法启动

1. 检查端口占用:
```bash
lsof -i :port
```

2. 强制重启:
```bash
openclaw gateway --force
```

3. 重新安装服务:
```bash
openclaw gateway uninstall
openclaw gateway install
openclaw gateway start
```

### 配置问题

1. 重置配置:
```bash
openclaw reset --scope config --yes
```

2. 重新配置:
```bash
openclaw configure
```

### 认证问题

1. 检查模型状态:
```bash
openclaw models status
```

2. 重新认证:
```bash
openclaw models auth login --provider anthropic
```

### 通道连接问题

1. 检查通道状态:
```bash
openclaw channels status
```

2. 查看通道日志:
```bash
openclaw channels logs --lines 100
```

### 常见修复步骤

1. 运行完整诊断:
```bash
openclaw doctor --repair --yes
```

2. 检查更新:
```bash
openclaw update
```

3. 如果问题持续，尝试完全重置:
```bash
openclaw reset --scope full --yes
openclaw setup --wizard
```

## 自动修复

使用 `openclaw doctor --repair` 可以自动修复常见问题，包括:
- 配置错误修复
- 权限问题修复
- 服务重启
- 依赖检查
