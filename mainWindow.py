from PyQt5 import QtWidgets, uic
from watermark import Watermark
from commentCheck import CommentCheck
from AutoLogin import AutoLogin
import webbrowser

class MainWindow(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = uic.loadUi("./resources//MainWidget.ui")
        self.setUp()
        self.ui.show()

    def setUp(self):
        self.ui.btn_watermark.clicked.connect(self.btn_watermarkClickedUI)
        self.ui.btn_commentCheck.clicked.connect(self.btn_commentCheckClickedUI)
        self.ui.btn_visitNeighbor.clicked.connect(self.btn_visitNeighborClickedUI)
        self.ui.actionmenu1.setText("자동 로그인 설정")
        self.ui.actionmenu1.triggered.connect(self.autoLogin)
        self.ui.label_watermark.mousePressEvent = self.openWeb

    def btn_watermarkClickedUI(self):
        watermarkUI = Watermark()
        watermarkUI.folderChooseUI.show()
        watermarkUI.folderChooseUI.exec()

    def btn_commentCheckClickedUI(self):
        commentCheckUI = CommentCheck()
        commentCheckUI.commentCheckUI.show()
        commentCheckUI.commentCheckUI.exec()

    def btn_visitNeighborClickedUI(self):
        print("Test")

    def autoLogin(self):
        autoLoginUI = AutoLogin()
        autoLoginUI.autoLoginUI.show()
        autoLoginUI.autoLoginUI.exec()

    def openWeb(self, event):
        webbrowser.open("https://blog.naver.com/hanjinhee502")