from PyQt6 import QtGui
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QListWidget, QAbstractItemView, QScrollArea, QSizePolicy, QVBoxLayout, \
    QLabel, QListWidgetItem, QTextBrowser, QTextEdit, QHBoxLayout, QPushButton

import API.apps

class CommentItem(QListWidgetItem):
    def __init__(self, text, id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = text
        self.setText(text)
        self.id = id

    def getId(self):
        return self.id

class Comments(QWidget):
    def __init__(self, slug, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.MainVL = QVBoxLayout(self)
        self.name = QLabel()
        self.list = QListWidget()
        self.user = user
        self.MainVL.addWidget(self.list)
        self.slug = slug
        self.initUI()

    def paintEvent(self, a0: QtGui.QPaintEvent):
        painter = QtGui.QPainter(self)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 188))
        painter.setBrush(brush)
        painter.drawRect(0, 0, self.width(), self.height())

    def dictToComment(self, dict):
        res = dict['user'] + ': ' + dict['text'] + '\nОценка ' + str(dict['score'])
        return res

    def initUI(self):
        self.name.setText('Комментарии')
        self.name.setFont(QtGui.QFont("Times new roman", 16))
        self.list.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        self.list.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.list.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.list.setFont(QtGui.QFont("Times new roman", 16))
        self.list.setIconSize(QSize(50, 50))
        self.iconGreen = QIcon('./Images/ComLabelGreen.png')
        self.iconYellow = QIcon('./Images/ComLabelYellow.png')
        self.iconRed = QIcon('./Images/ComLabelRed.png')
        self.initList()
        if self.user != API.apps.UserTypes.GUEST:
            self.initCommentPost()
            self.initCommentDelete()

    def initList(self):
        self.properties = API.apps.Comments.get_comments(book=self.slug)
        self.list.clear()
        for el in self.properties:
            ins_el = CommentItem(self.dictToComment(el), el['id'])
            num = el['score']
            if num is None:
                num = 0
            if num >= 3.5:
                ins_el.setIcon(self.iconGreen)
            elif num >= 2.5:
                ins_el.setIcon(self.iconYellow)
            else:
                ins_el.setIcon(self.iconRed)
            self.list.addItem(ins_el)

    def postAndUpdate(self, slug, score, comment):
        if score == '' or comment == '':
            return
        API.apps.Comments.post_comment(slug, score, comment)
        self.initList()

    def deleteComments(self):
        selections = self.list.selectedItems()
        for el in selections:
            integer = el.getId()
            API.apps.Comments.remove_comment(integer)
        self.initList()

    def initCommentPost(self):
        self.postMainHL = QHBoxLayout()
        self.postVL1 = QVBoxLayout()
        self.postVL2 = QVBoxLayout()
        self.postVL3 = QVBoxLayout()

        self.button = QPushButton('Отправить комментарий')
        self.button.setFont(QtGui.QFont("Times new roman", 16))

        self.postText = QTextBrowser()
        self.postText.setFont(QtGui.QFont("Times new roman", 16))
        self.postText.setText('Введите текст вашего комметария: ')

        self.postScore = QTextBrowser()
        self.postScore.setFont(QtGui.QFont("Times new roman", 16))
        self.postScore.setText('Введите вашу оценку: ')

        self.postEditText = QTextEdit()
        self.postEditText.setFont(QtGui.QFont("Times new roman", 16))

        self.postEditScore = QTextEdit()
        self.postEditScore.setFont(QtGui.QFont("Times new roman", 16))

        self.postVL1.addWidget(self.postText)
        self.postVL1.addWidget(self.postScore)

        self.postVL2.addWidget(self.postEditText)
        self.postVL2.addWidget(self.postEditScore)

        self.postVL3.addWidget(self.button)

        self.postMainHL.addLayout(self.postVL1)
        self.postMainHL.addLayout(self.postVL2)
        self.postMainHL.addLayout(self.postVL3)

        self.MainVL.addLayout(self.postMainHL)

        self.button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        self.button.clicked.connect(lambda: self.postAndUpdate(self.slug,
                                                               self.postEditScore.toPlainText(),
                                                               self.postEditText.toPlainText()))

    def initCommentDelete(self):
        self.list.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.deleteButton = QPushButton('Удалить выделенные комментарии')
        self.deleteButton.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        self.deleteButton.setFont(QtGui.QFont("Times new roman", 16))
        self.postVL3.addWidget(self.deleteButton)

        self.deleteButton.clicked.connect(lambda: self.deleteComments())
