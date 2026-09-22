from __future__ import annotations

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ValidatorGrowthGateRegressionTest(unittest.TestCase):
    def run_validator_in_copy(self, mutate_growth=None):
        with tempfile.TemporaryDirectory() as temp_dir:
            checkout = Path(temp_dir) / "repo"
            shutil.copytree(
                ROOT,
                checkout,
                ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"),
            )

            growth_path = checkout / ".github" / "workflows" / "growth-loop.yml"
            if mutate_growth is not None:
                growth = growth_path.read_text(encoding="utf-8")
                growth_path.write_text(mutate_growth(growth), encoding="utf-8")

            return subprocess.run(
                [sys.executable, str(checkout / ".ami" / "validate.py")],
                cwd=checkout,
                capture_output=True,
                text=True,
                check=False,
            )

    def test_current_repository_contract_passes(self):
        result = self.run_validator_in_copy()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("growth_ingress_contract=PASS", result.stdout)

    def test_broken_growth_enable_gate_fails_closed(self):
        reviewed_gate = '[ "$AMI_GROWTH_INGRESS_ENABLED" != "true" ]'
        broken_gate = '[ "$AMI_GROWTH_INGRESS_ENABLED" != "not-reviewed" ]'

        def break_gate(growth):
            self.assertIn(reviewed_gate, growth)
            return growth.replace(reviewed_gate, broken_gate, 1)

        result = self.run_validator_in_copy(break_gate)
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(
            "growth workflow missing exact opt-in comparison",
            result.stdout,
        )
        self.assertNotIn("AMI repository contract: PASS", result.stdout)


if __name__ == "__main__":
    unittest.main()
