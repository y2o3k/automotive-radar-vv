# Engineering Assumptions

본 문서는 프로젝트에서 사용하는 Engineering Assumption을 관리하기 위한 문서이다.

외부 표준 또는 공개 시험 프로토콜에서 직접 정의된 요구사항과,
개인 프로젝트의 검증 목적을 위해 임의로 설정한 조건을 구분하여 관리한다.

본 문서에 정의된 값은 실제 OEM 사양, 양산 차량 사양 또는 법규 요구사항을 의미하지 않는다.


## ASM-001 — FCW TTC Threshold

Assumption:
FCW activation threshold = 2.0 s

Classification:
Engineering Assumption

Purpose:
TTC 기반 FCW 판단 로직의 Boundary Value Analysis를 수행하기 위해 설정하였다.

Reason:
threshold 바로 아래, 동일, 바로 위의 조건을 이용하여
경계조건에서 소프트웨어가 요구사항대로 동작하는지 검증하기 위함이다.

Planned Test Conditions:
- TTC = 1.9 s
- TTC = 2.0 s
- TTC = 2.1 s

External Requirement:
No

Note:
2.0 s 값은 Euro NCAP, ISO 또는 특정 OEM 요구사항에서 직접 가져온 값이 아니다.


## ASM-002 — Relative Velocity Sign Convention

Assumption:

Relative velocity is defined as:

relative_velocity = target_velocity - ego_velocity

Therefore:

relative_velocity < 0: distance between ego and target is decreasing
relative_velocity = 0: relative distance remains constant
relative_velocity > 0: distance between ego and target is increasing

For TTC calculation, a closing condition is considered only when:

relative_velocity < 0

and the closing speed is defined as:

closing_speed = -relative_velocity

Example:

Ego velocity    = 20 m/s
Target velocity = 10 m/s

Relative velocity = 10 - 20 = -10 m/s
Closing speed     = 10 m/s

This means the distance between the ego vehicle and the target decreases by 10 m every second.

Classification: Project Convention

Purpose: TTC 계산 및 테스트 입력값의 상대속도 부호 기준을 일관되게 정의하기 위해 사용한다.

External Requirement: No


## ASM-003 — Single Target Model

Assumption:

The V0.1 verification scope considers only one target vehicle located in front of the ego vehicle.

The target vehicle is assumed to be the object used directly for TTC calculation and FCW decision.

Multiple-target scenarios and target selection logic are outside the scope of V0.1.

Classification: Project Scope Assumption

Purpose: 복수 객체 선택이나 타깃 추적 로직을 제외하고 TTC 기반 FCW 경계 검증에 집중하기 위해 사용한다.

External Requirement: No



## ASM-004 — Constant Relative Velocity

Assumption:

V0.1에서는 TTC 계산 시 차량 간 상대속도가 일정하다고 가정한다.

차량의 가속 및 감속은 고려하지 않으며,
현재 Target Range와 Closing Speed를 사용하여 TTC를 계산한다.

Classification:

Engineering Assumption

Purpose:

가속 및 감속에 따른 시간 변화 모델을 제외하고,
현재 거리와 상대속도를 이용한 단순 TTC 계산에 집중하기 위해 설정하였다.

External Requirement:

No

Note:

본 가정은 V0.1의 단순화된 TTC 계산 모델을 위해 정의한
프로젝트 내부 가정이며, 실제 OEM 또는 법규 요구사항을 의미하지 않는다.
