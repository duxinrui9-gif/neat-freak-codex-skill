# Handoff Three-Layer Architecture

Use this when `neat-freak` is cleaning up a project and the task involves handoff trimming, history archival, audit evidence, or deciding whether to create the three layers. The goal is to keep current handoff short while preserving history and evidence somewhere durable.

## Layer 1: Current Handoff

Default file: `docs/handoff.md`.

Purpose:

- Give the next human or Codex session the current state in 30 seconds.
- Record only active status, unresolved work, risks, and key entry points.
- Stay short. If it grows beyond roughly 80-120 lines, compress old material into the history or archive layer.

Recommended sections:

- `Current State`
- `Recent Changes`
- `Open Items`
- `Risks / Notes`
- `Key Entry Points`
- `History / Archive`

Rules:

- Recent small changes may stay temporarily.
- Completed, committed, or archived history should become one short line plus a link.
- Do not keep long command logs, patch summaries, old plans, or repeated governance rules here.
- Do not store secrets, private URLs, account details, or environment values.

## Pending Skill Knowledge

Create this section in `docs/handoff.md` only when a safe handoff or an incomplete full cleanup has identified reusable Skill knowledge that is not yet resolved. Each item contains:

- `Candidate Skill`
- `Experience Summary`
- `Evidence Path`
- `Unfinished Reason`

Lifecycle:

1. A later full cleanup reads only this section before the wider document inventory.
2. Process pending items in their listed order, with no more than three total Skill candidates in one cleanup.
3. Remove an item after an `updated`, `already covered`, `project fact`, or `insufficient evidence` conclusion is recorded.
4. Keep an item only when it is blocked, cannot be verified, or exceeds the current cleanup limit; update `Unfinished Reason` with the concrete reason and next full-cleanup priority.

Do not use this section for routine project work, customer facts, or completed decisions. It is a small queue, not an audit log.

## Layer 2: History Timeline

Default files, in priority order:

1. Existing project governance log, such as `governance/governance-log.jsonl`.
2. Existing `CHANGELOG.md` or release log.
3. New `docs/CHANGELOG.md` when no better project-specific history file exists.

Purpose:

- Preserve what changed over time without bloating `docs/handoff.md`.
- Record dates, change type, affected area, validation, and links to evidence.
- Keep entries factual and compact.

Rules:

- Use absolute dates, not relative terms.
- Reference commit hashes, audit directories, dashboard hashes, or release identifiers when relevant.
- Do not duplicate long reports; link to the archive layer instead.
- If the project already has a structured log, reuse it instead of creating a competing changelog.

## Layer 3: Evidence Archive

Default location, in priority order:

1. Existing project audit/archive directory, such as `audits/<YYYY-MM-DD-topic>/`.
2. Existing `docs/archive/<YYYY-MM-DD-topic>/`.
3. New `docs/archive/README.md` plus dated subdirectories when no archive exists.

Purpose:

- Store bulky evidence that should not live in `handoff.md`.
- Preserve reports, before/after notes, patch files, failed attempts, command transcripts, screenshots, checksums, and audit outputs.

Rules:

- One event or audit gets one dated folder.
- Keep each folder self-describing with a short `README.md`.
- Do not commit caches, dependency directories, build output, large binaries, or secrets.
- Historical absolute local paths may remain only when they are necessary audit evidence in a private repo.

## Creation Threshold

Do not create all three layers by default.

- Create or update `docs/handoff.md` when the project has durable work and future sessions need a current state.
- Create or update a history timeline only when there is completed history worth finding later, such as commits, releases, governance changes, dashboard/catalog changes, or architecture decisions.
- Create or update an archive only when there is long evidence worth preserving, such as audit reports, patches, before/after files, command logs, screenshots, or rollback material.
- For a small task with no future handoff, no completed history, and no long evidence, do not create new layers just for formality.

Quick rule:

- Current handoff needed now -> `docs/handoff.md`.
- Timeline needed later -> `docs/CHANGELOG.md` or existing governance log.
- Evidence or rollback material needed later -> `docs/archive/` or existing `audits/`.

## Cleanup Workflow

When running `neat-freak`:

1. Check whether the project has `docs/handoff.md`, a history timeline, and an evidence archive.
2. Reuse existing structures first; create missing defaults only when the project has enough durable work to justify them.
3. Move completed historical detail out of `docs/handoff.md`.
4. Keep the current handoff focused on what the next session must know now.
5. Put reusable cross-project rules into `AGENTS.md`, project docs, or the relevant skill instead of repeating them in every handoff.

If the user asks for only a minimal context rescue, use safe handoff mode: update `docs/handoff.md` and leave history/archive cleanup as a follow-up.
