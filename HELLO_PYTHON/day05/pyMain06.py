from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import random


form_class = uic.loadUiType("pyMain06.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        #버튼에 기능을 연결하는 코드
        self.pb.clicked.connect(self.myclick)

    def myclick(self):
        danT = ""
        text = "";
        
        danT = self.le.text()
        dan = int(danT)
        print(dan)
        
        text += "{}*{}={}\n".format(dan, 1, dan*1) 
        text += "{}*{}={}\n".format(dan, 2, dan*2) 
        text += "{}*{}={}\n".format(dan, 3, dan*3) 
        text += "{}*{}={}\n".format(dan, 4, dan*4) 
        text += "{}*{}={}\n".format(dan, 5, dan*5) 
        text += "{}*{}={}\n".format(dan, 6, dan*6) 
        text += "{}*{}={}\n".format(dan, 7, dan*7) 
        text += "{}*{}={}\n".format(dan, 8, dan*8) 
        text += "{}*{}={}\n".format(dan, 9, dan*9) 
        
        self.te.setText(text)
        


if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()