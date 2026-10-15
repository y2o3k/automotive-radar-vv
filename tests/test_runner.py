"""Verify runner exit codes and failure evidence in isolated project copies."""

import csv
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class RunnerChecks(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.project = Path(temporary.name)
        shutil.copy(ROOT / "run_tests.py", self.project)
        for directory in ("src", "testcases"):
            shutil.copytree(
                ROOT / directory, self.project / directory,
                ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
            )
        self.report = self.project / "results/report.csv"

    def execute(self, *arguments):
        return subprocess.run(
            [sys.executable, str(self.project / "run_tests.py"),
             "--output", str(self.report), *arguments],
            # Defaults must resolve relative to the script, not the caller.
            cwd=ROOT, capture_output=True, text=True, timeout=10,
        )

    def read_report(self):
        with self.report.open(newline="", encoding="utf-8") as report:
            return list(csv.DictReader(report))

    def test_normal_suite_returns_zero_and_writes_report(self):
        process = self.execute()
        self.assertEqual(process.returncode, 0, process.stdout + process.stderr)
        rows = self.read_report()
        self.assertEqual(len(rows), 6)
        self.assertTrue(all(row["result"] == "PASS" for row in rows))

    def test_boundary_defect_returns_one_and_preserves_failed_evidence(self):
        source = self.project / "src/fcw.py"
        original = source.read_text(encoding="utf-8")
        condition = "ttc_s <= FCW_TTC_THRESHOLD_S"
        self.assertEqual(original.count(condition), 1, "Update the mutation when FCW changes")
        source.write_text(
            original.replace(condition, "ttc_s < FCW_TTC_THRESHOLD_S"),
            encoding="utf-8",
        )
        process = self.execute()
        self.assertEqual(process.returncode, 1, process.stdout + process.stderr)
        failed = [row for row in self.read_report() if row["result"] == "FAIL"]
        self.assertEqual([row["test_case_id"] for row in failed], ["TC-FCW-002"])
        self.assertEqual(failed[0]["expected_fcw"], "ON")
        self.assertEqual(failed[0]["actual_fcw"], "OFF")

    def test_empty_suite_returns_two_without_stale_report(self):
        self.assertEqual(self.execute().returncode, 0)
        cases = self.project / "testcases/test_cases.csv"
        cases.write_text(cases.read_text().splitlines()[0] + "\n", encoding="utf-8")
        process = self.execute()
        self.assertEqual(process.returncode, 2)
        self.assertIn("No test cases", process.stderr)
        self.assertFalse(self.report.exists())

    def test_invalid_number_returns_two_without_stale_report(self):
        self.assertEqual(self.execute().returncode, 0)
        cases = self.project / "testcases/test_cases.csv"
        cases.write_text(cases.read_text().replace("19.0", "not-a-number", 1))
        process = self.execute()
        self.assertEqual(process.returncode, 2)
        self.assertIn("Test execution error", process.stderr)
        self.assertFalse(self.report.exists())


if __name__ == "__main__":
    unittest.main()
