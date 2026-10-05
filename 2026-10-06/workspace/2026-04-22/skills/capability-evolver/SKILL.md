---
name: capability-evolver
description: Local evolution engine for OpenClaw (offline, no EvoMap)
metadata: {"openclaw": {"always": true}}
---

# Capability Evolver (OpenClaw Integration)

## How it works
- Automatically review session logs when OpenClaw session ends
- Self-heal tool call errors and optimize execution logic
- Background "dream learning" when OpenClaw is idle
- 100% offline, no network connection to EvoMap

## Usage
Run manually when you want to evolve prompts:
```bash
cd ~/.openclaw/skills/capability-evolver && node index.js
```

Or use as part of OpenClaw skill system.

## Configuration
Set evolution strategy via environment variable:
- `EVOLVE_STRATEGY=balanced` (default, recommend)
- `EVOLVE_STRATEGY=innovate` (max innovation)
- `EVOLVE_STRATEGY=harden` (enhance security)
- `EVOLVE_STRATEGY=repair-only` (only fix errors)

## Offline Mode
Evolver runs completely offline without any network connection to EvoMap Hub.
No `.env` file is needed - this is the default behavior when A2A_HUB_URL is not set.