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
            root.joinpath(".obsidian").mkdir()
            result = self.run_inventory(root)
            self.assertEqual(result.returncode, 3)
            self.assertIn("dedicated knowledge-management workflow", result.stderr)


if __name__ == "__main__":
    unittest.main()
