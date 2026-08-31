# Software Requirements

본 문서는 V0.1에서 검증할 FCW 판단 로직의 소프트웨어 요구사항을 정의한다.

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

Output:

FCW State = ON

Source:

ASM-001 — FCW TTC Threshold
ASM-002 — Relative Velocity Sign Convention
ASM-003 — Single Target Assumption
ASM-004 — Constant Relative Velocity Assumption

Verification Method:

Test

## REQ-FCW-002 — FCW 비활성화: TTC 임계값 초과 (Deactivation Above Threshold)
전방 타깃의 relative_velocity < 0 m/s이고 계산된 TTC가 2.0초를 초과하는 경우,
시스템은 FCW 상태를 OFF로 설정해야 한다.

Input:

Target Range [m]
Relative Velocity [m/s]

Output:

FCW State = OFF

Source:

ASM-001 — FCW TTC Threshold
ASM-002 — Relative Velocity Sign Convention
ASM-003 — Single Target Assumption
ASM-004 — Constant Relative Velocity Assumption

Verification Method:

Test


## REQ-FCW-003 — 비접근 타깃 처리(Non-Closing Target)

Requirement:

relative_velocity >= 0 m/s인 경우,
시스템은 FCW 상태를 OFF로 설정해야 한다.

Input:

Target Range [m]
Relative Velocity [m/s]

Output:

FCW State = OFF

Source:

ASM-002 — Relative Velocity Sign Convention
ASM-003 — Single Target Assumption

Verification Method:

Test

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

Output:

TTC [s]

Source:

ASM-002 — Relative Velocity Sign Convention
ASM-004 — Constant Relative Velocity Assumption

Verification Method:

Test


