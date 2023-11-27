import time
from PyQt5 import QtWidgets, uic
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from AutoLogin import AutoLogin
import commentWriter
import logWriter
import mainFunction

class NeighborPostLike(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.parent = parent
        self.neighborPostLikeUI = uic.loadUi("./resources//neighborPostLike.ui")
        self.setUp()

    def setUp(self):
        self.neighborPostLikeUI.btn_startAndPause.clicked.connect(self.btn_startAndPauseClicked)
        self.useAutoComment = self.parent.ui.actionmenu2.isChecked()

    def naverLogin(self):
        useAutoLogin = self.parent.ui.actionmenu1.isChecked()
        self.driver = AutoLogin.naverLogin(AutoLogin, useAutoLogin)

    def likePost(self):
        page = 1
        alreadyCheck = 0
        checkPost = 0

        while (True):
            blogHome = "https://section.blog.naver.com/BlogHome.naver?directoryNo=0&currentPage=" + str(page) + "&groupId=0"

            self.driver.get(url=blogHome)

            # u_likeit_list_btn 정보 찾기
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'u_likeit_list_btn')))
            except:
                logWriter.writeError("u_likeit_list_btn Search Fali : ")

            likeOfPost = self.driver.find_elements(By.CLASS_NAME, 'u_likeit_list_btn')
            infoPost = self.driver.find_elements(By.CLASS_NAME, 'comments')
            windowCount = 0
            likeStatus = None
            Pass = False
            for i in range(len(likeOfPost)):
                try:
                    likeStatus = likeOfPost[i].get_attribute('outerHTML').split('"')[3]
                except:
                    time.sleep(30)
                    Pass = True
                if 'off' in likeStatus or Pass:
                    likeOfPost[i].click()
                    #댓글기능 추가
                    try:
                        postURL = infoPost[i].get_attribute('innerHTML').split("data-url=")[1].split(" ")[0][1:-1]
                    except:
                        logWriter.writeError("postURL Search Fali : " + str(postURL))
                    try:
                        self.driver.execute_script('window.open("' + postURL + '");')
                    except:
                        logWriter.writeError("Lodding Fali : " + str(postURL))
                    windowCount += 1
                    time.sleep(0.1)
                else:
                    alreadyCheck += 1

            useComment = True
            for j in range(windowCount):
                try:
                    self.driver.switch_to.window(self.driver.window_handles[1])
                except:
                    logWriter.writeError("switch window Fail")

                try:
                    self.driver.switch_to.frame('mainFrame')
                except:
                    logWriter.writeError("MainFrame Switch Fail")
                    commentUse = False

                if useComment:
                    commentWriter.write(self.driver, self.useAutoComment) # fail 추가해야함.

                try:
                    self.driver.close() #self.driver.current_url 하면 exception 나거든.
                except:
                    useComment = False
                    logWriter.writeError("Driver Close Fail")
                    self.driver.close()


                time.sleep(0.1)

            checkPost += windowCount
            try:
                self.driver.switch_to.window(self.driver.window_handles[0])
            except:
                logWriter.writeError("Lodding Fali : page :" + str(page) + ", post :" + str(checkPost))

            page += 1
            if alreadyCheck > 1000:  # or page > 500
                logWriter.writeInfo("page : " + str(page) + ", post : " + str(checkPost))
                mainFunction.driverQuitAll(self.driver)
                break

    def btn_startAndPauseClicked(self):
        self.naverLogin()
        self.likePost()

