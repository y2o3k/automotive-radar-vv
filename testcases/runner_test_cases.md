# Test Runner Exit Code Test Cases 
본 문서는 V0.2에서 추가하는 Test Runner 종료 코드 요구사항을 검증하기 위한 Test Case를 정의한다. 

현재 Test Case는 설계만 완료된 상태이며, 코드 구현 및 실행 전까지 상태를 Planned로 관리한다. 
 
## TC-RUN-001 - 모든 테스트 통과 시 종료 코드 확인 
Related Requirement: 
REQ-RUN-001 - 모든 테스트 통과시 정상 종료

Test TYPE:
Positive Test
Objective: 모든 Test Case가 PASS인 경우 , 
Test Runner가 프로세스 종료 코드 0으로 실행을 종료하는지 확인한다. 

Precondition: 
- 터미널의 현재 위치가 `automotive-radar-vv` 저장소의 최상위 폴더인 상태
- `src/fcw.py`에 의도적인 Mutation이 적용되지 않은 상태
- `testcases/test_cases.csv`에 정의된 6개 Test Case 사용
- Test Runner가 실행 중 예외 없이 모든 Test Case를 완료할 수 있는 상태

Test Procedure: 
1. 터미널에서 python3 run_tests.py를 실행한다.
2. 6개 Test Case가 모두 PASS인지 확인한다.
3. 같은 터미널에서 즉시 `echo $?`를 실행한다.
4. 출력된 프로세스 종료 코드를 확인한다.

Expected Result: 
- 6개 Test Case가 모두 PASS
- Process Exit Code: 0

Actual Result: Not Executed
Status: Planned

## TC-RUN-002 - 테스트 실패 발생 시 종료 코드 확인
Related Requirment:
REQ-RUN-002 - 테스트 실패 발생 시 비정상 종료 

Test Type:  Negative Test
Failure Injection Method: Mutation Test

Objective: 하나 이상의 Test Case 결과가 FAIL인 경우, 
Test Runner가 프로세스 종료 코드 1로 실행을 종료하는지 확인한다. 

Mutation Condition: 
Mut-001 - FCW TTC 경계 연산자 변경 

원본조건: ttc_s <= FCW_TTC_THRESHOLD_S
변경조건: ttc_s < FCW_TTC_THRESHOLD_S

MUT-001은 테스트 검출력을 확인하기 위한 의도적인 변경이며, 실제 프로젝트 결함을 의미하지는 않는다. 

Precondition:
- 터미널의 현재 위치가 `automotive-radar-vv` 저장소의 최상위 폴더인 상태
- `testcases/test_cases.csv`에 정의된 6개 Test Case 사용
- MUT-001이 테스트 실행 중에만 임시로 적용된 상태
- Mutation이 GitHub에 커밋되지 않은 상태

Test Procedure:
1. 로컬 환경에서 MUT-001을 임시로 적용한다.
2. 터미널에서 `python3 run_tests.py`를 실행한다.
3. `TC-FCW-002`가 FAIL인지 확인한다.
4. 같은 터미널에서 즉시 `echo $?`를 실행한다.
5. 출력된 프로세스 종료 코드를 확인한다.
6. 테스트가 끝나면 원래 조건인 `<=`로 복원한다.

Expected Result:
- `TC-FCW-002`: FAIL
- 나머지 5개 Test Case: PASS
- Process Exit Code: 1
- MUT-001: Detected

Postcondition:
- `src/fcw.py`의 경계 연산자가 원래 조건인 `<=`로 복원된 상태
- 원본 코드를 다시 실행했을 때 6개 Test Case가 모두 PASS한 상태


Actual Result: Not Executed
Status: Planned (아직 코드를 구현하거나 실제 실행하지 않았기 떄문 , 계횐된 시험과 실행 완료된 시험을 구분해야함) 


