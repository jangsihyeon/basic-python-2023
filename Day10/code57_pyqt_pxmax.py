# 이미지
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pixmap = QPixmap('./Day10/suncat.jpg')

        lblImage =QLabel(self)
        lblImage.setPixmap(pixmap)
        lblSize = QLabel(str(pixmap.width() )+ 'x'+str(pixmap.height()))
        lblSize.setAlignment(Qt.AlignmentFlag.AlignCenter)               # Ot.AlignCenter도 가능 

        vbox = QVBoxLayout(self)
        vbox.addWidget(lblImage)
        vbox.addWidget(lblSize)

        self.setLayout(vbox) 

        # 필수 설정
        self.setWindowTitle('pxmax')
        self.setGeometry(300,300,300,300)
        self.show()
        self.setCenter()

    # 화면 중심 셋팅 
    def setCenter(self):
        qr = self.frameGeometry()                                # 창 자기 자신의 위치 값 
        cp = QDesktopWidget().availableGeometry().center()       # 모니터 화면 중심 
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    

if __name__ =='__main__' :
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())