from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import random


form_class = uic.loadUiType("pyMain05.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        #버튼에 기능을 연결하는 코드
        self.pb.clicked.connect(self.myclick)

    def myclick(self):
        list = []
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                   11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                   21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                   31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                   41, 42, 43, 44, 45]
        
        while len(list)<6: 
            rnd = (int) (random.random()*45)
            lottoNum = numbers[rnd]
            if lottoNum!=-1: 
                list.append(lottoNum)
                numbers[rnd] = -1
            else:
                continue
            
        print(list) 
        
        for i in range(len(list)) :
            j = len(list) - i
            for a in range(1, j):
                if list[a-1] > list[a]:
                    temp = list[a-1]
                    list[a-1] = list[a]
                    list[a] = temp
        
        
        for i in range(len(list)) :
            for j in range(len(list)):
                if list[i] < list[j]:
                    temp = list[i]
                    list[i] = list[j]
                    list[j] = temp
        
                     
        print(list)
        
        self.le1.setText(str(list[0]))
        self.le2.setText(str(list[1]))
        self.le3.setText(str(list[2]))
        self.le4.setText(str(list[3]))
        self.le5.setText(str(list[4]))
        self.le6.setText(str(list[5]))


if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()