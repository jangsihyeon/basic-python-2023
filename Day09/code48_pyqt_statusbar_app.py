import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, qApp, QDesktopWidget 
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate , QTime

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # 액션
        actExit = QAction(QIcon('./Day09/exit.png'), 'Exit', self)
        actExit.setShortcut('Ctrl+Q')        # 단축키 지정
        actExit.setStatusTip('앱 종료')
        actExit.triggered.connect(qApp.quit) # 종료 하는 이벤트 지정 

        actSave = QAction(QIcon('./Day09/save.png'), 'Save', self)
        actSave.setShortcut('Ctrl+S')
        actSave.setStatusTip('저장')

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(actExit)

        # 툴바 
        toolbar=self.addToolBar('MainToolBar')    # 툴바 타이틀은 없어도 됌 
        toolbar.addAction(actSave)
        toolbar.addAction(actExit)


        # 상태바 
        now = QDate.currentDate()              # 현재 일자  
        time = QTime.currentTime()             # 현재 시각 
        self.statusBar().showMessage(now.toString('yyyy-MM-dd')+' '+ time.toString('hh:mm:ss'))
        self.setWindowIcon(QIcon('./Day09/iot.png'))
        # GUI 화면 설정
        self.setWindowTitle('Bar Window')
        # self.move(1440//2-200, 900//2-100)   # 정중앙 위치잡기
        self.move(50,50)
        self.resize(400, 200)
        self.setCenter()
        self.show()     # 핵심 !!
    
    # 화면 중심 셋팅 
    def setCenter(self):
        qr = self.frameGeometry()         # 창 자기 자신의 위치 값 
        cp = QDesktopWidget().availableGeometry().center()       # 모니터 화면 중심 
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())