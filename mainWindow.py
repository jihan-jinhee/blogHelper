from PyQt5 import QtWidgets, uic
from watermark import Watermark
from commentCheck import CommentCheck
from AutoLogin import AutoLogin
from Purchase import Purchase
import os

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
        self.ui.actionmenu1.setCheckable(True)
        self.ui.actionmenu1.triggered.connect(self.autoLogin)
        self.ui.label_watermark.mousePressEvent = self.openWeb

    def btn_watermarkClickedUI(self):
        watermarkUI = Watermark(self)
        watermarkUI.folderChooseUI.show()
        watermarkUI.folderChooseUI.exec()

    def btn_commentCheckClickedUI(self):
        commentCheckUI = CommentCheck(self)
        commentCheckUI.commentCheckUI.show()
        commentCheckUI.commentCheckUI.exec()

    def btn_visitNeighborClickedUI(self):
        if os.path.isfile('./neighborPostLike.py'):
            from neighborPostLike import NeighborPostLike
            neighborPostLikeUI = NeighborPostLike(self)
            neighborPostLikeUI.neighborPostLikeUI.show()
            neighborPostLikeUI.neighborPostLikeUI.exec()
        else:
            purchaseUI = Purchase(self)
            purchaseUI.purchaseUI.show()
            purchaseUI.purchaseUI.exec()

    def autoLogin(self):
        if self.ui.actionmenu1.isChecked():
            autoLoginUI = AutoLogin(self)
            autoLoginUI.autoLoginUI.show()
            autoLoginUI.autoLoginUI.exec()
            if not autoLoginUI.isHaveInfo():
                self.ui.actionmenu1.setChecked(False)
        else:
            pass

    def openWeb(self, event):
        Purchase(self).openContact()