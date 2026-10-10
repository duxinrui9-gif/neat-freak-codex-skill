#!/usr/bin/env python3
"""Read-only project-document inventory for neat-freak full cleanup."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path


PRUNED_DIRS = {".git", ".next", ".turbo", ".vercel", ".cache", ".venv", ".obsidian", "__pycache__", "build", "coverage", "dist", "node_modules"}
KEY_DOCUMENTS = ("README.md", "AGENTS.md", "AGENTS.override.md", "docs/README.md", "docs/handoff.md")
RELATIVE_TIME_RE = re.compile(r"今天|昨天|刚刚|最近|上周|\btoday\b|\byesterday\b|\brecently\b", re.IGNORECASE)
MAX_CANDIDATES = 200
MAX_KEY_READ_BYTES = 512 * 1024


def is_personal_vault(root: Path) -> bool:
    return (root / ".obsidian").is_dir() or ((root / "00_知识库配置.md").is_file() and (root / "90_System" / "知识库自增长说明.md").is_file())


def containing_vault(root: Path) -> Path | None:
    return next((p for p in (root, *root.parents) if is_personal_vault(p)), None)


def markdown_inventory(root: Path) -> tuple[list[dict], int]:
    candidates: list[dict] = []
    omitted = 0
    for current_root, directories, filenames in os.walk(root, topdown=True):
        current = Path(current_root)
        directories[:] = sorted(directory for directory in directories if directory not in PRUNED_DIRS and not (current / directory).is_symlink() and not is_personal_vault(current / directory))
        for filename in sorted(filenames):
            if not filename.endswith(".md"):
                continue
            path = current / filename
            if path.is_symlink():
                continue
            relative = path.relative_to(root).as_posix()
            if len(candidates) >= MAX_CANDIDATES:
                omitted += 1
                continue
            try:
                candidates.append({"path": relative, "bytes": path.stat().st_size})
            except OSError as error:
                candidates.append({"path": relative, "error": type(error).__name__})
    return candidates, omitted


def key_document_report(root: Path) -> list[dict]:
    report: list[dict] = []
    for relative in KEY_DOCUMENTS:
        path = root / relative
        if path.is_symlink() or not path.resolve().is_relative_to(root):
            report.append({"path": relative, "exists": False, "scan_skipped": "symlink_or_outside_root"})
            continue
        item: dict = {"path": relative, "exists": path.is_file()}
        if not path.is_file():
            report.append(item)
            continue
        try:
            size = path.stat().st_size
            item["bytes"] = size
            if size <= MAX_KEY_READ_BYTES:
                text = path.read_text(encoding="utf-8")
                item["relative_time_matches"] = RELATIVE_TIME_RE.findall(text)
            else:
                item["relative_time_matches"] = []
                item["scan_skipped"] = "file_too_large"
        except (OSError, UnicodeDecodeError) as error:
            item["error"] = type(error).__name__
        report.append(item)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--format", choices=("json", "text"), default="text")
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        print(f"Project root not found: {root}", file=sys.stderr)
        return 2
    if containing_vault(root):
        print("Obsidian Vault content detected; use that Vault's dedicated knowledge-management workflow instead.", file=sys.stderr)
        return 3

    candidates, omitted = markdown_inventory(root)
    report = {
        "root": str(root),
        "pruned_directories": sorted(PRUNED_DIRS),
        "key_documents": key_document_report(root),
        "markdown_candidates": candidates,
        "candidate_limit": MAX_CANDIDATES,
        "candidates_omitted": omitted,
    }
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
