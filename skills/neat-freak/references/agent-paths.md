# Codex 记忆与配置路径速查

这个本地版本是 Codex-first。执行盘点时，以 `AGENTS.md` 和项目 docs 为主线；其他 agent 专用文件只在已经存在或用户明确要求时作为兼容文件处理。

## OpenAI Codex

| 用途 | 路径 |
|---|---|
| 全局跨项目指令 | `~/.codex/AGENTS.md` 或 `$CODEX_HOME/AGENTS.md` |
| 项目级指令 | 项目根 `AGENTS.md`，可按目录层级覆盖 |
| 项目级 override | `AGENTS.override.md`，若存在则覆盖同目录 `AGENTS.md` |
| 用户级 skills | `~/.codex/skills/<name>/SKILL.md` |
| 项目级 skills | `<project>/.codex/skills/<name>/SKILL.md` |

Codex 没有独立的“记忆文件 + 索引”机制。需要跨会话保留的项目事实默认写进项目 `AGENTS.md`；只有跨项目稳定原则才写进全局 Codex 指令。

## 读取优先级

1. 当前工作目录及其父目录中的 `AGENTS.md`。
2. 同目录 `AGENTS.override.md`，如果存在。
3. 项目 `README.md` 和 `docs/`。
4. 全局 `~/.codex/AGENTS.md` 或 `$CODEX_HOME/AGENTS.md`，仅限跨项目原则或用户明确要求。
5. 已存在的非 Codex agent 指令文件，仅作兼容检查。

## 兼容文件策略

如果项目里已经有其他 agent 使用的指令文件：

- 读取它们，避免与 `AGENTS.md`、README、docs 互相矛盾。
- 只有当它们已经存在且内容会误导后续 agent 时才同步。
- 不要默认新建非 Codex 指令文件。
- 不要把非 Codex 文件作为主入口；Codex 本地知识主线始终是 `AGENTS.md`。

## 创建规则

- 项目已有可运行代码但缺少 `AGENTS.md`：可以创建，内容只写稳定项目事实、命令、红线和环境约束。
- 只是一次性脚本或早期试验：不要急着创建 `AGENTS.md`，在摘要中说明未创建原因。
- 全局 Codex 指令只记录跨项目长期原则，不记录单个项目细节。
