# 콤보 박스 
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class YourApp(QWidget):            
    def __init__(self):                  # self : 클래스 자기자신 , self.~ 쓰면 클래스 변수(클래스의 로컬, def의 글로벌)로 사용한다는 의미// 안쓰면 def 아래 로컬로 
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.lblOption = QLabel('선택 값 :', self)
        self.lblOption.move(20, 20)

        cbOption = QComboBox(self)
        cbOption.addItem('Option1')
        cbOption.addItem('Option2')
        cbOption.addItem('Option3')
        cbOption.addItem('Option4')
        cbOption.addItem('Option5')
        cbOption.move(20, 40)
        cbOption.activated[str].connect(self.onActivated)

        # 필수 설정
        self.setWindowTitle('콤보박스')
        self.setGeometry(300,300,300,300)
        self.show()

    def onActivated(self, text):
        self.lblOption.setText('선택 값 : '+ text)
        self.lblOption.adjustSize()             # 글자수 만큼 라벨 넓이 조정

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = YourApp()
    sys.exit(app.exec_())
