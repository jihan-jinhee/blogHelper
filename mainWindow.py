from PyQt5 import QtWidgets, uic
from watermark import Watermark
from commentCheck import CommentCheck
from letterCount import LetterCount
from AutoLogin import AutoLogin
from Purchase import Purchase
from CommentText import CommentText
from ChromeVersion import ChromeVersion
from NeighborBlame import NeighborBlame
from NeighborAdd import NeighborAdd
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
        self.ui.btn_letterCount.clicked.connect(self.btn_letterCountClickedUI)
        self.ui.btn_neighborBlame.clicked.connect(self.btn_neighborBlameClickedUI)
        self.ui.btn_neighborAdd.clicked.connect(self.btn_neighborAddClickedUI)
        self.ui.actionmenu1.setText("자동 로그인 설정")
        self.ui.actionmenu1.setCheckable(True)
        self.ui.actionmenu1.triggered.connect(self.autoLogin)
        self.ui.actionmenu2.setText("댓글 문구 설정")
        self.ui.actionmenu2.setCheckable(True)
        self.ui.actionmenu2.triggered.connect(self.commentText)
        self.ui.actionmenu3.setText("크롬 버전 설정")
        self.ui.actionmenu3.triggered.connect(self.chromeVersion)
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

    def btn_letterCountClickedUI(self):
        letterCountUI = LetterCount(self)
        letterCountUI.letterCountUI.show()
        letterCountUI.letterCountUI.exec()

    def btn_neighborBlameClickedUI(self):
        neighborBlameUI = NeighborBlame(self)
        neighborBlameUI.fileChooseUI.show()
        neighborBlameUI.fileChooseUI.exec()

    def btn_neighborAddClickedUI(self):
        neighborAddUI = NeighborAdd(self)
        neighborAddUI.neighborAddUI.show()
        neighborAddUI.neighborAddUI.exec()

    def autoLogin(self):
        if self.ui.actionmenu1.isChecked():
            autoLoginUI = AutoLogin(self)
            autoLoginUI.autoLoginUI.show()
            autoLoginUI.autoLoginUI.exec()
            if not autoLoginUI.isHaveInfo():
                self.ui.actionmenu1.setChecked(False)
        else:
            pass

    def commentText(self):
        if self.ui.actionmenu2.isChecked():
            commentTextUI = CommentText(self)
            commentTextUI.commentTextUI.show()
            commentTextUI.commentTextUI.exec()
            if not commentTextUI.isHaveInfo():
                self.ui.actionmenu2.setChecked(False)
        else:
            pass

    def chromeVersion(self):
        ChromeVersionUI = ChromeVersion(self)
        ChromeVersionUI.ChromeVersionUI.show()
        ChromeVersionUI.ChromeVersionUI.exec()

    def openWeb(self, event):
        Purchase(self).openContact()