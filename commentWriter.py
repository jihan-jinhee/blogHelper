from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logWriter
import pyperclip
import pyautogui

def write(driver):
    text = "포스팅 잘 보고 갑니다~\n 오늘 정말 춥데요! 건강 조심하세요~"
    write2(driver, text)

def write2(driver, text):
    driver.switch_to.frame('mainFrame')
    commentUse = findCommentLocation(driver)
    if commentUse:
        writeComment(text)
        try:
            commentSend = driver.find_element(By.CLASS_NAME, 'u_cbox_btn_upload')
            commentSend.click()
        except:
            logWriter.writeError("Comment Send Fail")


def findCommentLocation(driver):
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn_comment')))
        commentPage = driver.find_elements(By.CLASS_NAME, 'btn_comment')
        commentPage[1].click()
    except:
        logWriter.writeError("No Comment")
        return False

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'u_cbox_write_wrap')))
        commentWindow = driver.find_elements(By.CLASS_NAME, 'u_cbox_write_wrap')
        commentWindow[0].click()
    except:
        logWriter.writeError("Comment Window Click Fail")
        return False

    return True

def writeComment(text):
    texts = text.split('\n')
    for i in range(len(texts)):
        pyperclip.copy(texts[i])
        pyautogui.hotkey('ctrl', 'v')
        if not i == len(texts) - 1:
            pyautogui.press('enter')