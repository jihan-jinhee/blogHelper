import multiprocessing
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

def multiProcess(function1, function2, page):
    driver = function1()
    function2(driver, 1)

def multiProcessWork(numberOfProcess, function1, function2): # 자식 프로세스를 실행할 방안 필요
    if function1.__name__ == 'naverLogin' and function2.__name__ == 'likePost':
        pool = multiprocessing.Pool(processes=numberOfProcess)

        poolList = []
        for i in range(numberOfProcess):
            poolParamList = [function1, function2]
            poolParamList.append(numberOfProcess * 10 + 1)
            poolList.append(poolParamList)

        pool.starmap(multiProcess, poolList)
        pool.close()
        pool.join()
