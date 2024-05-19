import sys
import threading
import time

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, QObject

form_class = uic.loadUiType("timesaver.ui")[0]


class Communicate(QObject):
    update_progress = pyqtSignal(int)  # 프로그레스 바 시그널 설정


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Button_input.clicked.connect(self.buttonFunction)

        self.comm = Communicate()
        self.comm.update_progress.connect(self.updateProgressBar)
    def buttonFunction(self):
        global a, b, c
        a = self.apple.text()  # 시간
        c = self.apple_2.text()  # 분
        b = self.plant.text()  # 할 일

        self.table.setPlainText(b)

        try:
            k = (int(a) * 3600) + (int(c) * 60)  # 초로 변환
        except ValueError:
            print("시간과 분을 전부 다 입력 해주세요")
            return

        self.Bar.setMinimum(0)
        self.Bar.setMaximum(k)

        # 타이머 스레드 시작
        timer_thread = threading.Thread(target=self.timeTimer, args=(k,))
        timer_thread.start()

    def updateProgressBar(self, value):
        self.Bar.setValue(value)

    def timeTimer(self, seconds):
        for i in range(seconds):
            time.sleep(1)
            self.comm.update_progress.emit(i + 1)
        print("Timeover")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())
