# Neat Freak for Codex

一个面向 Codex 的项目知识收尾 Skill。它用于让 README、docs、AGENTS.md、handoff 与已验证的项目事实保持一致，并在收尾时判断哪些经验值得沉淀为可复用 Skill 规则。

它不是通用格式化器，也不负责个人 Obsidian 知识库维护、部署、删除或其他外部写入。

> **第一次使用？** 先读 [新手使用指南](docs/BEGINNER-GUIDE.zh-CN.md)。它用不需要预先了解 Git、终端或 Skill 的方式说明安装、调用和常见问题。

## 安装

通过 Codex 自带的安装器：

    python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
      --repo duxinrui9-gif/neat-freak-codex-skill \
      --path skills/neat-freak

安装后新建一个 Codex task，或重新打开当前 task，使 Skill 可被发现。

也可以将仓库中的 skills/neat-freak 目录复制到 ~/.codex/skills/neat-freak。

## 使用

以下请求会使用它：

- “整理项目文档并收尾”
- “做最小交接，方便新窗口继续”
- “检查 README、AGENTS 和 handoff 是否与现状一致”
- “沉淀本轮可复用的 Skill 经验”

它提供两种模式：

- safe handoff：只保留下一次接手所需的短交接。
- full cleanup：盘点文档、清理过期叙述、维护三层 handoff，并判断是否需要更新已使用的业务 Skill。

详细规则位于 skills/neat-freak/SKILL.md。

## 包含内容

- 三层 handoff 架构：当前状态、历史时间线、长证据归档。
- 变更影响矩阵：将代码、文档、规则与 Skill 维护关联起来。
- 只读文档盘点脚本及标准库测试。
- Codex 指令与项目文档的路径和优先级说明。

## 来源与许可

本仓库基于 KKKKhazix/khazix-skills 的 neat-freak（MIT）进行 Codex-first 改造。保留原始 MIT 许可与版权声明；详细来源见 NOTICE.md。

## 验证

    python3 /path/to/quick_validate.py skills/neat-freak
    python3 -m unittest skills/neat-freak/scripts/test_inventory_docs.py

本仓库不包含个人项目、Vault 内容、凭据、本机路径或遥测数据。
