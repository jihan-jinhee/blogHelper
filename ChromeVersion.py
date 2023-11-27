import webbrowser

from PyQt5 import QtWidgets, uic

class ChromeVersion(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.ChromeVersionUI = uic.loadUi("./resources//chromeVersion.ui")
        self.setUp()

    def setUp(self):
        self.ChromeVersionUI.btn_saveChromeVersion.clicked.connect(self.btn_saveChromeVersion)
        self.ChromeVersionUI.manual_button.clicked.connect(self.btn_manual)
        self.loadChromeVersionInfo()

    def btn_saveChromeVersion(self):
        chromeVersion = self.ChromeVersionUI.textEdit_chromeVersion.toPlainText()
        self.saveInfo(chromeVersion)

    def btn_manual(self):
        webbrowser.open("https://support.google.com/chrome/answer/95414?hl=ko&co=GENIE.Platform%3DDesktop")

    def saveInfo(self, chromeVersion):
        File = open("./resources/chromeVersion.txt", "w")
        print(chromeVersion, file=File)
        self.ChromeVersionUI.close()

    def loadChromeVersionInfo(self):
        if self.isHaveInfo():
            version = self.getChromeVersionInfo()
            self.ChromeVersionUI.textEdit_chromeVersion.setText(str(version))

    def isHaveInfo(self):
        version = ChromeVersion.getChromeVersionInfo(self)
        if version is None:
            return False
        else:
            return True

    def getChromeVersionInfo(self):
        try:
            File = open("./resources/chromeVersion.txt", "r")
        except:
            return None

        lines = File.readlines()
        version = []
        for i in range(len(lines)):
            if lines[len(lines) - i - 1] != '\n':
                version.insert(0, lines[len(lines) - i - 1])
        return ''.join(version)