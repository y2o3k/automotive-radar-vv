import csv
# csv 모듈을 import하여 CSV 파일을 읽고 쓰기 위해 사용
import os
# 결과 파일을 저장할 results 폴더를 생성하기 위해 os를 import
import sys
# 테스트 실행 결과를 프로세스 종료 코드로 전달하기 위해 사용

from src.fcw import evaluate_fcw
# evaluate_fcw 함수를 import하여 테스트 케이스를 평가하는 데 사용


TEST_CASE_FILE = "testcases/test_cases.csv" #TEST_CASE_FILE을 내부에서 만날때마다 testcases/test_cases.csv로 이해하여 경로를 지정
RESULT_FILE = "results/test_results.csv"
# 테스트 케이스 파일과 결과 파일의 경로를 지정

#results 폴더가 없으면 생성하고, 결과를 저장할 리스트를 초기화
os.makedirs("results", exist_ok=True)
results = []
failed_test_count = 0
#실행 중 FAIL로 판정된 Test Case의 개수를 저장
#반복문 밖에 있어야 전체 6개 Test Case의 실패 개수가 누적됨.

#test_results.csv라는 파일 자체는 open()이 만들어주지만, results라는 폴더가 없으면 에러가 발생하기 때문에 os.makedirs()를 사용하여 results 폴더를 생성
#exist_ok=True를 지정하면 이미 폴더가 존재해도 에러가 발생하지 않음 -> Test Runner를 여러 번 실행해도 results 폴더가 이미 존재하면 에러 없이 계속 진행됨

#open() 함수를 사용하여 test_cases.csv 파일을 읽기 모드로 열고, csv.DictReader를 사용하여 각 행을 딕셔너리로 읽어옴
#with 구문을 사용하여 파일을 열면, 블록이 끝나면 자동으로 파일이 닫힘
#as csvfile: csvfile이라는 이름으로 파일 객체를 참조 (열린 파일을 csvfile이라는 이름을 사용하겠다는 뜻)
with open(TEST_CASE_FILE, newline="", encoding="utf-8") as csvfile:
    test_cases = csv.DictReader(csvfile) #dictReader를 사용하여 CSV 파일을 읽어옴. 각 행은 딕셔너리로 반환되며, 첫 번째 행은 키(컬럼명)로 사용됨

    for test_case in test_cases: #test_cases안에 있는 데이터를 한 줄씩 가져와서 test case 라는 이름으로 반복해서 처리.
        test_case_id = test_case["test_case_id"]
        requirement_id = test_case["requirement_id"]

        range_m = float(test_case["range_m"]) #csv에서 읽은 값이 기본적으로 문자열이므로 float() 함수를 사용하여 실수로 변환 (ttc 계산을 하려면 숫자여야함.)
        relative_velocity_mps = float(test_case["relative_velocity_mps"]) #csv에서 읽은 값이 기본적으로 문자열이므로 float() 함수를 사용하여 실수로 변환

        expected_fcw = test_case["expected_fcw"]
        expected_ttc = test_case["expected_ttc_s"]

        #실제 검증 대상 실행
        #evaluate_fcw 함수는 range_m과 relative_velocity_mps를 인자로 받아서 실제 TTC와 FCW 상태를 계산
        #함수가 두값을 돌려주었고, 두변 수에 각각 할당
        actual_ttc, actual_fcw = evaluate_fcw(
            range_m,
            relative_velocity_mps
        )

        if expected_ttc == "":
            ttc_pass = actual_ttc is None #여기서의 None은 값이 0이 아닌 TTC를 계산되지 않는다 라는 의미임.
        else:
            expected_ttc = float(expected_ttc)
            ttc_pass = actual_ttc == expected_ttc

        fcw_pass = actual_fcw == expected_fcw

        if ttc_pass and fcw_pass: #and 연산자를 사용하여 두 조건이 모두 참일 때만 PASS로 판단
            result = "PASS"
        else:
            result = "FAIL"
            failed_test_count += 1 #실패한 Test Case의 개수를 누적
        #콘솔 출력
        print(
            test_case_id,
            "| Expected TTC:", expected_ttc,
            "| Actual TTC:", actual_ttc,
            "| Expected FCW:", expected_fcw,
            "| Actual FCW:", actual_fcw,
            "| Result:", result
        )

        results.append({
            "test_case_id": test_case_id,
            "requirement_id": requirement_id,
            "range_m": range_m,
            "relative_velocity_mps": relative_velocity_mps,
            "expected_ttc_s": expected_ttc,
            "actual_ttc_s": actual_ttc,
            "expected_fcw": expected_fcw,
            "actual_fcw": actual_fcw,
            "result": result
        })

#결과 파일 열기
#w는 쓰기모드로 열기
with open(RESULT_FILE, "w", newline="", encoding="utf-8") as csvfile:
    #fieldnames 리스트를 정의하여 CSV 파일의 열 이름을 지정(csv의 헤더 정의)
    fieldnames = [
        "test_case_id",
        "requirement_id",
        "range_m",
        "relative_velocity_mps",
        "expected_ttc_s",
        "actual_ttc_s",
        "expected_fcw",
        "actual_fcw",
        "result"
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results) #results 리스트에 있는 모든 딕셔너리 데이터를 한 줄씩 CSV 파일에 씀


print()
print("Test results saved to", RESULT_FILE)

# 모든 Test Case 실행과 결과 파일 저장이 끝난 후 최종 종료 코드를 결정
if failed_test_count == 0:
    sys.exit(0)
else:
    sys.exit(1)
