
# Automotive Radar V&V

TTC(Time-To-Collision) 기반 FCW 판단 로직을 대상으로
요구사항 정의, 테스트 설계, 구현, 실행 결과 및 Traceability를 구성한 개인 학습 프로젝트입니다.

## V0.1 Scope

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

## Project Structure
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

## Test Execution
python3 run_tests.py

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