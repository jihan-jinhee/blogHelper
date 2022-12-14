import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PyQt5 import QtWidgets, uic
from webdriver_manager.chrome import ChromeDriverManager
from AutoLogin import AutoLogin
import logWriter
import commentWriter
import mainFunction

class CommentCheck(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.parent = parent
        self.commentCheckUI = uic.loadUi("./resources//commentCheckUI.ui")
        self.setUp()

    def setUp(self):
        self.commentCheckUI.btn_check.clicked.connect(self.btn_checkClicked)
        self.useAutoComment = self.parent.ui.actionmenu2.isChecked()

    def btn_checkClicked(self):
        error = False
        URL = self.commentCheckUI.lineEdit_URL.text()
        driver = webdriver.Chrome(ChromeDriverManager().install())

        userID = URL.split('/')[3]
        useAutoLogin = self.parent.ui.actionmenu1.isChecked()
        AutoLogin.login(AutoLogin, driver, useAutoLogin)

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
            logWriter.writeError("Lodding Fali : comiID, 댓글창 클릭 실패")
            driver.close()

        commentPageList = self.commentPageListSearch(driver)

        # 댓글 리스트 저장
        for i in range(len(commentPageList)):
            if len(commentPageList) != 1:
                commentPageList[i].click()
            time.sleep(1)
            if not error:
                try:
                    elem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'u_cbox_btn_recomm')))
                    commentList = driver.find_elements(By.CLASS_NAME, 'u_cbox_btn_recomm')

                except:
                    error = True
                    logWriter.writeError("Lodding Fali : u_cbox_btn_recomm, 댓글 리스트 저장 실패")
                    driver.close()

            if not error:
                # 댓글 관리 (좋아요, 창 띄우기)
                self.commentLike(commentList, driver)
                windowCount = len(driver.window_handles)
                if windowCount != 1:
                    self.likePost(driver, windowCount)

            driver.switch_to.window(driver.window_handles[0])
            driver.switch_to.frame('mainFrame')

            commentPageList = self.commentPageListSearch(driver)


        mainFunction.driverQuitAll(driver)

    def commentLike(self, commentList, driver):
        for i in range(len(commentList)):
            commentLike = commentList[i]
            try:
                isLen1 = len(commentLike.get_attribute('outerHTML').split('class="')[1].split('"')[0].split(" ")) == 1
            except:
                logWriter.writeError('commentLike error : ' + str(commentLike))

            if isLen1:
                # 좋아요
                time.sleep(0.1)
                try:
                    commentLike.click()
                except:
                    commentList = driver.find_elements(By.CLASS_NAME, 'u_cbox_btn_recomm')
                    commentLike = commentList[i]
                    time.sleep(1)
                    commentLike.click()

                commentBox = commentLike.find_element(By.XPATH, '../../..')
                commentID = commentBox.find_element(By.CLASS_NAME, 'u_cbox_info_main')
                comentIDURL = commentID.get_attribute('outerHTML').split('"')[3]
                comentIDURL = comentIDURL.replace('https://blog', 'https://m.blog')
                driver.execute_script('window.open("' + comentIDURL + '");')
                driver.switch_to.window(driver.window_handles[0])
                driver.switch_to.frame('mainFrame')
                j = 0
                while True:
                    if len(commentLike.get_attribute('outerHTML').split('class="')[1].split('"')[0].split(" ")) == 2:
                        break
                    else:
                        time.sleep(0.1)
                        j += 1

                    if j > 100:
                        logWriter.writeError("line 103 error")
                        break

    def likePost(self, driver, windowCount):
        for i in range(windowCount - 1):
            error = self.searchLikeButton(driver)

            if not error:
                likeOfPost = driver.find_elements(By.CLASS_NAME, 'u_likeit_list_btn')
                for j in range(len(likeOfPost)):
                    if likeOfPost[j].aria_role == 'generic':
                        if 'off' in likeOfPost[j].get_attribute('outerHTML').split('"')[1]:
                            likeOfPost[j - 1].click()
                            time.sleep(0.1)
                            commentWriter.write(driver, self.useAutoComment)

            driver.close()

    def searchLikeButton(self, driver):
        error = False
        driver.switch_to.window(driver.window_handles[1])
        try:
            elem = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'view_type_btn__z6Hlf')))
        except:
            logWriter.writeError("Lodding Fali : view_type_btn__z6Hlf")
            error = True

        time.sleep(0.2)
        try:
            elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn__xjUPw')))
        except:
            logWriter.writeError("Lodding Fali : btn__xjUPw")
            error = True

        if not error:
            buttonList = driver.find_elements(By.CLASS_NAME, 'btn__xjUPw')
            for button in buttonList:
                if button.accessible_name == '카드형 보기':
                    button.click()

        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'card__WjujK')))
        except:
            logWriter.writeError("Lodding Fali : card__WjujK")
            error = True

        if not error:
            time.sleep(0.1)
            driver.find_element(By.CLASS_NAME, 'card__WjujK').click()
            moblieURL = driver.current_url
            PCURL = moblieURL.replace('https://m.blog', 'https://blog')
            driver.get(url=PCURL)
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'u_likeit_list_btn')))
        except:
            logWriter.writeError("Lodding Fali : u_likeit_list_btn, 좋아요 버튼 탐색 실패")
            error = True

        return error

    def commentPageListSearch(self, driver):
        commentPageList = []
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'u_cbox_page')))
            commentPageList = driver.find_elements(By.CLASS_NAME, 'u_cbox_page')
        except:
            logWriter.writeError("Lodding Fali : 댓글 페이지 리스트 개수 호출 실패")

        return commentPageList