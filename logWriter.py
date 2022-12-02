import logging
import time
import os

if not os.path.exists("./log"):
    os.mkdir("log")

Log_Format = "%(levelname)s %(asctime)s - %(message)s"
filename = "./log//" + time.strftime("%Y_%m%d_%H%M") + "_logfile.log"
logging.basicConfig(filename=filename,
                    format=Log_Format,
                    level=logging.INFO)
logger = logging.getLogger()

def writeInfo(text : str):
    logger.info(text)

def writeError(text : str):
    logger.error(text)

writeInfo("Program Start!!")