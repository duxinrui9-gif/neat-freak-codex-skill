# Full Cleanup Procedure

Use this only after `neat-freak` selected full cleanup. The main skill owns mode selection and Skill knowledge decisions; this reference owns the project-document procedure.

## 1. Inventory Before Reading

Run:

```bash
python3 scripts/inventory_docs.py --root <project-root> --format json
```

The script is read-only and prunes dependency, build, cache, deployment and Git directories. If it identifies an Obsidian Vault, stop and use that Vault's dedicated knowledge-management workflow instead.

For each affected project root, first read only existing `README.md`, `AGENTS.md`, `AGENTS.override.md`, `docs/README.md`, and `docs/handoff.md`. Read other Markdown only when the inventory, filename, current diff, or this matrix makes it relevant. Record each inspected file as `updated` or `no change`.

## 2. Determine Impact

| Change | Usual durable surfaces |
|---|---|
| API, route, SDK, integration | project instructions, integration guide, architecture |
| Environment or infrastructure | project instructions, runbook, deployment docs |
| User workflow or major feature | README, architecture, current handoff |
| Data model | project instructions and architecture |
| Cross-project contract | upstream and consumer documentation |
| Completed work or long evidence | history log and dated archive, not current handoff |

Correct stale facts, consolidate duplicates, use absolute dates, and keep project facts out of formal Skills.

## 3. Edit In Audience Order

1. Compress current handoff and move completed history or long evidence to existing history/archive locations.
2. Update README and user-facing docs.
3. Update project `AGENTS.md` or `AGENTS.override.md` with stable operating constraints.
4. Apply only authorized body/reference fixes to the selected business Skill; otherwise record a candidate.
5. Touch global instructions only for verified cross-project rules.
6. Synchronize pre-existing non-Codex agent files only when they conflict with the primary Codex surfaces.

## 4. Verify

- Key paths, commands and environment variable names exist before documenting them.
- Current handoff is short and contains no long logs, old plans or completed-history dump.
- History uses an existing changelog/governance log when present; archive evidence is dated and self-describing.
- Relative-time scan results from `inventory_docs.py` are reviewed only for current docs, never blindly replaced in history, quotations or examples.
- Skill changes run `quick_validate`, link/fence checks and the smallest relevant routing dry-run.
- Any unverified conflict stays in `Unresolved` rather than being guessed away.
