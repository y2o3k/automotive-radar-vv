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
Negative relative velocity indicates a closing target.

Examples:
- -10 m/s : target is approaching
- 0 m/s   : no relative longitudinal movement
- +10 m/s : target is moving away

Classification:
Project Convention

Purpose:
TTC 계산 및 테스트 입력값을 일관된 방식으로 정의하기 위해 사용한다.

External Requirement:
No


## ASM-003 — Single Target Model

Assumption:
V0.1에서는 하나의 전방 target만 존재한다고 가정한다.

Classification:
Scope Assumption

Purpose:
초기 프로토타입에서는 TTC 계산과 FCW 경계조건 검증에 집중하고,
multi-target tracking 및 object selection 문제는 제외하기 위함이다.

External Requirement:
No


## ASM-004 — Constant Relative Velocity

Assumption:
TTC 계산 시 target과 ego vehicle의 상대속도는 계산 구간 동안 일정하다고 가정한다.

Classification:
Model Assumption

Purpose:
V0.1에서 TTC 계산을 단순화하고
FCW 판단 로직 검증에 집중하기 위함이다.

External Requirement:
No
