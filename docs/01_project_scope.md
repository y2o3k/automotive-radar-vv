
# Project Scope

## 1. Project Purpose

요구사항 기반의 소프트웨어 검증 절차와 Python 기반 테스트 자동화 과정을 직접 설계하고 구현해보며, 이해하기 위해 본 프로젝트를 시작하였다.

본 프로젝트의 목적은 단순히 FCW 기능을 구현하는 것이 아니라,

- 요구사항 정의
- 테스트 케이스 설계
- Expected / Actual 비교
- 결함 검출
- Regression Test

까지 이어지는 검증 프로세스를 직접 구성하는 것이다.


## 2. Verification Target

V0.1에서는 전방 객체의 거리와 상대속도를 입력으로 받아
TTC(Time To Collision)를 계산하고,
설정된 기준에 따라 FCW 상태를 판단하는 간단한 소프트웨어 로직을 검증한다.


## 3. Inputs

- Target Range [m]
- Relative Velocity [m/s]


## 4. Outputs

- FCW ON
- FCW OFF


## 5. V0.1 Verification Question

접근 중인 전방 객체의 TTC가 설정된 threshold의 경계값에 있을 때,
FCW 판단 로직이 정의된 요구사항대로 동작하는가?


## 6. Out of Scope

현재 V0.1에서는 아래 항목은 포함하지 않는다.

- 실제 차량 및 실제 Radar Sensor
- FMCW Radar Signal Processing
- Range FFT / Doppler FFT / CFAR
- 실제 ECU
- CAN / UDS 통신
- 실제 OEM FCW Calibration
- AEB Brake Control
- SIL / HIL 환경
- ISO 26262 인증 또는 규격 적합성 주장


## 7. Future Expansion

향후 프로젝트를 다음과 같이 단계적으로 확장할 예정이다.

- Radar Detection Verification
- Fault Injection
- Scenario-based Testing
- Test Automation
- Radar Detection과 FCW 기능의 Interface Integration
- CAN / UDS 기반 검증
- SIL / HIL 기반 검증
