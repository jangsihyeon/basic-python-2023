# 인풋 다이어로그 (엄청 많이 씀)
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btnDlg=QPushButton('Dialog', self)
        self.btnDlg.move(30, 30)
        self.btnDlg.clicked.connect(self.onClicked)

        self.txtInput = QLineEdit(self)
        self.txtInput.move(30, 60)

        # 필수 설정(initUI에 있는 class로 불러오는 변수 // 이거 밑에 원하는 실행함수 작성)
        self.setWindowTitle('다이어로그')
        self.setGeometry(300,300,300,300)
        self.show()
    
    def onClicked(self):
        text, ok = QInputDialog.getText(self, '인풋 다이얼로그', '이름을 적으세요')
        
        if ok :
            self.txtInput.setText(text)
   
if __name__ =='__main__' :
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())