from PyQt5 import QtWidgets, uic
import webbrowser

class Purchase(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.purchaseUI = uic.loadUi("./resources//purchase.ui")
        self.setUp()

    def setUp(self):
        self.purchaseUI.label_watermark.mousePressEvent = self.openWeb

    def openWeb(self, event):
        self.openContact()

    def openContact(self):
        webbrowser.open("https://blog.naver.com/hanjinhee502")