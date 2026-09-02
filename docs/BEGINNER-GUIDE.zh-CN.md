# Neat Freak 新手使用指南

这是一份给第一次使用 Codex、Git 或项目文档的人看的说明。你不需要先理解所有术语；把需要的指令复制给 Codex 就可以开始。

## 它能帮你做什么

开发、写文档或改网站做了一段时间后，常见的问题是：代码变了，README 没更新；换一个对话后，没人知道做到哪里；旧 handoff 越写越长。Neat Freak 负责在任务结束时整理这些**项目知识**，让下一次接手的人或 Codex 能快速继续。

它会根据你的请求选择两种工作方式：

| 方式 | 适合什么时候 | 结果 |
|---|---|---|
| 最小交接（safe handoff） | 只是要换窗口、暂停，或不想大范围整理 | 一份简短的下一步说明 |
| 完整收尾（full cleanup） | 一个功能、研究或一批修改已经完成 | 检查项目文档是否过期，整理交接，并判断是否有经验值得写回 Skill |

它不会部署网站、删除文件、替你发布内容，也不维护个人 Obsidian 知识库。

## 先认识三个词

- **Skill**：给 Codex 的一套专项工作说明。安装后，你可以用一句自然语言让 Codex 按这套流程工作。
- **handoff**：交接说明。它记录当前进度、下一步和风险，让新对话不用从头猜。
- **AGENTS.md**：项目给 Codex 的长期规则，例如测试方式、目录边界和发布限制。

## 安装

### 推荐：直接让 Codex 安装

在一个 Codex 对话中发送下面这段话：

```text
请从 https://github.com/duxinrui9-gif/neat-freak-codex-skill 安装 neat-freak Skill。
先检查本机是否已有同名 Skill；不要覆盖已有版本，除非我明确同意。安装后验证并告诉我如何在新任务中调用它。
```

安装完成后，请**新建一个 Codex 任务**。Skill 列表通常在任务开始时读取，旧任务不一定立刻显示新 Skill。

### 备用：在终端安装

如果你会使用终端，可在任意目录运行：

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo duxinrui9-gif/neat-freak-codex-skill \
  --path skills/neat-freak
```

随后新建 Codex 任务。若安装器提示同名目录已存在，先让 Codex 帮你比较版本；不要为了省事直接覆盖。

## 第一次怎么用

优先使用下面的完整句子。若你的 Codex 显示 `$neat-freak`，也可以把它放在句首。

### 我要先暂停，换一个对话继续

```text
请用 neat-freak 做最小交接：只更新下一位接手者真正需要的状态、下一步、关键路径、风险和验证结果，不做全面整理。
```

### 这轮任务做完了，帮我正式收尾

```text
请用 neat-freak 做完整收尾：检查 README、docs、AGENTS.md 和 handoff 是否仍与已验证的项目现状一致；只修改确实需要同步的内容，并说明是否有可复用的 Skill 经验。
```

### 我只担心文档和实际工作脱节

```text
请用 neat-freak 检查这个项目的 README、AGENTS.md 和 handoff 是否与当前实现一致。先列出需要确认的差异，再只修复已验证的内容。
```

### 我希望记住这次踩过的坑

```text
请用 neat-freak 判断这次的经验是否值得沉淀为 Skill 规则。项目临时事实不要写进 Skill；证据不足时只记录待验证结论。
```

## 怎样算正常完成

正常的结果应告诉你：改了哪些项目文档、做了什么验证、还有什么没有处理，以及下面四种 Skill 结论之一：

- 更新了哪个 Skill，以及新增了什么可复用规则；
- 已有规则已经覆盖；
- 这只是当前项目的事实，不应该写进 Skill；
- 证据还不够，暂时不沉淀。

“没有更新 Skill”经常是正确结果：不是每次项目经验都适合变成长期规则。

## 常见问题

### 新任务里没有看到 Skill

确认安装成功后再新建任务。仍没有时，把下面这句话发给 Codex：

```text
请只读检查 neat-freak 是否安装在 Codex 的 Skill 目录中，并告诉我发现路径；不要重装或覆盖任何已有 Skill。
```

### handoff 变得很长

下次明确说“做最小交接”。完整收尾才会在确有长期价值时使用 history 或 archive；当前状态应保持短小。

### 我想整理 Obsidian 知识库

不要用 Neat Freak。它负责项目文档和交接，不负责个人知识库。应使用 Obsidian 的专用工作流或 [Obsidian Codex Workbench](https://github.com/duxinrui9-gif/obsidian-codex-workbench)。

### 我想卸载或更新

先让 Codex 检查当前安装路径和版本，再决定是否备份并替换。不要直接删除同名目录，以免丢失你后来加入的本地规则。

## 最简单的记忆方法

任务还没结束但要换窗口，用“最小交接”；任务真正做完、文档可能过期时，用“完整收尾”。
