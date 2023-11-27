from PyQt5 import QtWidgets, uic
from cryptography.fernet import Fernet
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip
import logWriter
from ChromeVersion import ChromeVersion


class AutoLogin(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.autoLoginUI = uic.loadUi("./resources//autoLogin.ui")
        self.setUp()

    def setUp(self):
        self.recentText = ''
        self.autoLoginUI.btn_saveLoginInfo.clicked.connect(self.btn_saveLoginInfoClicked)
        self.autoLoginUI.lineEdit_PW.textChanged.connect(self.pwTextInitial)
        self.getSercurityFernet()
        self.loadUserInfo()

    def getSercurityFernet(self):
        securityKeyFile = open("./resources//securityKey.txt", "r")
        securityKey = bytes(securityKeyFile.readline(), 'utf-8')  # Fernet.generate_key()
        fernet = Fernet(securityKey)
        return fernet

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
        fernet = self.getSercurityFernet()
        return fernet.encrypt(bytes(key, 'utf-8'))

    def decrypt(self, key):
        fernet = AutoLogin.getSercurityFernet(self)
        bKey = fernet.decrypt(key)
        return bKey.decode('utf-8')

    def saveEvent(self):
        ID = self.autoLoginUI.lineEdit_ID.text()
        PW = self.autoLoginUI.lineEdit_PW.text()
        self.saveInfo(ID, PW)

    def saveInfo(self, ID, PW):
        if self.checkPwIsHidden(PW):
            self.autoLoginUI.close()
            return

        File = open("./resources/userInfo.txt", "w")
        securityPW = self.encrypt(PW)
        print(ID, file=File)
        print(securityPW, file=File)
        self.autoLoginUI.close()

    def getUserInfo(self):
        try:
            File = open("./resources/userInfo.txt", "r")
        except:
            return [None, None]

        lines = File.readlines()
        if len(lines) == 2:
            id = lines[0][:-1]
            pw = lines[1][2:]
            pw = AutoLogin.decrypt(self, pw)
            return [id, pw]
        else:
            return [None, None]

    def isHaveInfo(self):
        [id, pw] = AutoLogin.getUserInfo(self)
        if id == None or pw == None:
            return False
        else:
            return True

    def naverLogin(self, useAutoLogin):
        URL = "https://blog.naver.com"
        try:
            from selenium.webdriver.chrome.service import Service
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("useAutomationExtension", False)
            chromeVersion = ChromeVersion.getChromeVersionInfo(ChromeVersion).replace("\n", "").replace(" ", "")
            chrome_driver_path = ChromeDriverManager(version=chromeVersion).install()
            service = Service(executable_path=chrome_driver_path)
            driver = webdriver.Chrome(service=service, options=options)
            # driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.implicitly_wait(2)
        except:
            logWriter.writeError("webdriver open fail")
            return None

        self.login(self, driver, useAutoLogin)
        return driver

    def login(self, driver, useAutoLogin : bool):
        driver.get(url='https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
        if self.isHaveInfo(self) and useAutoLogin:
            userID, userPW = self.getUserInfo(self)
            idBox = driver.find_element(By.ID, 'id')
            idBox.click()
            pyperclip.copy(userID)
            idBox.send_keys(Keys.CONTROL, 'v')

            pwBox = driver.find_element(By.ID, 'pw')
            pwBox.click()
            pyperclip.copy(userPW)
            pwBox.send_keys(Keys.CONTROL, 'v')

            enterBox = driver.find_element(By.CLASS_NAME, 'btn_login')
            enterBox.click()

        while (True):
            loginDone = driver.current_url
            if loginDone == 'https://www.naver.com/':
                break
            else:
                time.sleep(0.1)