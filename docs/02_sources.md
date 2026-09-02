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


## SRC-004 — Python `sys.exit()`

Organization:

Python Software Foundation

Document:

Python 3.9 Standard Library — `sys.exit()`

Purpose:

Python 프로그램이 실행 결과를 종료 코드로 전달하는 방법을 이해하기 위한 참고 자료.

Python 공식 문서에서는 종료 코드 0을 정상 종료로 보고,
0이 아닌 값을 비정상 종료 상태로 설명한다.

Used For:

- 모든 Test Case가 PASS한 경우 정상 종료 상태 전달
- 하나 이상의 Test Case가 FAIL한 경우 비정상 종료 상태 전달
- 향후 Test Automation 환경에서 테스트 성공과 실패 판정

Note:

Python 공식 문서는 종료 코드의 기본 의미를 제공한다.

본 프로젝트에서 모든 Test Case가 PASS하면 종료 코드 0,
하나 이상의 Test Case가 FAIL하면 종료 코드 1을 사용한다는 구체적인 기준은
별도의 Project Convention으로 정의한다.

Official Reference:

https://docs.python.org/3.9/library/sys.html#sys.exit







