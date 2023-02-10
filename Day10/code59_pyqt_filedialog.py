# 인풋 다이어로그 (엄청 많이 씀)
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        
        openFile= QAction('Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('파일열기')
        openFile.triggered.connect(self.onClicked)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')

        fileMenu.addAction(openFile)

        # 필수 설정(initUI에 있는 class로 불러오는 변수 // 이거 밑에 원하는 실행함수 작성)
        self.setWindowTitle('파일 다이어로그')
        self.setGeometry(300,300,300,300)
        self.show()

    def onClicked(self):
        fname= QFileDialog.getOpenFileName(self, '파일 열기', './')

        if fname[0]:                 # 파일 선택했다면
            file = open(fname[0], 'rt', encoding='utf-8')
            with file:
                data = file.read()
                self.textEdit.setText(data) 
            file.close()

        QMessageBox.about(self, '메세지', '로드했습니다.')

    def closeEvent(self, event) -> None:
        relpy= QMessageBox.question(self, '종료', '정말 종료하시겠습니까?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if relpy == QMessageBox.Yes:
            event.accept()          # 프로그램 종료 
        else:
            event.ignore()          # 그대로 프로그램 계속 


if __name__ =='__main__' :
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())