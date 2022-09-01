from PyQt5 import QtWidgets, uic
from watermark import Watermark
import webbrowser

class MainWindow(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = uic.loadUi("./resources//MainWidget.ui")
        self.setUp()
        self.ui.show()

    def setUp(self):
        self.ui.btn_watermark.clicked.connect(self.btn_watermarkClickedUI)
        self.ui.label_watermark.mousePressEvent = self.openWeb

    def btn_watermarkClickedUI(self):
        watermarkUI = Watermark()
        watermarkUI.folderChooseUI.show()
        watermarkUI.folderChooseUI.exec()

    def openWeb(self, event):
        webbrowser.open("https://blog.naver.com/hanjinhee502")