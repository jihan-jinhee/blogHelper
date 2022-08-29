import sys
from PyQt5 import QtWidgets, uic

class MyApp(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = uic.loadUi("./MainWidget.ui")
        self.ui.show()


app = QtWidgets.QApplication(sys.argv)
me = MyApp()
sys.exit(app.exec())