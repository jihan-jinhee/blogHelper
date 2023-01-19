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

        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'card__WjujK')))
        except:
            logWriter.writeError("Lodding Fali : card__WjujK")
            error = True

        time.sleep(0.1)
        driver.find_element(By.CLASS_NAME, 'card__WjujK').click()
        return error