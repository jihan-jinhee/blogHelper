from PyQt5 import QtWidgets, uic

class LetterCount(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.parent = parent
        self.letterCountUI = uic.loadUi("./resources//letterCount.ui")
        self.setUp()

    def setUp(self):
        self.letterCountUI.textEdit_letter.textChanged.connect(self.showCount)

    def showCount(self):
        (count, postCount, pureCount) = self.getCount()
        self.letterCountUI.lbl_count.setText(str(count))
        self.letterCountUI.lbl_postCount.setText(str(postCount))

    def getCount(self):
        text = self.letterCountUI.textEdit_letter.toPlainText()
        textCount = len(text)
        (postCount, pureCount) = self.pureTextCount(text)
        return (textCount, postCount, pureCount)

    def pureTextCount(self, text):
        text = text.replace("￼", "")
        text = text.replace("\ufeff", "")
        textList = text.split("\n")

        i = 0
        while(True):
            if i >= len(textList):
                break

            try:
                line = textList[i]
            except:
                # 줄바꿈 문제
                print("pass")

            if self.removeGarbage(text = textList[i]):
                textList.remove(textList[i])
            elif textList[i] == "":
                textList.remove(textList[i])
            else:
                i += 1

        postText = ''.join(textList)
        postCount = len(postText)

        pureText = postText.replace(' ', '')
        pureCount = len(pureText)
        return (postCount, pureCount)

    def removeGarbage(self, text):
        garbageList = ["사진 편집", "사진 삭제", "사진 설명",
                       "삭제삭제", "작게문서", "너비문서 너비옆트임옆트임", "업로드 준비중입니다."]
        for garbage in garbageList:
            if garbage in text:
                return True

        return False
