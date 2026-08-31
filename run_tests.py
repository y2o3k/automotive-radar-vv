import csv

from src.fcw import evaluate_fcw


TEST_CASE_FILE = "testcases/test_cases.csv"


with open(TEST_CASE_FILE, newline="", encoding="utf-8") as csvfile:
    test_cases = csv.DictReader(csvfile)

    for test_case in test_cases:
        test_case_id = test_case["test_case_id"]

        range_m = float(test_case["range_m"])
        relative_velocity_mps = float(test_case["relative_velocity_mps"])

        expected_fcw = test_case["expected_fcw"]
        expected_ttc = test_case["expected_ttc_s"]

        actual_ttc, actual_fcw = evaluate_fcw(
            range_m,
            relative_velocity_mps
        )

        if expected_ttc == "":
            ttc_pass = actual_ttc is None
        else:
            expected_ttc = float(expected_ttc)
            ttc_pass = actual_ttc == expected_ttc

        fcw_pass = actual_fcw == expected_fcw

        if ttc_pass and fcw_pass:
            result = "PASS"
        else:
            result = "FAIL"

        print(
            test_case_id,
            "| Expected TTC:", expected_ttc,
            "| Actual TTC:", actual_ttc,
            "| Expected FCW:", expected_fcw,
            "| Actual FCW:", actual_fcw,
            "| Result:", result
        )
