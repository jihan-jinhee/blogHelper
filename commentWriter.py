import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logWriter
from CommentText import CommentText

def write(driver, useAutoComment):
    if useAutoComment:
        text = CommentText.getCommentInfo(CommentText)
    else:
        text = "정성 가득 포스팅 잘 보고 갑니다~"
    write2(driver, text)

def write2(driver, text):
    commentUse = True

    if commentUse:
        commentWindow = findCommentLocation(driver)
        if not commentWindow:
            commentUse = False

    if commentUse:
        error = writeComment(commentWindow, text)
        if not error:
            try:
                commentSend = driver.find_element(By.CLASS_NAME, 'u_cbox_btn_upload')
                commentSend.click()
                time.sleep(2)
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
    error = False
    try:
        commentWindow.send_keys(text)
    except:
        logWriter.writeError("Comment Write Fail : ")
        error = True

    return error