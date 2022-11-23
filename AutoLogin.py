from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from cryptography.fernet import Fernet

class AutoLogin(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.autoLoginUI = uic.loadUi("./resources//autoLogin.ui")
        self.securityKeyFile = open("./resources//securityKey.txt", "r")
        self.setUp()

    def setUp(self):
        self.autoLoginUI.btn_saveLoginInfo.clicked.connect(self.btn_saveLoginInfoClicked)
        securityKey = bytes(self.securityKeyFile.readline(), 'utf-8')  # Fernet.generate_key()
        self.fernet = Fernet(securityKey)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Enter:
            self.saveEvent()

    def btn_saveLoginInfoClicked(self):
        self.saveEvent()

    def encrypt(self, key):
        return self.fernet.encrypt(bytes(key, 'utf-8'))

    def decrypt(self, key):
        return self.fernet.decrypt(key)

    def saveEvent(self):
        ID = self.autoLoginUI.lineEdit_ID.text()
        PW = self.autoLoginUI.lineEdit_PW.text()
        self.saveInfo(ID, PW)

    def saveInfo(self, ID, PW):
        File = open("userInfo.txt", "w")
        securityPW = self.encrypt(PW)
        print(ID, file=File)
        print(securityPW, file=File)
        self.autoLoginUI.close()