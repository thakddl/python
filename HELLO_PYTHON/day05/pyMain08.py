from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import random


form_class = uic.loadUiType("pyMain08.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        #버튼에 기능을 연결하는 코드
        self.pb.clicked.connect(self.myclick)
        self.lelast.returnPressed.connect(self.myclick)

    def drawStar(self,cnt):
        txt=""
        for a in range(cnt):
            txt += "*"
        txt += "\n"
        return txt
    
    def myclick(self):
        lefirst = self.lefirst.text()
        lelast = self.lelast.text()
        
        firstNum = int(lefirst)
        lastNum = int(lelast)
        result = ""
        
        for item in range(firstNum,lastNum+1):
            result += self.drawStar(item)
        
        self.te.setText(result)
        


if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()