import time
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtCore import Qt
from blogNeighbor import BlogNeighbor

class NeighborBlame(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.filePath = None
        self.fileChooseUI = uic.loadUi("./resources//fileChoose.ui")
        self.neighborBlameUI = uic.loadUi("./resources//NeighborBlame.ui")
        self.neighborBlameUI.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setUp()

    def setUp(self):
        self.fileChooseUI.btn_choose.clicked.connect(self.btn_chooseClicked)
        self.neighborBlameUI.btn_check.clicked.connect(self.btn_checkClicked)
        self.neighborBlameUI.spinBox.valueChanged.connect(self.spinChanged)
        self.spinChanged()

    def spinChanged(self):
        self.postSearchNum = self.neighborBlameUI.spinBox.value()
        self.neighborBlameUI.label_processing.setText("0/" + str(self.postSearchNum))

    def fileChooseUI(self, kind: str):
        fileChooseUI = uic.loadUi("./resources//fileChoose.ui")
        fileChooseUI.label.setText(kind + " : ")
        fileChooseUI.btn_choose.setText(kind)
        self.filepath = QtWidgets.QFileDialog.getOpenFileNames(self, 'Select File')
        fileChooseUI.label_path.setText(self.filepath)
        return fileChooseUI

    def btn_chooseClicked(self):
        self.filepath = QtWidgets.QFileDialog.getOpenFileNames(self, 'Select File')[0][0]
        if self.filepath is None or self.filepath == "" or self.filepath.split(".")[-1] != 'opml':
            return

        self.userID = self.filepath.split('/')[-1].split('.')[0]
        self.neighborBlameUI.lineEdit_ID.setText(self.userID)
        self.fileChooseUI.label_filePath.setText(self.filepath)
        qr = self.neighborBlameUI.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        self.neighborBlameUI.move(cp.x(), cp.y() + 50)
        self.neighborBlameUI.show()

    def btn_checkClicked(self):
        self.timeCal()
        ID = self.neighborBlameUI.lineEdit_ID.text()
        postLikeList = BlogNeighbor.postLikeNeighbor(BlogNeighbor, ID, self.postSearchNum)
        neighborList = BlogNeighbor.loadNeighborList(BlogNeighbor, self.filepath)
        warnUser = neighborList - postLikeList
        print(warnUser)

    def timeCal(self):
        pass
