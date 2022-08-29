import sys
from PyQt5 import QtWidgets
from mainWindow import MainWindow

app = QtWidgets.QApplication(sys.argv)
me = MainWindow()
sys.exit(app.exec())