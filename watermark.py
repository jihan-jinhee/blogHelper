import time
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
from PyQt5.QtCore import Qt
import os
from PIL import Image

class Watermark(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.folderpath = None
        self.folderChooseUI = uic.loadUi("./resources//folderChoose.ui")
        self.progressBarUI = uic.loadUi("./resources//progressbar.ui")
        self.progressBarUI.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setUp()

    def setUp(self):
        self.folderChooseUI.btn_folderChoose.clicked.connect(self.btn_folderChooseClicked)
        self.progressBarUI.btn_watermark.clicked.connect(self.btn_watermarkClicked)

    def btn_folderChooseClicked(self):
        self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if self.folderpath is None or self.folderpath == "":
            return
        self.folderChooseUI.label_folderPath.setText(self.folderpath)

        qr = self.progressBarUI.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        self.progressBarUI.move(cp.x(), cp.y() + 50)
        self.progressBarUI.show()

    def btn_watermarkClicked(self):
        self.progressBarUI.progressBar.setValue(0)
        if self.folderpath is None or self.folderpath == "":
            self.progressBarUI.close()
            return

        files = os.listdir(self.folderpath)
        totalCount = 0
        for file in files:
            if 'png' in file or 'jpg' in file:
                totalCount += 1
        progressPitch = 100 / totalCount

        startTime = time.time()
        count = 0
        for file in files:
            if 'png' in file or 'jpg' in file:
                count +=1
                imagePath = self.folderpath + "\\" + file
                imgResult = self.makeWatermark(imagePath)
                self.saveResult(imgResult, file)
                self.progressBarUI.progressBar.setValue(int(progressPitch * count))

                processingTime = int(time.time() - startTime)
                remainCount = totalCount - count
                remainTpropotion = remainCount / count
                remainTime = int(processingTime * remainTpropotion)
                self.showTime(processingTime, remainTime)
                self.progressBarUI.label_processing.setText(str(count) + "/" + str(totalCount))

        self.folderChooseUI.close()
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
        resultPath = self.folderpath + "\\워터마크 사진폴더"
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)

        imgResult.save(resultPath + "\\" + fileName)

    def showTime(self, time, remainTime):
        timeSec = int(time % 60)
        timeMin = int(time / 60)
        timeHour = int(time / 3600)

        rTimeSec = int(remainTime % 60)
        rTimeMin = int(remainTime / 60)
        rTimeHour = int(remainTime / 3600)

        if timeHour == 0:
            if timeMin == 0:
                self.progressBarUI.label_processTime.setText(str(timeSec) + "초")

            else:
                self.progressBarUI.label_processTime.setText(str(timeMin) + "분" + str(timeSec) + "초")

        else:
            self.progressBarUI.label_processTime.setText(str(timeHour) + "시간" + str(timeMin) + "분" + str(timeSec) + "초")

        if rTimeHour == 0:
            if rTimeMin == 0:
                self.progressBarUI.label_remainTime.setText(str(rTimeSec) + "초")

            else:
                self.progressBarUI.label_remainTime.setText(str(rTimeMin) + "분" + str(rTimeSec) + "초")

        else:
            self.progressBarUI.label_remainTime.setText(str(rTimeHour) + "시간" + str(rTimeMin) + "분" + str(rTimeSec) + "초")
