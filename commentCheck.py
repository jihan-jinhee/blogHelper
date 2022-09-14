import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from PyQt5 import QtWidgets, uic
import pyperclip

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

        # 추후 login 방법 변경
        userID = URL.split('/')[3]
        self.login(driver, userID)

        driver.get(url=URL)
        driver.switch_to.frame('mainFrame')

        postID = URL.split('/')[-1]
        comiID = '//*[@id="Comi' + postID + '"]'

        # 댓글창 클릭
        elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, comiID)))
        driver.find_element(By.XPATH, comiID).click()

        # 댓글 리스트 저장
        elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'u_cbox_btn_recomm')))
        commentList = driver.find_elements(By.CLASS_NAME, 'u_cbox_btn_recomm')

        # 댓글 관리 (좋아요, 답방)
        self.commentManage(commentList, driver)

        time.sleep(10)

    def login(self, driver, userID):
        driver.get(url='https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
        idBox = driver.find_element(By.ID, 'id')
        idBox.click()
        pyperclip.copy(userID)
        idBox.send_keys(Keys.CONTROL, 'v')

        pwBox = driver.find_element(By.ID, 'pw')
        pwBox.click()

        while (True):
            loginDone = driver.current_url
            if loginDone == 'https://www.naver.com/':
                break
            else:
                time.sleep(0.1)

    def commentManage(self, commentList, driver):
        for i in range(len(commentList)):
            commentLike = commentList[i]
            if len(commentLike.get_attribute('outerHTML').split('class="')[1].split('"')[0].split(" ")) == 1:
                # 좋아요
                commentLike.click()

                commentBox = commentLike.find_element(By.XPATH, '../../..')
                commentID = commentBox.find_element(By.CLASS_NAME, 'u_cbox_info_main')
                comentIDURL = commentID.get_attribute('outerHTML').split('"')[3]

                driver.execute_script('window.open("' + comentIDURL + '");')
                driver.switch_to.window(driver.window_handles[0])
                driver.switch_to.frame('mainFrame')

                while True:
                    if len(commentLike.get_attribute('outerHTML').split('class="')[1].split('"')[0].split(" ")) == 2:
                        break
                    else:
                        time.sleep(0.1)