#!/usr/bin/env node
/**
 * Director Agent - 任务协调引擎
 * 每30分钟运行一次，检查任务池并下发指令
 */

import { readFileSync, writeFileSync, readdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const TEAM_DIR = __dirname; // 直接是 cross-border 目录
const TASK_POOL = join(TEAM_DIR, 'tasks', 'task-pool.json');
const RESULTS_DIR = join(TEAM_DIR, 'results');

// 读取任务池
function loadTasks() {
  try {
    const data = readFileSync(TASK_POOL, 'utf-8');
    return JSON.parse(data);
  } catch {
    return { tasks: [], last_updated: null };
  }
}

// 写入任务池
function saveTasks(pool) {
  pool.last_updated = new Date().toISOString();
  writeFileSync(TASK_POOL, JSON.stringify(pool, null, 2));
}

// 读取已完成的执行结果
function loadResults(taskId) {
  const resultPath = join(RESULTS_DIR, `${taskId}.json`);
  try {
    return JSON.parse(readFileSync(resultPath, 'utf-8'));
  } catch {
    return null;
  }
}

// 主逻辑
const pool = loadTasks();
const pending = pool.tasks.filter(t => t.status === 'pending');

if (pending.length === 0) {
  console.log('[Director] 无待下发任务');
  process.exit(0);
}

console.log(`[Director] 发现 ${pending.length} 个待处理任务`);

// 遍历任务，下发到对应 Agent
for (const task of pending) {
  // 标记为进行中
  task.status = 'dispatched';
  task.dispatched_at = new Date().toISOString();
  
  console.log(`[Director] → ${task.to.join(', ')}: ${task.content}`);
  console.log(`[Director] 任务ID: ${task.id} | 类型: ${task.type} | 截止: ${task.deadline || '未设'}`);
  
  // 结果写回路径说明
  const resultPath = join(RESULTS_DIR, `${task.id}.json`);
  console.log(`[Director] 预期结果路径: ${resultPath}`);
}

saveTasks(pool);
console.log('[Director] 本轮调度完成');