#!/usr/bin/env python3
"""Fixture tests for neat-freak's read-only document inventory."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("inventory_docs.py")


class InventoryDocsTests(unittest.TestCase):
    def run_inventory(self, root: Path) -> subprocess.CompletedProcess:
        return subprocess.run([sys.executable, str(SCRIPT), "--root", str(root), "--format", "json"], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)

    def test_prunes_generated_directories_and_scans_current_docs(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            root.joinpath("README.md").write_text("最近 changed\n", encoding="utf-8")
            root.joinpath("node_modules").mkdir()
            root.joinpath("node_modules/ignored.md").write_text("ignored", encoding="utf-8")
            result = self.run_inventory(root)
            report = json.loads(result.stdout)
            self.assertEqual(result.returncode, 0)
            self.assertEqual([item["path"] for item in report["markdown_candidates"]], ["README.md"])
            self.assertIn("最近", report["key_documents"][0]["relative_time_matches"])

    def test_rejects_personal_vault(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            root.joinpath("00_知识库配置.md").write_text("---\n---\n", encoding="utf-8")
            root.joinpath("90_System").mkdir()
            root.joinpath("90_System/知识库自增长说明.md").write_text("# Vault", encoding="utf-8")
            result = self.run_inventory(root)
            self.assertEqual(result.returncode, 3)
            self.assertIn("dedicated knowledge-management workflow", result.stderr)

    def test_rejects_subdirectory_of_generic_vault(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / ".obsidian").mkdir()
            (root / "notes").mkdir()
            self.assertEqual(self.run_inventory(root / "notes").returncode, 3)

    def test_workbench_repository_skips_nested_vault(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "README.md").write_text("Project documentation")
            (root / "starter-vault/90_System").mkdir(parents=True)
            (root / "starter-vault/00_知识库配置.md").write_text("config")
            (root / "starter-vault/90_System/知识库自增长说明.md").write_text("vault")
            (root / ".venv").mkdir()
            (root / ".venv/noise.md").write_text("noise")
            result = self.run_inventory(root)
            self.assertEqual(result.returncode, 0)
            report = json.loads(result.stdout)
            self.assertEqual([x['path'] for x in report['markdown_candidates']], ['README.md'])

    def test_does_not_read_external_key_document_symlink(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            parent = Path(temporary)
            root = parent / "project"
            root.mkdir()
            (parent / "external.md").write_text("最近 private outside scope")
            (root / "README.md").symlink_to(parent / "external.md")
            result = self.run_inventory(root)
            report = json.loads(result.stdout)
            self.assertEqual(report['markdown_candidates'], [])
            self.assertEqual(report['key_documents'][0]['scan_skipped'], 'symlink_or_outside_root')
            self.assertNotIn('relative_time_matches', report['key_documents'][0])


if __name__ == "__main__":
    unittest.main()
