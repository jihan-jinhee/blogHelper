import logging
import time
import os

if not os.path.exists("./log"):
    os.mkdir("log")

logDate = time.strftime("%Y_%m%d")
logTime = time.strftime("%Y_%m%d_%H%M")

if not os.path.exists("./log//" + logDate):
    os.mkdir("./log//" + logDate)

Log_Format = "%(levelname)s %(asctime)s - %(message)s"
filename = "./log//" + logDate + "//" + logTime + "_logfile.log"
logging.basicConfig(filename=filename,
                    format=Log_Format,
                    level=logging.INFO)
logger = logging.getLogger()

def writeInfo(text : str):
    logger.info(text)

def writeError(text : str):
    logger.error(text)

writeInfo("Program Start!!")