import time
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtCore import Qt
from AutoLogin import AutoLogin
import csvManager
from blogNeighbor import BlogNeighbor
from csvManager import *
from webControl import blogAdmin

class NeighborBlame(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.filePath = None
        self.fileChooseUI = uic.loadUi("./resources//fileChoose.ui")
        self.neighborBlameUI = uic.loadUi("./resources//NeighborBlame.ui")
        self.neighborBlameUI.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setUp()

    def setUp(self):
        self.fileChooseUI.btn_choose.clicked.connect(self.btn_chooseClicked)
        self.neighborBlameUI.btn_check.clicked.connect(self.btn_checkClicked)
        self.neighborBlameUI.btn_deleteNeighbor.clicked.connect(self.btn_deleteNeighborClicked)

    def fileChooseUI(self, kind: str):
        fileChooseUI = uic.loadUi("./resources//fileChoose.ui")
        fileChooseUI.label.setText(kind + " : ")
        fileChooseUI.btn_choose.setText(kind)
        self.filepath = QtWidgets.QFileDialog.getOpenFileNames(self, 'Select File')
        fileChooseUI.label_path.setText(self.filepath)
        return fileChooseUI

    def btn_chooseClicked(self):
        filepath = QtWidgets.QFileDialog.getOpenFileNames(self, 'Select File')[0]
        if filepath == [] or filepath == "" or filepath[0].split(".")[-1] != 'opml':
            return
        else:
            self.filepath = filepath[0]

        self.userID = self.filepath.split('/')[-1].split('.')[0].split(" ")[0]
        self.neighborBlameUI.lineEdit_ID.setText(self.userID)
        self.fileChooseUI.label_filePath.setText(self.filepath)
        qr = self.neighborBlameUI.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        self.neighborBlameUI.move(cp.x(), cp.y() + 50)
        self.neighborBlameUI.show()

    def btn_checkClicked(self):
        ID = self.neighborBlameUI.lineEdit_ID.text()
        postSearchNum = self.neighborBlameUI.spinBox.value()
        postLikeList = BlogNeighbor.postLikeNeighbor(BlogNeighbor, ID, postSearchNum)
        neighborList = BlogNeighbor.loadNeighborList(BlogNeighbor, self.filepath)
        warnUser = neighborList - postLikeList
        csvWrite.neighborListCSV(warnUser)
        print(warnUser)

    def btn_deleteNeighborClicked(self):
        deleteNeighborCount = self.neighborBlameUI.spinBox_delete.value()
        sucess = self.deleteNeighbor(deleteNeighborCount)
        self.driver.close()

    def login(self):
        useAutoLogin = self.parent.ui.actionmenu1.isChecked()
        self.driver = AutoLogin.naverLogin(AutoLogin, useAutoLogin)

    def deleteNeighbor(self, neighborCount):
        success = False
        deleteList = self.readNeighborCSV()
        if deleteList == None:
            return success

        self.login()
        self.userID = self.neighborBlameUI.lineEdit_ID.text()
        blogAdmin.moveBlogAdmin(blogAdmin, self.driver, self.userID)
        success = blogAdmin.deleteNeighborInGroup(blogAdmin, self.driver, deleteList, neighborCount)
        self.EditNeighborCSV(neighborCount)
        return success

    def readNeighborCSV(self):
        deleteList = csvManager.csvRead.neighborListCSV()
        return deleteList

    def EditNeighborCSV(self, neighborCount):
        csvManager.csvWrite.deleteNeighborCSV(neighborCount)
