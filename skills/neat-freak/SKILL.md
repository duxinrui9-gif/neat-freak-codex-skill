---
name: neat-freak
description: "Use when a Codex task needs either a minimal continuation handoff or full end-of-session knowledge cleanup across project README/docs, AGENTS.md, handoff notes, and reusable skill lessons; trigger on a standalone nf or /nf cleanup command, /neat, /sync, tidy up docs, clean up docs, 整理一下, 同步一下, 收尾, compact failed, new-window handoff, stale docs, or conflicting memories. Do not use for personal knowledge vault maintenance; use that vault's dedicated workflow instead."
license: MIT
metadata:
  source: https://github.com/KKKKhazix/khazix-skills/tree/main/neat-freak
  upstream_commit: "7a5c4934be4106ac740ffdb95280bb81b3f4b83c"
  profile: codex-first
---

# 洁癖 — Codex Knowledge Base Neat-Freak

`neat-freak` 是项目知识的编辑器，不是追加式记录员。它维护项目 README、docs、`AGENTS.md`、handoff 和可复用的正式 Skill 规则，使下一次接手能基于当前事实继续工作。

## Scope And Boundaries

- 管理项目文档、项目/全局 `AGENTS.md`、三层 handoff 和正式 Skill；不保存一次性项目事实到 Skill。
- 个人知识库 Vault 应由其专用知识管理工作流维护。检测到 Obsidian Vault 时停止项目式盘点，不创建 handoff、不重组 Vault Markdown。
- 发布、部署、删除、外部写入和生产可见操作仍需用户明确请求。
- 外部目录、telemetry 或仪表盘是独立维护面；技能变化不构成刷新授权。

## Mode Selection

1. 用户明确“只做最小交接”时进入 **safe handoff**。
2. 独立 `nf`、`/nf`、`/neat`、`/sync`，或明确要求完整收尾、同步、沉淀经验时进入 **full cleanup**。
3. 只有渐进式读取后确实无法完成 full cleanup，才降级 safe handoff；长线程、大目录或脏工作区只要求缩小读取范围。

Safe handoff 只确认或创建简短 `docs/handoff.md`，记录当前状态、下一步、关键路径、风险、验证和禁止扫描目录。发现可复用经验但未完成验证时，才创建 `## Pending Skill Knowledge`，每项写候选 Skill、经验、证据和阻塞原因。

## Full Cleanup

1. 先运行 `scripts/inventory_docs.py --root <project-root> --format json`，再按结果读取必要文档；不要默认全量读取或扫描依赖、构建和缓存目录。
2. 优先消费 handoff 中已有 `Pending Skill Knowledge`，总候选最多 3 个；再补本轮实际使用、失败或验证产生的候选。
3. 每个候选依次判断：是否改变未来触发/路由/执行/交付/验证；是否只是项目事实；是否有官方、可复现或跨两次任务的证据；现有规则是否已覆盖。
4. 候选优先级：当前任务的业务 Skill → 实际踩坑的工具/流程 Skill → 元治理 Skill。每个候选必须读取对应 `SKILL.md` 后才能得出结论。
5. 结论只能是 `更新`、`已覆盖`、`项目事实`、`证据不足` 或 `待沉淀`。已覆盖、项目事实和证据不足的 pending 在 handoff 留下结论后删除；阻塞或超过上限才保留。

### 修改授权分级

- full cleanup 可直接修复本轮已使用业务 Skill 的 body/reference 规则，并运行最小验证。
- 安装、删除、frontmatter、package membership、system/plugin Skill、全局规则和公开发现面只形成候选与证据，等待用户明确授权。
- 不刷新外部目录、telemetry 或仪表盘，除非用户明确要求。

完整盘点、影响判断、编辑顺序和自检见 [references/full-cleanup-procedure.md](references/full-cleanup-procedure.md)。变更影响与 Skill 同步边界见 [references/sync-matrix.md](references/sync-matrix.md)。三层 handoff 的创建阈值见 [docs/handoff-three-layer-architecture.md](docs/handoff-three-layer-architecture.md)。

## Editing Rules

- 合并优于追加，删除已完成临时事实，使用绝对日期。
- `AGENTS.md` 写 Codex 操作约束；docs 面向接手者；Skill 只写跨任务可复用规则。
- 三层结构：handoff 放当前状态，history 放时间线，archive 放长证据。没有长期价值时不要为了形式创建它们。
- 修改后做最小相关验证；无法验证时写明原因与风险。

## Completion Contract

最终摘要只列实际结果，并始终包含一条 Skill 结论：

- `更新 skill：<name> — <规则变化>`
- `未更新 skill：<name> — 已覆盖 / 项目事实 / 证据不足`
- `待沉淀 skill：<name> — 阻塞原因与证据路径`
- `未更新 skill：无候选 — 本轮没有跨任务可复用经验`

空分组省略。Safe handoff 不得伪装成完整清理或“无可复用规则”。

## References

- [references/full-cleanup-procedure.md](references/full-cleanup-procedure.md) — 项目盘点、影响判断、编辑顺序与自检
- [references/sync-matrix.md](references/sync-matrix.md) — 变更类型到文档与 Skill 的映射
- [references/agent-paths.md](references/agent-paths.md) — Codex 指令与 Skill 路径
- [docs/handoff-three-layer-architecture.md](docs/handoff-three-layer-architecture.md) — handoff、history、archive 架构
