from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webControl import WebControl
from webdriver_manager.chrome import ChromeDriverManager
import logWriter
import time
import re

class BlogNeighbor():
    def __init__(self):
        pass

    def postLikeNeighbor(self, ID, postNum):
        useAutoLogin = False
        neighborList = []
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(2)
        URL = 'https://m.blog.naver.com/' + str(ID)
        driver.get(url=URL)
        WebControl.showCardMobile(self= WebControl, driver= driver)

        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'card__WjujK')))
        except:
            logWriter.writeError("Lodding Fali : card__WjujK")
            error = True

        time.sleep(0.1)
        posts = driver.find_elements(By.CLASS_NAME, 'card__WjujK')
        i = 0
        for post in posts:
            if i>=postNum:
                break
            postURL = post.get_attribute('outerHTML').split('data-url=')[1].split(" ")[0][1:-1]
            driver.execute_script('window.open("' + postURL + '");')
            i +=1

        for postNum in range(i):
            if len(driver.window_handles) == 1:
                break
            driver.switch_to.window(driver.window_handles[1])
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn_like_more')))
                a = driver.find_elements(By.CLASS_NAME, 'btn_like_more')
            except:
                logWriter.writeError("포스팅 오픈 에러 : " + str(driver.current_url))

            if a != []:
                try:
                    a[0].click()
                except:
                    a[1].click()

                WebControl.scrollDownDeep(self=WebControl, driver=driver)

                userList = driver.find_elements(By.CLASS_NAME, 'blogname__PmDH5')
                for user in userList:
                    if not user.text in neighborList:
                        neighborList.append(user.text)

            driver.close()
        return set(neighborList)

    def loadNeighborList(self, filePath):
        neighborFile = open(filePath, 'r', encoding='UTF8')
        neighborFile.readline()
        neighborData = neighborFile.readline()
        neighborTitles = neighborData.split("title=")

        neighborList = []
        for title in neighborTitles:
            try:
                neighbor = re.search('"(.+?)"', title).group(1)
                neighborList.append(neighbor)
            except:
                pass

        return set(neighborList)
