# Software Requirements

본 문서는 V0.1에서 검증할 FCW 판단 로직의 소프트웨어 요구사항을 정의한다.

각 요구사항은 고유 ID를 가지며,
향후 Test Case와 연결하여 Requirement-to-Test Traceability를 구성한다.

현재 요구사항은 개인 학습 프로젝트를 위해 정의된 Engineering Assumption과
Project Convention을 기반으로 작성되었으며,
실제 OEM 또는 법규 요구사항을 의미하지 않는다.


## REQ-FCW-001 — FCW Activation

Requirement:

If a forward target is closing and the calculated TTC is less than or equal to 2.0 seconds,
the system shall set the FCW state to ON.

Input:
- Target Range [m]
- Relative Velocity [m/s]

Output:
- FCW = ON

Source:
- ASM-001 — FCW TTC Threshold
- ASM-002 — Relative Velocity Sign Convention
- ASM-004 — Constant Relative Velocity

Verification Method:
Test


## REQ-FCW-002 — FCW Deactivation Above Threshold

Requirement:

If a forward target is closing and the calculated TTC is greater than 2.0 seconds,
the system shall set the FCW state to OFF.

Input:
- Target Range [m]
- Relative Velocity [m/s]

Output:
- FCW = OFF

Source:
- ASM-001 — FCW TTC Threshold
- ASM-002 — Relative Velocity Sign Convention
- ASM-004 — Constant Relative Velocity

Verification Method:
Test


## REQ-FCW-003 — Non-Closing Target

Requirement:

If the relative velocity is greater than or equal to 0 m/s,
the system shall set the FCW state to OFF.

Input:
- Target Range [m]
- Relative Velocity [m/s]

Output:
- FCW = OFF

Source:
- ASM-002 — Relative Velocity Sign Convention

Verification Method:
Test
