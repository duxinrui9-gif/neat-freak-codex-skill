# 变更影响矩阵

遇到不确定"这次改动要同步哪些文件"时查这张表。

## 代码层变更 → 文档层变更

| 本次对话发生的事 | 要改的文件(按受众) |
|---|---|
| 新增 API / 路由 | 项目根 markdown 路由清单 · `docs/integration-guide.md` API 速查表 · `docs/architecture.md` Routes 小节 |
| 新增 / 改名 环境变量 | 项目根 markdown 环境变量表 · `docs/operator-runbook.md` 环境变量章节 · `docs/integration-guide.md`(如果下游要配) |
| 新增数据库表 / 列 | 项目根 markdown 数据库表 · `docs/architecture.md` Data Model |
| 新增 / 改动 用户流程 | 项目根 markdown 用户流程 · README 相关命令行示例 · `docs/handoff.md` What Exists Today |
| 新增大特性(能跨多文件) | 以上全部 + `docs/architecture.md` 新增章节 + `docs/handoff.md` 已完成清单 |
| 新增术语 / 改命名 | `docs/integration-guide.md` 术语表(如果有)+ 全局搜索旧术语替换 |
| 部署参数 / 基础设施变化 | `docs/operator-runbook.md` · 项目根 markdown 部署章节 |
| 下游项目接入方式变化 | 下游项目的 `docs/<integration>.md` · 上游项目的 `integration-guide.md` |

## 记忆层变更

| 情况 | 处理方式 |
|---|---|
| 过期事实 | 改记忆文件,同时更新索引(如 MEMORY.md)的 description |
| 相对时间("今天"、"最近") | 全部转成绝对日期(`<YYYY-MM-DD>` 而非"今天") |
| 重复记录(多条说同一件事) | 合并为一条,改索引 |
| 已完成的待办 | 从 `docs/handoff.md` 删除；如有长期追溯价值，压缩进 `docs/CHANGELOG.md`、项目既有治理日志或 archive/audits |
| 推翻的决策 | 删除旧条目,留新决策 |
| 跨会话只用一次的临时上下文 | 删除 |

## Skill 维护变更 → 要同步哪里

每次 `neat-freak` 收尾都要检查本节。只有稳定、可复用、会改变未来执行方式且通过证据门的经验才写进 skill；一次性项目事实不进 skill。涉及安装、合并、删除、package、catalog、dashboard、trigger collision 或 plugin boundary 时，先用这张表选候选 skill，再回到 `SKILL.md` 判断是否真的修改。

外部技能目录、telemetry 和仪表盘可能是手动快照：除非用户明确要求刷新，不运行其生成、索引或发布流程。收尾时只记录本轮验证与待刷新事实；不得把“技能有变化”当作刷新授权。

Skill 修改分级：本轮已使用业务 Skill 的 body/reference 规则可在 full cleanup 中修复；安装、删除、frontmatter、package、system/plugin Skill、全局规则与公开发现面只记录候选和证据，必须等待用户明确授权。

