import sys

from PyQt5 import uic
from PyQt5.Qt import QIcon, QPushButton, QSize, QMessageBox
from PyQt5.QtWidgets import QMainWindow, QApplication


form_class = uic.loadUiType("myomok04.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.flagWb = True
        self.flagEnd = False
        self.reset.clicked.connect(self.resetClick)
        self.arr2D = []
        self.pb2D = []
        self.lineCnt = 19
        
        for i in range(self.lineCnt):
            line =[]
            for j in range(self.lineCnt):
                line.append(0)
            self.arr2D.append(line)
            
            
        for i in range(self.lineCnt):
            line =[]
            for j in range(self.lineCnt):
                pb = QPushButton(self)
                pb.setIconSize(QSize(40,40))
                pb.setGeometry(40*j, 40*i, 40, 40)
                pb.setIcon(QIcon('0.png'))
                pb.setToolTip('{},{}'.format(i, j))
                pb.clicked.connect(self.myclick)
                line.append(pb)
            self.pb2D.append(line)
        self.myRander()
        
        
    def myRander(self):
        for i in range(self.lineCnt):
            for j in range(self.lineCnt):
                if self.arr2D[i][j] == 0:
                    self.pb2D[i][j].setIcon(QIcon('0.png'))
                elif self.arr2D[i][j] == 1:
                    self.pb2D[i][j].setIcon(QIcon('1.png'))
                elif self.arr2D[i][j] == 2:
                    self.pb2D[i][j].setIcon(QIcon('2.png'))
    
    def resetClick(self):
        for i in range(self.lineCnt):
            for j in range(self.lineCnt):
                self.arr2D[i][j] = 0
                
        self.myRander()        
        self.flagWb = True
        self.flagEnd = False

    def myclick(self):
        
        if self.flagEnd:
            return
        
        place = self.sender().toolTip()
        spPlace = place.split(',')
        
        i = int(spPlace[0])
        j = int(spPlace[1])
        
        if self.arr2D[i][j] > 0:
            return
        
        stone = -1
        if self.flagWb:
            self.arr2D[i][j] = 1
            stone = 1
        else:
            self.arr2D[i][j] = 2
            stone = 2
        up = self.checkUP(i,j,stone)
        dw = self.checkDW(i,j,stone)
        le = self.checkLE(i,j,stone)
        ri = self.checkRI(i,j,stone)
        
        ul = self.checkUL(i,j,stone)
        ur = self.checkUR(i,j,stone)
        dl = self.checkDL(i,j,stone)
        dr = self.checkDR(i,j,stone)
        
        print(up,dw,le,ri,ul,ur,dl,dr)
        self.myRander()
        
        d1 = up + dw + 1
        d2 = le + ri + 1
        d3 = ul + dr + 1
        d4 = ur + dl + 1
        
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5:
            self.finish(self.flagWb)
        
        self.flagWb = not self.flagWb
    
    
    def finish(self, flagWb):
        str = ''
        if flagWb:
            str = '백돌 승리'
        else:
            str = '흑돌 승리'
            
        self.flagEnd = True
        QMessageBox.about(self,'결과', str)

    
    def checkDR(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                j += 1
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt        
        except:
            return cnt 
    
    def checkDL(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                j -= 1
                
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt        
        except:
            return cnt 
        
    def checkUR(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i -= 1
                j += 1
                
                if i < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt        
        except:
            return cnt 
     
    def checkUL(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i -= 1
                j -= 1
                
                if i < 0 or j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt        
        except:
            return cnt 
        
    def checkRI(self,i,j,stone):
        cnt = 0
        try:
            while True:
                j += 1
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt        
        except:
            return cnt
        
    def checkLE(self,i,j,stone):
        cnt = 0
        try:
            while True:
                j -= 1
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt        
        except:
            return cnt
        
    def checkDW(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt        
        except:
            return cnt
        
    def checkUP(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i -= 1
                if i < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt            
        except:
            return cnt
        
        
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()