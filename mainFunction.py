import os
import logWriter

def killProcess():
    try:
        os.system("taskkill /f /im chromedriver.exe /t")
    except Exception as e:
        logWriter.writeError("chromedriver taskKill Fail")

def driverQuitAll(driver):
    driver.quit()
    killProcess()