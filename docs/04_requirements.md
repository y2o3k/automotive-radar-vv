# Software Requirements

본 문서는 프로젝트에서 검증할 FCW 판단 로직과 Test Runner의 소프트웨어 요구사항을 정의한다.

v0.1에서 정의한 FCW 요구사항을 기준선으로 유지하며, 
v0.2에서는 Test Runner와 차량 시나리오 관련 요구사항을 단계적으로 추가한다. 

각 요구사항은 고유 ID를 가지며,
향후 Test Case와 연결하여 Requirement-to-Test Traceability를 구성한다.

현재 요구사항은 개인 학습 프로젝트를 위해 정의된 Engineering Assumption과
Project Convention을 기반으로 작성되었으며,
실제 OEM 또는 법규 요구사항을 의미하지 않는다.


## REQ-FCW-001 — FCW 활성화(Activation)
Requirement:

전방 타깃의 relative_velocity < 0 m/s이고 계산된 TTC가 2.0초 이하인 경우,
시스템은 FCW 상태를 ON으로 설정해야 한다.

Input:
Target Range [m]
Relative Velocity [m/s]

Output: FCW State = ON

Source:
ASM-001 — FCW TTC Threshold
ASM-002 — Relative Velocity Sign Convention
ASM-003 — Single Target Assumption
ASM-004 — Constant Relative Velocity Assumption

Verification Method: Test

## REQ-FCW-002 — FCW 비활성화: TTC 임계값 초과 (Deactivation Above Threshold)
전방 타깃의 relative_velocity < 0 m/s이고 계산된 TTC가 2.0초를 초과하는 경우,
시스템은 FCW 상태를 OFF로 설정해야 한다.

Input:
Target Range [m]
Relative Velocity [m/s]

Output: FCW State = OFF

Source:
ASM-001 — FCW TTC Threshold
ASM-002 — Relative Velocity Sign Convention
ASM-003 — Single Target Assumption
ASM-004 — Constant Relative Velocity Assumption

Verification Method: Test


## REQ-FCW-003 — 비접근 타깃 처리(Non-Closing Target)

Requirement:

relative_velocity >= 0 m/s인 경우,
시스템은 FCW 상태를 OFF로 설정해야 한다.

Input:
Target Range [m]
Relative Velocity [m/s]

Output: FCW State = OFF

Source:
ASM-002 — Relative Velocity Sign Convention
ASM-003 — Single Target Assumption

Verification Method: Test

## REQ-FCW-004 — TTC 계산

Requirement:

전방 타깃의 relative_velocity < 0 m/s인 경우,
시스템은 다음 식을 사용하여 closing_speed를 계산해야 한다.

closing_speed = -relative_velocity

시스템은 계산된 closing_speed와 target_range를 사용하여 TTC를 다음과 같이 계산해야 한다.

TTC = target_range / closing_speed

Input:
Target Range [m]
Relative Velocity [m/s]

Output: TTC [s]

Source:
ASM-002 — Relative Velocity Sign Convention
ASM-004 — Constant Relative Velocity Assumption

Verification Method: Test

## REQ-RUN-001 — 모든 테스트 통과 시 정상 종료

Requirement: 
테스트 러너가 정의된 모든 Test Case의 실행을 완료하고 
모든 Test Case 결과가 PASS인 경우, 테스트 러너는 프로세스 종료 코드 0으로 실행을 종료해야 한다. 

Input: 개별 Test Case 실행 결과

Output: Process Exit Code = 0

Source:
- SRC-004 — Python `sys.exit()`
- ASM-005 — 테스트 러너 종료 코드 규칙

Verification Method: Test

## REQ-RUN-002 — 테스트 실패 발생 시 비정상 종료
Requirement: 

테스트 러너가 정의된 모든 Test Case의 실행을 완료하고 
하나 이상의 Test Case 결과가 FAIL인 경우, 테스트 러너는 프로세스 종료 코드 1로 실행을 종료해야한다.

Input: 개별 Test Case 실행 결과

Output: Process Exit Code = 1

Source:
- SRC-004 — Python `sys.exit()`
- ASM-005 — 테스트 러너 종료 코드 규칙

Verification Method: Test


