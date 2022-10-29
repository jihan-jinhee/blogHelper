import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from PyQt5 import QtWidgets, uic
import pyperclip
import logging

class CommentCheck(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.commentCheckUI = uic.loadUi("./resources//commentCheckUI.ui")
        Log_Format = "%(levelname)s %(asctime)s - %(message)s"
        logging.basicConfig(filename="logfile.log",
                            filemode="w",
                            format=Log_Format,
                            level=logging.ERROR)
        self.logger = logging.getLogger()
        self.setUp()

    def setUp(self):
        self.commentCheckUI.btn_check.clicked.connect(self.btn_checkClicked)

    def btn_checkClicked(self):
        error = False
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
        time.sleep(0.1)
        try:
            elem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, comiID)))
            driver.find_element(By.XPATH, comiID).click()
        except:
            error = True
            self.logger.error("Lodding Fali : comiID, 댓글창 클릭 실패")
            driver.close()

        # 댓글 리스트 저장
        if not error:
            try:
                elem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'u_cbox_btn_recomm')))
                commentList = driver.find_elements(By.CLASS_NAME, 'u_cbox_btn_recomm')

            except:
                error = True
                self.logger.error("Lodding Fali : u_cbox_btn_recomm, 댓글 리스트 저장 실패")
                driver.close()

        if not error:
            # 댓글 관리 (좋아요, 창 띄우기)
            self.commentLike(commentList, driver)
            windowCount = len(driver.window_handles)
            if windowCount != 1:
                self.likePost(driver, windowCount)

        driver.quit()

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

    def commentLike(self, commentList, driver):
        for i in range(len(commentList)):
            commentLike = commentList[i]
            if len(commentLike.get_attribute('outerHTML').split('class="')[1].split('"')[0].split(" ")) == 1:
                # 좋아요
                commentLike.click()

                commentBox = commentLike.find_element(By.XPATH, '../../..')
                commentID = commentBox.find_element(By.CLASS_NAME, 'u_cbox_info_main')
                comentIDURL = commentID.get_attribute('outerHTML').split('"')[3]
                comentIDURL = comentIDURL.replace('https://blog', 'https://m.blog')
                driver.execute_script('window.open("' + comentIDURL + '");')
                driver.switch_to.window(driver.window_handles[0])
                driver.switch_to.frame('mainFrame')

                while True:
                    if len(commentLike.get_attribute('outerHTML').split('class="')[1].split('"')[0].split(" ")) == 2:
                        break
                    else:
                        time.sleep(0.1)

    def likePost(self, driver, windowCount):
        for i in range(windowCount - 1):
            error = False
            driver.switch_to.window(driver.window_handles[1])
            try:
                elem = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'view_type_btn__z6Hlf')))
            except:
                self.logger.error("Lodding Fali : view_type_btn__z6Hlf : " + str(i))
                error = True

            try:
                elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn__xjUPw')))
            except:
                self.logger.error("Lodding Fali : btn__xjUPw : " + str(i))
                error = True

            if not error:
                buttonList = driver.find_elements(By.CLASS_NAME, 'btn__xjUPw')
                buttonList[3].click()

            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'card__WjujK')))
            except:
                self.logger.error("Lodding Fali : card__WjujK : " + str(i))
                error = True

            if not error:
                driver.find_element(By.CLASS_NAME, 'card__WjujK').click()
                moblieURL = driver.current_url
                PCURL = moblieURL.replace('https://m.blog', 'https://blog')
                driver.get(url=PCURL)
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'u_likeit_list_btn')))
            except:
                self.logger.error("Lodding Fali : u_likeit_list_btn, 좋아요 버튼 탐색 실패 : " + str(i))
                error = True

            if not error:
                likeOfPost = driver.find_elements(By.CLASS_NAME, 'u_likeit_list_btn')
                for j in range(len(likeOfPost)):
                    if likeOfPost[j].aria_role == 'generic':
                        if 'off' in likeOfPost[j].get_attribute('outerHTML').split('"')[1]:
                            likeOfPost[j - 1].click()
                            time.sleep(0.1)

            driver.close()


