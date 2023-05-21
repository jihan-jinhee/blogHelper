from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import logWriter
import time

class WebControl:
    def __init__(self):
        pass

    def showCardMobile(self, driver):
        error = False
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

        return error

    def scrollDownDeep(self, driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            # 끝까지 스크롤 다운
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # 1초 대기
            time.sleep(1)

            # 스크롤 다운 후 스크롤 높이 다시 가져옴
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

class blogAdmin:
    def __init__(self):
        pass

    def moveBlogAdmin(self, driver, ID):
        driver.get(url='https://m.blog.naver.com/BuddyList.naver?blogId=' + ID)

    def moveAdminNeighborGroup(self, driver):
        a = driver.find_elements(By.ID, 'buddylist_config_anchor')
        a[0].click()

    def deleteNeighborInGroup(self, driver, deleteList, neighborCount):
        count = 0
        i = 0
        while i < len(deleteList):
            if count >= neighborCount:
                break
            proceed = True

            if "페페의 냠냠 아일랜드" in deleteList[i]:
                proceed = False

            if len(deleteList[i]) < 4:
                proceed = False
            
            try:
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'search_input__OUlaE')))
                box = driver.find_elements(By.CLASS_NAME, 'search_input__OUlaE')
                box[0].clear()
                box[0].send_keys(deleteList[i]) # 검색창 클릭
                box[0].send_keys(Keys.RETURN)
            except:
                proceed = False
                logWriter.writeError("neighbor delete: 검색창 클릭 실패")
                
            # if proceed:
            #     try:
            #         WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'sim')))
            #         btn_search = driver.find_elements(By.CLASS_NAME, 'sim')
            #         btn_search[0].click()
            #
            #         time.sleep(0.5)
            #     except:
            #         proceed = False
            #         logWriter.writeError("neighbor delete: 검색 버튼 탐색 실패")
                    
            if proceed:
                try:
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'more_btn_icon__rZd7v')))
                    btn_more = driver.find_elements(By.CLASS_NAME, 'more_btn_icon__rZd7v')
                    btn_more[0].click()
                except:
                    proceed = False
                    i += 10
                    logWriter.writeError("neighbor delete: 검색 실패 (정상일수도)")

            if proceed:
                try:
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'menu_item___2HmB')))
                    btn_delete = driver.find_elements(By.CLASS_NAME, 'menu_item___2HmB')
                    btn_delete[3].click()
                except:
                    proceed = False
                    logWriter.writeError("delete button search fail")

            if proceed:
                try:
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), '서로이웃과 이웃을 모두 취소합니다.')]")))
                    neighborDelteCheckBox = driver.find_elements(By.XPATH, "//label[contains(text(), '서로이웃과 이웃을 모두 취소합니다.')]")
                    neighborDelteCheckBox[0].click()
                except:
                    proceed = False
                    logWriter.writeError("neighbor delete: radio 버튼 탐색 실패")
                    
            if proceed:
                try:
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn_ok')))
                    btn_ok = driver.find_elements(By.CLASS_NAME, 'btn_ok')
                    btn_ok[0].click()
                except:
                    proceed = False
                    logWriter.writeError("neighbor delete: ok 버튼 탐색 실패")

            if proceed:
                try:
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn_100')))
                    btn_finish = driver.find_elements(By.CLASS_NAME, 'btn_100')
                    btn_finish[0].click()
                except:
                    proceed = False
                    logWriter.writeError("neighbor delete: 삭제 완료 버튼 탐색 실패")

            if proceed:
                count += 1

            i += 1

        return True