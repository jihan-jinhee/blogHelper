from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        i = 0
        for neighbor in deleteList:
            if i >= neighborCount:
                break
            proceed = True
            
            try:
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'search_input')))
                box = driver.find_elements(By.CLASS_NAME, 'search_input')
                box[0].clear()
                box[0].send_keys(neighbor) # 검색창 클릭
            except:
                proceed = False
                logWriter.writeError("neighbor delete: 검색창 클릭 실패")
                
            if proceed:
                try:
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'sim')))
                    btn_search = driver.find_elements(By.CLASS_NAME, 'sim')
                    btn_search[0].click()
        
                    time.sleep(0.5)
                except:
                    proceed = False
                    logWriter.writeError("neighbor delete: 검색 버튼 탐색 실패")
                    
            if proceed:
                try:
                    btn_del = driver.find_elements(By.XPATH, '//*[@id="ct"]/div[4]/div/ul/buddy/li/div[1]/div[2]/a[2]')
                    btn_del[0].click()
                except:
                    proceed = False
                    logWriter.writeError("neighbor delete: 검색 실패 (정상일수도)")
            
            if proceed:
                try:
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'r2')))
                    neighborDelteCheckBox = driver.find_elements(By.ID, 'r2')
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
                i += 1

        return True