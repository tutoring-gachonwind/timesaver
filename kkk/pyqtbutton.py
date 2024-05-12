import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("타임세이버ui.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #버튼에 기능을 할당하는 코드
        self.lineEdittimelimit.returnPressed.connect(self.printTextFunction)

    def printTextFunction(self) :
        #self.lineEdit이름.text()
        #Lineedit에 있는 글자를 가져오는 메서드
        print(self.lineEdittimelimit.text())

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
