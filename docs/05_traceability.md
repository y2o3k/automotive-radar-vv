# Requirement-to-Test Traceability

본 문서는 V0.1의 Software Requirement와 Test Case 간의 추적 관계를 정의한다.

각 Requirement가 하나 이상의 Test Case를 통해 검증되는지 확인하고,
테스트 실행 결과를 통해 요구사항의 검증 상태를 기록한다.

본 Traceability는 개인 학습 프로젝트를 위해 구성한 것으로,
실제 OEM 개발 프로세스 또는 공식 Automotive SPICE 산출물을 의미하지 않는다.


## Traceability Matrix

| Requirement ID | Requirement Summary | Test Case | Test Type | Expected Result | Test Result |
|---|---|---|---|---|---|
| REQ-FCW-001 | TTC가 2.0초 이하인 closing target에 대해 FCW ON | TC-FCW-001 | Boundary | FCW ON | PASS |
| REQ-FCW-001 | TTC가 2.0초 이하인 closing target에 대해 FCW ON | TC-FCW-002 | Boundary | FCW ON | PASS |
| REQ-FCW-002 | TTC가 2.0초를 초과하는 closing target에 대해 FCW OFF | TC-FCW-003 | Boundary | FCW OFF | PASS |
| REQ-FCW-003 | `relative_velocity`가 0 이상이면 FCW OFF | TC-FCW-004 | Equivalence | FCW OFF | PASS |
| REQ-FCW-003 | `relative_velocity`가 0 이상이면 FCW OFF | TC-FCW-005 | Equivalence | FCW OFF | PASS |
| REQ-FCW-004 | closing target의 TTC 계산 | TC-FCW-001 | Boundary | TTC = 1.9 s | PASS |
| REQ-FCW-004 | closing target의 TTC 계산 | TC-FCW-002 | Boundary | TTC = 2.0 s | PASS |
| REQ-FCW-004 | closing target의 TTC 계산 | TC-FCW-003 | Boundary | TTC = 2.1 s | PASS |
| REQ-FCW-001 | TTC가 2.0초 이하인 closing target에 대해 FCW ON | TC-FCW-006 | Scenario | FCW ON | PASS |
| REQ-FCW-004 | closing target의 TTC 계산 | TC-FCW-006 | Scenario | TTC = 1.5 s | PASS |

## Requirement Verification Summary

| Requirement ID | Verification Status |
|---|---|
| REQ-FCW-001 | PASS |
| REQ-FCW-002 | PASS |
| REQ-FCW-003 | PASS |
| REQ-FCW-004 | PASS |


## Test Execution

Test cases are defined in:

`testcases/test_cases.csv`

The FCW logic is implemented in:

`src/fcw.py`

Tests are executed using:

```bash
python3 run_tests.py
```

Execution results are stored in:

`results/test_results.csv`


## V0.1 Verification Result

V0.1의 정의된 6개 Test Case를 실행한 결과 모든 Test Case가 PASS하였다.

- Total Test Cases: 6
- PASS: 6
- FAIL: 0

현재 V0.1 범위에서 구현된 TTC 기반 FCW 판단 로직은
정의된 Software Requirement와 일치하는 동작을 확인하였다.