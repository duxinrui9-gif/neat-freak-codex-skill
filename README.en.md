# Neat Freak for Codex

A Codex-oriented project knowledge closeout Skill. It keeps README files, docs, AGENTS.md, handoff notes, and verified project facts aligned, then decides whether a lesson is reusable enough to become a Skill rule.

It is not a generic formatter and does not maintain personal Obsidian Vaults, deploy software, delete files, or perform other external writes.

> **New to Codex or Skills?** A Chinese, beginner-friendly guide is available at [BEGINNER-GUIDE.zh-CN.md](docs/BEGINNER-GUIDE.zh-CN.md).

## Install

Use the bundled Codex installer:

    python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
      --repo duxinrui9-gif/neat-freak-codex-skill \
      --path skills/neat-freak

Start a new Codex task after installation so the Skill can be discovered. You can also copy skills/neat-freak into ~/.codex/skills/neat-freak.

## Use

Typical requests include:

- “Tidy the project documentation and close out the task.”
- “Create a minimal handoff for a fresh task.”
- “Check whether README, AGENTS, and handoff notes match reality.”
- “Capture reusable Skill lessons from this work.”

The Skill has two modes:

- safe handoff: a short continuation brief for the next session.
- full cleanup: document inventory, stale-information cleanup, three-layer handoff maintenance, and evidence-based Skill lessons.

See skills/neat-freak/SKILL.md for the complete instructions.

## Attribution and License

This repository is a Codex-first adaptation of neat-freak from KKKKhazix/khazix-skills, licensed under MIT. The original copyright notice and license are preserved. See NOTICE.md for provenance.
