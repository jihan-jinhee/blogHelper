import time
from PyQt5 import QtWidgets, uic
from AutoLogin import AutoLogin
import mainFunction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webControl import WebControl
import logWriter
from selenium.webdriver import ActionChains

class NeighborAdd(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.parent = parent
        self.neighborAddUI = uic.loadUi("./resources//neighborAdd.ui")
        self.setUp()

    def setUp(self):
        self.neighborAddUI.btn_add.clicked.connect(self.btn_addClicked)

    def naverLogin(self):
        useAutoLogin = self.parent.ui.actionmenu1.isChecked()
        self.driver = AutoLogin.naverLogin(AutoLogin, useAutoLogin)

    def btn_addClicked(self):
        URL = self.neighborAddUI.lineEdit_URL.text()
        URL = URL.replace('https://blog', 'https://m.blog')

        self.naverLogin()

        self.driver.get(url=URL)
        time.sleep(1)
        self.findNeighbor(driver=self.driver)
        mainFunction.driverQuitAll(self.driver)

    def findNeighbor(self, driver):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn_like_more')))
        a = driver.find_elements(By.CLASS_NAME, 'btn_like_more')
        try:
            a[0].click()
        except:
            a[1].click()
        WebControl.scrollDownDeep(self=WebControl, driver=driver)
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'num___9TRf')))
        except:
            logWriter.writeError("like num find fail")
            return

        num = int(driver.find_element(By.CLASS_NAME, 'num___9TRf').text)
        action = ActionChains(driver)
        for i in range(num):
            error = False
            btn_adds = driver.find_elements(By.CLASS_NAME, 'add_buddy_btn___Xme9')
            try:
                action.move_to_element(btn_adds[i]).perform()
            except:
                logWriter.writeError("move fail: add neighbor")
                error = True

            if not error:
                time.sleep(0.2)
                # page 올리고
                try:
                    btn_adds[i].click()
                except:
                    logWriter.writeError("btn click fail: add neighbor")
                    error = True

            if not error:
                try:
                    WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME, 'radio_img1')))
                except:
                    if '이웃수가 초과' in driver.find_elements(By.CLASS_NAME, 'apollo_layer_container')[0].text or '5,000명이 초과' in driver.find_elements(By.CLASS_NAME, 'apollo_layer_container')[0].text:
                        break
                    driver.find_elements(By.CLASS_NAME, 'btn__nsI4v')[0].click()
                    error = True

            if not error:
                radio = driver.find_elements(By.CLASS_NAME, 'radio_img1')
                if ' disabled=' in radio[1].get_attribute('outerHTML'):
                    if 'disabled' in radio[1].get_attribute('outerHTML').split(" disabled=")[1]:
                        try:
                            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn_close')))
                            closeBtn = driver.find_elements(By.CLASS_NAME, 'btn_close')
                            closeBtn[0].click()
                            error = True
                        except:
                            pass
                if not error:
                    try:
                        radio[1].click()
                        time.sleep(0.5)
                    except:
                        error = True

            if not error:
                try:
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn_ok')))
                    sendBtn = driver.find_elements(By.CLASS_NAME, 'btn_ok')
                    sendBtn[0].click()
                except:
                    logWriter.writeError("btn click fail: add neighbor, btn_ok")
                    error = True

            if not error:
                try:
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn_close')))
                    closeBtn = driver.find_elements(By.CLASS_NAME, 'btn_close')
                    closeBtn[0].click()
                except:
                    driver.find_elements(By.CLASS_NAME, 'btn_100')[0].click()
                    try:
                        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn_close')))
                        closeBtn = driver.find_elements(By.CLASS_NAME, 'btn_close')
                        closeBtn[0].click()
                    except:
                        logWriter.writeError("btn click fail: add neighbor, btn_close")