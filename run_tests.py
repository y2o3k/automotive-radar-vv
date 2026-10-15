"""Run the CSV test cases and return a CI-compatible exit status."""

import argparse
import csv
from pathlib import Path
import sys

from src.fcw import evaluate_fcw


ROOT = Path(__file__).resolve().parent
FIELDNAMES = [
    "test_case_id", "requirement_id", "range_m", "relative_velocity_mps",
    "expected_ttc_s", "actual_ttc_s", "expected_fcw", "actual_fcw", "result",
]


def run_tests(test_case_file, result_file):
    # Never present a previous PASS report as the result of an incomplete run.
    if test_case_file.resolve() == result_file.resolve():
        raise ValueError("The result file must not overwrite the test cases")
    result_file.unlink(missing_ok=True)
    results = []

    with test_case_file.open(newline="", encoding="utf-8") as csvfile:
        for test_case in csv.DictReader(csvfile):
            range_m = float(test_case["range_m"])
            relative_velocity_mps = float(test_case["relative_velocity_mps"])
            expected_fcw = test_case["expected_fcw"]
            expected_ttc = test_case["expected_ttc_s"]
            actual_ttc, actual_fcw = evaluate_fcw(range_m, relative_velocity_mps)

            if expected_ttc == "":
                ttc_pass = actual_ttc is None
            else:
                expected_ttc = float(expected_ttc)
                ttc_pass = actual_ttc == expected_ttc

            result = "PASS" if ttc_pass and actual_fcw == expected_fcw else "FAIL"
            print(
                test_case["test_case_id"],
                "| Expected TTC:", expected_ttc,
                "| Actual TTC:", actual_ttc,
                "| Expected FCW:", expected_fcw,
                "| Actual FCW:", actual_fcw,
                "| Result:", result,
            )
            results.append({
                "test_case_id": test_case["test_case_id"],
                "requirement_id": test_case["requirement_id"],
                "range_m": range_m,
                "relative_velocity_mps": relative_velocity_mps,
                "expected_ttc_s": expected_ttc,
                "actual_ttc_s": actual_ttc,
                "expected_fcw": expected_fcw,
                "actual_fcw": actual_fcw,
                "result": result,
            })

    if not results:
        raise ValueError("No test cases found; an empty suite is not a PASS")

    result_file.parent.mkdir(parents=True, exist_ok=True)
    with result_file.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(results)

    failures = sum(row["result"] == "FAIL" for row in results)
    print(f"\nTotal: {len(results)} | PASS: {len(results) - failures} | FAIL: {failures}")
    print("Test results saved to", result_file)
    return 1 if failures else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=Path, default=ROOT / "testcases/test_cases.csv")
    parser.add_argument("--output", type=Path, default=ROOT / "results/test_results.csv")
    args = parser.parse_args()
    try:
        return run_tests(args.cases, args.output)
    except (OSError, ValueError, KeyError, TypeError, csv.Error) as error:
        print(f"Test execution error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
