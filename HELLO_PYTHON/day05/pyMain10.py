import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import threading
import time


form_class = uic.loadUiType("pyMain10.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        #버튼에 기능을 연결하는 코드
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        th = threading.Thread(target=self.startTm)
        th.start()
    
    def startTm(self):
        old_text = self.lbl.text()
        old_time = int(old_text)
        now = old_time
        
        for i in range(10):
            now +=1 
            print(now)
            time.sleep(1)
            self.lbl.setText(str(now))
        
   

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()