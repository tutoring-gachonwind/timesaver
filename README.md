### 프로그램 명: timesaver
(tutoring 2024-1 / 김동욱 튜티) 할 일에 제한 시간을 부여하여 태스크를 효율적으로 관리하는 인터페이스 


---
## 개발 기간: 3주



---
####개발 단계
1.  ui를 pyqt5 designer를 통해 디자인
2.  ui의 파일과 파이썬 코드를 연결
3.  프로그레스 바 구현
4. 입력 받은 후 정보를 각 table에 전달하는 코드 작성
5. 타이머 기능 구현
6. 타이머 기능과 프로그레스 바를 연결
7. 중지/재생 qpushbutton 구현+ 타이머 기능에 중지 기능 추가




------
###디렉토리 구조
-timesaver_python_file.py
-timesaver.ui

------
###개발 라이브러리
1. PYQT5
2. QTHREAD


--------------
###PESEUDO CODE

UI 필요한 목록: 시간 입력 창, 현재 업무 표시 테이블, QPUSHBUTTON, PROGRESS BAR, 
PYTHON:
1. UI IMPORT, CONNECT SIGNAL
   -PROGRESS BAR
   -QPUSHBUTTON
   -TEXTBROWSER
2. QTHREAD로 타이머 구현
3. QPUSHBUTTON_STOPANDGO 버튼 조건에 따라  변화 


-----------
###작동방식
1. 시간과 업무를 작성 한 후 입력 버튼 클릭
2.  타이머가 호출되고 프로그레스 바가 진행, 현재 업무가 표시 됨
3.  프로그레스 바가 100%에 도달하는 동시에 타이머가 종료되고 완료되었다는 메시지가 출력 됨.  
