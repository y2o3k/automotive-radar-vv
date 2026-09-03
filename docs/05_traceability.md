# Requirement-to-Test Traceability

본 문서는 V0.1 및 V0.2의 Software Requirement와 Test Case 간의 추적 관계를 정의한다.

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
| REQ-RUN-001 | 모든 Test Case가 PASS이면 프로세스 종료 코드 0 | TC-RUN-001 | Positive | Process Exit Code = 0 | PASS |
| REQ-RUN-002 | 하나 이상의 Test Case가 FAIL이면 프로세스 종료 코드 1 | TC-RUN-002 | Negative (Mutation) | Process Exit Code = 1 | PASS |

## Requirement Verification Summary

| Requirement ID | Verification Status |
|---|---|
| REQ-FCW-001 | PASS |
| REQ-FCW-002 | PASS |
| REQ-FCW-003 | PASS |
| REQ-FCW-004 | PASS |
| REQ-RUN-001 | PASS |
| REQ-RUN-002 | PASS |

## Test Execution
FCW Test Case는 다음 파일에 정의한다.

`testcases/test_cases.csv`

Test Runner 종료 코드 Test Case는 다음 파일에 정의한다.

`testcases/runner_test_cases.md`

FCW 판단 로직은 다음 파일에 구현한다.

`src/fcw.py`

Test Runner는 다음 파일에 구현한다.

`run_tests.py`

테스트와 종료 코드는 다음 명령으로 확인한다.

```bash
python3 run_tests.py
echo $?
```
FCW Test Case 실행 결과는 다음 파일에 저장한다.

`results/test_results.csv`

Test Runner 종료 코드 실행 결과는
`testcases/runner_test_cases.md`의 `Actual Result`와 `Status`에 기록한다.

## V0.1 Verification Result

V0.1의 정의된 6개 Test Case를 실행한 결과 모든 Test Case가 PASS하였다.

- Total Test Cases: 6
- PASS: 6
- FAIL: 0

현재 V0.1 범위에서 구현된 TTC 기반 FCW 판단 로직은
정의된 Software Requirement와 일치하는 동작을 확인하였다.

## V0.2 Test Runner Exit Code Verification Result

V0.2에서 추가한 Test Runner 종료 코드 Test Case를 실행한 결과,
TC-RUN-001과 TC-RUN-002가 모두 PASS하였다.

- TC-RUN-001: 6개 FCW Test Case PASS, Process Exit Code 0
- TC-RUN-002: MUT-001 적용 시 `TC-FCW-002` FAIL, Process Exit Code 1
- MUT-001: Detected
- Mutation 복원 후 Regression Test: 6개 Test Case PASS, Process Exit Code 0

구현 전에는 Test Case가 FAIL해도 종료 코드 0이 반환되었으나,
V0.2 구현 후에는 하나 이상의 Test Case가 FAIL하면 종료 코드 1이 반환됨을 확인하였다.

따라서 REQ-RUN-001과 REQ-RUN-002가 정의된 Expected Result와
일치하는 동작을 확인하였다.

MUT-001은 Test Case와 Test Runner의 검출력을 확인하기 위한 의도적인 변경이며,
실제 프로젝트 결함을 의미하지 않는다.