| 本次对话发生的事 | 要同步的 skill 或文件 |
|---|---|
| 新增外部 skill / 从 GitHub 导入 skill | `skill-installer` 安装流程 · package 文案 · 当前任务的验证证据 |
| 新增本地 workflow skill 并让它负责某个长期项目流程 | 对应项目 `AGENTS.md` 路由规则 · package 文案 · 当前任务验证证据；仅在用户明确要求时更新 dashboard/catalog 快照 |
| 未删除 skill，但发生 package membership、family attribution、live count 或路由边界变化 | 项目 README/current state · package 文案 · 当前验证证据；地图快照仅按用户明确请求更新 |
| GitHub 高分 skill 与本地强能力重叠，只软并入非重复部分 | `skill-installer` 合并策略 · `.system/skill-creator` 作者规范 · 当前任务验证证据；不隐含刷新地图 |
| 发现外部 skill 与本地能力相似或重复 | `skill-installer` 合并策略 · 本轮审计中的重复能力与触发抢占检查 |
| 发现 frontmatter、description、相对链接、code fence、progressive disclosure 问题 | `.system/skill-creator` |
| 发现治理、全检、重复名、plugin boundary、trigger collision 问题 | 本轮集中审计、package registry 和治理脚本 |
| 发现完成声明前漏了验证证据 | 补跑当前任务最小相关验证并记录真实结果 |
| 发现收尾时漏同步相关 skill | `neat-freak` |
| 业务域经验会改变某个 skill 的触发、交付或边界 | 对应业务 skill；保持精简，避免把项目事实写进去 |
| safe handoff 已识别到可复用经验 | `docs/handoff.md` 的 `Pending Skill Knowledge`；下次 full cleanup 定点读取并按顺序优先处理，给出结论或更新阻塞原因 |
| pending 项超过本轮候选上限 | 保留超出项；将未完成原因改为“本轮候选上限，下一次 full cleanup 优先处理”，不要删除或宣称已处理 |
| 判断某项 Skill 应更新 | 同轮实际修改该 `SKILL.md` 并完成相关验证；无法完成时保留 pending，而不是只在摘要中写“已更新” |
| 物理删除 plugin cache 或批量删除 skill | 项目 handoff/audit · package manifest/`skills.txt` · 说明当前会话 Available skills 可能需新会话才刷新；dashboard/catalog 快照仅按用户明确请求更新 |

## Context-heavy project / compact failure

当项目或当前线程已经触发上下文膨胀、自动压缩失败、compact failure、长线程接力时，优先保护上下文预算。

| 风险信号 | 处理方式 |
|---|---|
| 存在 `.next/`、`node_modules/`、`.git/`、`.vercel/`、`dist/`、`build/` 等大目录 | 搜索和枚举必须 prune / glob exclude；不要读取目录树全文 |
| `git status` 显示大量改动 | 先看 `git status --short`、`git diff --stat`、`git diff --name-status`；只读必要文件的局部 diff |
| docs 很多或 handoff 很长 | 优先读 `docs/README.md` 和 `docs/handoff.md`；其他文档按影响矩阵点读 |
| 用户明确只要最小交接，或只要求新窗口接力且未要求完整收尾 | 进入 safe handoff mode，只更新 `docs/handoff.md` 和必要 `AGENTS.md` 规则 |
| 大日志、构建输出、源资料清单很长 | 只写摘要、结论、路径和必要错误行，不粘贴全文 |

项目级 `AGENTS.md` 应沉淀的上下文卫生规则：

- 新窗口先读 `AGENTS.md`、`README.md`、`docs/handoff.md`。
- 禁止无排除扫描生成目录、依赖目录、Git 内部目录和部署缓存目录。
- `rg` 使用 `--glob` 排除大目录；`find` 使用 `-prune`。
- Git 检查先用状态和统计，再点读局部 diff。
- 上下文过重时先控制读取范围；只有明确要求最小交接或完整收尾确实无法继续时才做 safe handoff。

## 跨项目影响检查

最容易漏改的场景:

- **上游 API 变了 → 下游 SDK 文档**:协议变化必须两边对齐
- **共享子域 / 路由 / 环境变量改了 → 所有 consumer 项目的 setup 文档**
- **认证中台变更 → 所有接入应用的 integration guide**
- **公共组件 / 基础设施 升级 → 各项目的 operator-runbook 提及版本号的地方**

判断方法:这次改的东西有没有 SDK、子域、共享配置、跨进程协议?有就要在所有依赖项目里搜一遍提到这件事的文档。

## 文档结构通用约定

新增一个能力(API、flow、特性)的标准动作是**按影响补齐**:

1. **integration-guide / 外部视角文档**:怎么用(curl / SDK 示例 / 错误码)
2. **architecture**:怎么工作(数据流、状态机、设计取舍)
3. **runbook**:怎么运维(冒烟命令、故障排查、环境变量)
4. **handoff / CHANGELOG / archive**:当前接手状态进 handoff；完成历史进 CHANGELOG 或治理日志；长证据进 archive/audits

API 速查表、环境变量表、术语表是高频查询的结构化信息,**必须保持"所见即最新"**。
