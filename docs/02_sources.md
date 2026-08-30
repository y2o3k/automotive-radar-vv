# Sources 
본 프로젝트에서는 공개된 자동차 시험 프로토콜 및 소프트웨어 검증 관련 자료를 참고한다. 
외부 자료에서 직접 가져온 내용과 개인프로젝트를 위해 정의한 Engineering Assumption을 구분하여 관리한다. 

## SRC-001 — Euro NCAP AEB Car-to-Car Test Protocol

Organization:
Euro NCAP

Document:
AEB Car-to-Car Test Protocol v4.3.1

Purpose:
FCW/AEB 기능 및 차량 간 충돌 시나리오와 TTC(Time To Collision) 개념을 이해하기 위한 참고 자료.

Used For:
- TTC 개념 이해
- Car-to-Car test scenario 이해
- 향후 scenario-based verification 설계 참고

Note:
본 프로젝트 V0.1에서 사용하는 FCW TTC threshold 2.0 s는
Euro NCAP 요구사항에서 직접 가져온 값이 아니라 개인 프로젝트용 Engineering Assumption이다.

Official Reference:
https://cdn.euroncap.com/cars/assets/euro_ncap_aeb_c2c_test_protocol_v431_532926aad1.pdf

Protocol Index:
https://www.euroncap.com/safety-assist/

## SRC-002 — Automotive SPICE 4.0

Organization:
VDA QMC

Document:
Automotive SPICE Process Assessment Model 4.0

Purpose:
자동차 소프트웨어 개발에서 요구사항과 검증 활동 사이의 추적성 및 검증 프로세스를 이해하기 위한 참고 자료.

Used For:
- Requirement 기반 Verification 설계
- Requirement ↔ Test Case Traceability
- Boundary / Negative / Fault Test 설계 개념
- Test Result 및 Evidence 관리

Official Reference:
https://webshop.vda.de/QMC/en/publications

## SRC-003 — ISO 34505:2025

Organization:
ISO

Document:
ISO 34505:2025
Road vehicles — Test scenarios for automated driving systems —
Scenario evaluation and test case generation

Purpose:
Scenario를 Test Case로 확장하는 과정과 Test Case 구성 요소를 이해하기 위한 참고 자료.

Used For:
- Test Case ID
- Test Objective
- Test Input
- Test Procedure
- Expected Result
- Test Result
- 향후 Scenario-based Verification 구조 설계

Note:
본 프로젝트는 ISO 34505 인증 또는 규격 적합성을 주장하지 않으며,
공개된 표준의 개념을 개인 학습 프로젝트의 검증 구조 설계에 참고한다.

Official Reference:
https://www.iso.org/standard/78954.html
