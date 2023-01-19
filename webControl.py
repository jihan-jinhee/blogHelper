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
