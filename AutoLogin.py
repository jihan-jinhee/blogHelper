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
        self.recentText = ''
        self.autoLoginUI.btn_saveLoginInfo.clicked.connect(self.btn_saveLoginInfoClicked)
        self.autoLoginUI.lineEdit_PW.textChanged.connect(self.pwTextInitial)
        securityKey = bytes(self.securityKeyFile.readline(), 'utf-8')  # Fernet.generate_key()
        self.fernet = Fernet(securityKey)
        self.loadUserInfo()

    def loadUserInfo(self):
        if self.isHaveInfo():
            [id, pw] = self.getUserInfo()
            self.autoLoginUI.lineEdit_ID.setText(id)
            self.autoLoginUI.lineEdit_PW.setText('*' * len(pw))

    def pwTextInitial(self):
        if self.checkPwIsHidden(self.recentText):
            self.autoLoginUI.lineEdit_PW.setText('')
        self.recentText = self.autoLoginUI.lineEdit_PW.text()

    def checkPwIsHidden(self, pw):
        if '*' in pw:
            checkPw = pw.replace('*','')
            if len(checkPw) == 0:
                return True
        return False

    # def keyPressEvent(self, e):
    #     if e.key() == Qt.Key_Enter:
    #         self.saveEvent()

    def btn_saveLoginInfoClicked(self):
        self.saveEvent()

    def encrypt(self, key):
        return self.fernet.encrypt(bytes(key, 'utf-8'))

    def decrypt(self, key):
        bKey = self.fernet.decrypt(key)
        return bKey.decode('utf-8')

    def saveEvent(self):
        ID = self.autoLoginUI.lineEdit_ID.text()
        PW = self.autoLoginUI.lineEdit_PW.text()
        self.saveInfo(ID, PW)

    def saveInfo(self, ID, PW):
        if self.checkPwIsHidden(PW):
            self.autoLoginUI.close()
            return

        File = open("userInfo.txt", "w")
        securityPW = self.encrypt(PW)
        print(ID, file=File)
        print(securityPW, file=File)
        self.autoLoginUI.close()

    def getUserInfo(self):
        try:
            File = open("userInfo.txt", "r")
        except:
            return [None, None]

        lines = File.readlines()
        if len(lines) == 2:
            id = lines[0][:-1]
            pw = lines[1][2:]
            pw = self.decrypt(pw)
            return [id, pw]
        else:
            return [None, None]

    def isHaveInfo(self):
        [id, pw] = AutoLogin.getUserInfo(self)
        if id == None or pw == None:
            return False
        else:
            return True