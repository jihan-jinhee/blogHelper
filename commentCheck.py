import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PyQt5 import QtWidgets, uic

class CommentCheck(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.commentCheckUI = uic.loadUi("./resources//commentCheckUI.ui")
        self.setUp()

    def setUp(self):
        self.commentCheckUI.btn_check.clicked.connect(self.btn_checkClicked)

    def btn_checkClicked(self):
        URL = self.commentCheckUI.lineEdit_URL.text()
        driver = webdriver.Chrome('chromedriver')
        driver.get(url='https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

        while(True):
            loginDone = driver.current_url
            if loginDone == 'https://www.naver.com/':
                break
            else:
                time.sleep(0.1)

        driver.get(url=URL)
        driver.switch_to.frame('mainFrame')

        postID = URL.split('/')[-1]
        comiID = '//*[@id="Comi' + postID + '"]'

        elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, comiID)))
        driver.find_element(By.XPATH, comiID).click()

        elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'u_cbox_btn_recomm')))
        commentList = driver.find_elements(By.CLASS_NAME, 'u_cbox_btn_recomm')
        for i in range(len(commentList)):
            if len(commentList[i].get_attribute('outerHTML').split('class="')[1].split('"')[0].split(" ")) == 1:
                commentList[i].click()
                while True:
                    if len(commentList[i].get_attribute('outerHTML').split('class="')[1].split('"')[0].split(" ")) == 2:
                        break
                    else:
                        time.sleep(0.1)
