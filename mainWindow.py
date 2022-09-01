import time
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
import os
from PIL import Image

class MainWindow(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = uic.loadUi("./resources//MainWidget.ui")
        self.progressBarUI = uic.loadUi("./resources//progressbar.ui")
        self.progressBarUI.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setUp()
        self.ui.show()

    def setUp(self):
        self.ui.btn_watermark.clicked.connect(self.btn_watermarkClicked)

    def btn_watermarkClicked(self):
        self.progressBarUI.show()
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folderpath is None or folderpath == "":
            return

        files = os.listdir(folderpath)
        count = 0
        for file in files:
            if 'png' in file or 'jpg' in file:
                count += 1
        progressPitch = int(100 / count)

        count = 0
        for file in files:
            if 'png' in file or 'jpg' in file:
                count +=1
                imagePath = folderpath + "\\" + file
                imgResult = self.makeWatermark(imagePath)
                self.saveResult(imgResult, file)
                time.sleep(2)
                self.progressBarUI.progressBar.setValue(progressPitch * count)

        self.progressBarUI.close()

    def makeWatermark(self, imagePath):
        img_watermark = None
        img_watermarkPath = os.getcwd() + "\\resources\\watermark.png"
        if os.path.exists(img_watermarkPath):
            img_watermark = Image.open(img_watermarkPath)

            img_origin = Image.open(imagePath)
            Xdim_origin, Ydim_origin = img_origin.size
            resizeRatio = Xdim_origin / 1000

            img_resizeWatermark, resized_Xdim, resized_Ydim = self.resizeWatermark(resizeRatio, img_watermark)

            image = Image.open(imagePath)
            image.paste(img_resizeWatermark, (Xdim_origin - resized_Xdim, Ydim_origin - resized_Ydim))
            return image

    def resizeWatermark(self, resizeRatio, img_watermark):
        Xdim_watermark, Ydim_watermark = img_watermark.size
        resized_Xdim = int(Xdim_watermark * resizeRatio)
        resized_Ydim = int(Ydim_watermark * resizeRatio)
        img_resizeWatermark = img_watermark.resize((resized_Xdim, resized_Ydim))
        return img_resizeWatermark, resized_Xdim, resized_Ydim

    def saveResult(self, imgResult, fileName):
        resultPath = os.getcwd() + "\\결과폴더"
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)

        imgResult.save(resultPath + "\\" + fileName)
