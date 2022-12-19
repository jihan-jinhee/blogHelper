from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logWriter

def write(driver):
    text = "포스팅 잘 보고 갑니다~\n오늘 하루도 고생하셨습니다!"
    print("test")
    write2(driver, text)

def write2(driver, text):
    commentUse = True
    try:
        driver.switch_to.frame('mainFrame')
    except:
        logWriter.writeError("MainFrame Switch Fail")
        commentUse = False

    if commentUse:
        commentWindow = findCommentLocation(driver)
        commentUse = True

    if commentUse:
        writeComment(commentWindow, text)
        try:
            commentSend = driver.find_element(By.CLASS_NAME, 'u_cbox_btn_upload')
            commentSend.click()
        except:
            logWriter.writeError("Comment Send Fail")


def findCommentLocation(driver):
    commentWindow = False
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn_comment')))
        commentPage = driver.find_elements(By.CLASS_NAME, 'btn_comment')
        commentPage[1].click()
    except:
        logWriter.writeError("No Comment")
        return False

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'u_cbox_write_wrap')))
        commentWindow = driver.find_element(By.CLASS_NAME, 'u_cbox_text')
    except:
        logWriter.writeError("Comment Window Click Fail")
        return False

    return commentWindow

def writeComment(commentWindow, text):
    try:
        commentWindow.send_keys(text)
    except:
        logWriter.writeError("Comment Write Fail : ")