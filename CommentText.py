from PyQt5 import QtWidgets, uic

class CommentText(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.commentTextUI = uic.loadUi("./resources//commentText.ui")
        self.setUp()

    def setUp(self):
        self.commentTextUI.btn_saveCommentText.clicked.connect(self.btn_saveCommentTextClicked)
        self.loadCommentInfo()

    def btn_saveCommentTextClicked(self):
        comment = self.commentTextUI.textEdit_comment.toPlainText()
        self.saveInfo(comment)

    def saveInfo(self, comment):
        File = open("./resources/commentText.txt", "w")
        print(comment, file=File)
        self.commentTextUI.close()

    def loadCommentInfo(self):
        if self.isHaveInfo():
            comment = self.getCommentInfo()
            self.commentTextUI.textEdit_comment.setText(str(comment))

    def isHaveInfo(self):
        comment = CommentText.getCommentInfo(self)
        if comment == None:
            return False
        else:
            return True

    def getCommentInfo(self):
        try:
            File = open("./resources/commentText.txt", "r")
        except:
            return None

        lines = File.readlines()
        comments = []
        for i in range(len(lines)):
            if lines[len(lines) - i - 1] != '\n':
                comments.insert(0, lines[len(lines) - i - 1])
        comment = ''.join(comments)

        return comment