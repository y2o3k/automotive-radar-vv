
# Automotive Radar V&V

TTC(Time-To-Collision) 기반 FCW 판단 로직을 대상으로
요구사항 정의, 테스트 설계, 구현, 실행 결과 및 Traceability를 구성한 개인 학습 프로젝트입니다.

## 시각화 SIL 및 CI 리뷰 안내

시각화 실습과 기존 CI를 함께 확인할 리뷰 브랜치는 `codex/fcw-visual-sil`입니다. 이 브랜치는 `codex/fcw-ci`의 변경을 포함합니다. PR 병합 전에는 `main`의 파일과 다릅니다.

```sh
python3 sil/server.py
```

Python 3.9 이상과 C 컴파일러 `cc`가 필요합니다. 실행 후 http://127.0.0.1:8765 를 엽니다. [SIL 실행 구조와 실습 안내](sil/README.md), [CI 학습 안내](docs/06_ci_learning.md)를 참고하세요.

이 구현의 기준은 [V0.1 학습용 요구사항](docs/04_requirements.md)입니다. 20 ms는 시나리오의 가상 시간 간격이며 실시간 ECU 실행 주기가 아닙니다. 경고는 TTC 조건에 따라 즉시 결정됩니다. 고객 사양 v1.0 원문은 이 브랜치에 없으며, 50 ms 실행 주기·0.3초 진입 대기·1초 해제 지연·타깃 소실 처리는 구현 또는 적합성 확인 전입니다.

알려진 검토 항목: 기존 Python 러너는 TTC를 `==`로 비교하고, 시각화 SIL의 CSV 판정은 `math.isclose`로 비교합니다. 수치 허용오차를 요구사항으로 정한 뒤 두 판정 기준을 정리해야 합니다. 현재 테스트 통과가 모든 수치 입력에 대한 정확성을 보장하지는 않습니다.

## V0.1 검증 범위

V0.1에서는 다음 조건을 검증합니다.

- Closing target에 대한 TTC 계산
- TTC 2.0 s 기준 FCW ON/OFF 판단
- TTC boundary 검증: 1.9 / 2.0 / 2.1 s
- Non-closing target 처리
- High closing speed 조건 추가 검증

## Logic

```text
relative_velocity >= 0
        |
        +----> FCW OFF

relative_velocity < 0
        |
        v
closing_speed = -relative_velocity
        |
        v
TTC = target_range / closing_speed
        |
        v
TTC <= 2.0 s ?
   |          |
  YES         NO
   |          |
FCW ON      FCW OFF
```

## Project Structure
```text
docs/
  01_project_scope.md
  02_sources.md
  03_assumptions.md
  04_requirements.md
  05_traceability.md

src/
  fcw.py

testcases/
  test_cases.csv

results/
  test_results.csv

run_tests.py

tests/
  test_runner.py

.github/workflows/
  fcw-ci.yml
```

## Test Execution
```bash
python3 run_tests.py
python3 -m unittest discover -s tests -v
```

## Continuous Integration (CI)

GitHub의 **Actions → FCW validation**에서 자동 시험을 확인할 수 있습니다.
코드 push 및 Pull Request 생성·갱신 시 기존 FCW 6개 시험과 실행기 검증을 수행합니다.
기본 브랜치에 반영한 뒤에는 Actions 화면의 **Run workflow**로도 실행할 수 있습니다.

- 종료 코드 `0`: 시험을 실행했고 모두 PASS
- 종료 코드 `1`: 하나 이상의 시험이 FAIL
- 종료 코드 `2`: 빈 시험 목록 또는 입력 파일 오류 등으로 시험을 정상 실행하지 못함
- 실행 중 예외가 발생해도 성공으로 처리하지 않습니다.

실패한 실행에서도 **Artifacts → fcw-test-evidence**에 CSV 결과(생성된 경우)와
실행기 검증 로그를 14일 보관합니다. 현재 실행의 결과는 이 파일과 Actions 로그로 확인합니다.
기존 `results/test_results.csv`와 아래 V0.1 결과는 수동 실행 시점의 기록입니다.

로컬에서 CI와 같은 위치에 결과를 만들려면:

```bash
python3 run_tests.py --output results/ci/test_results.csv
```

첫 실습과 실패 검출 원리는 [CI 학습 가이드](docs/06_ci_learning.md)를 참고하세요.
이 단계는 Python 기반 기능 검증의 CI 실습이며, RTOS·HIL 검증 또는 차량 배포(CD)는 포함하지 않습니다.

## V0.1 Result
Test Cases: 6
PASS: 6
FAIL: 0

Detailed execution results are available in:

results/test_results.csv

Requirement-to-Test relationships are documented in:

docs/05_traceability.md

## Current Limitations 
V0.1 uses Target Range and Relative Velocity as inputs.

The following are not included in the current scope:

Ego / Target absolute velocity input
Acceleration or deceleration
Multiple target selection
Sensor measurement noise
Real radar data
Vehicle or simulation environment integration
