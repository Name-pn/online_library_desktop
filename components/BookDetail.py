from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtWidgets import QLayout, QLabel, QSizePolicy

import components.Comments
from API.apps import Books, Authors, Users, UserTypes
from Program.Networking import NETWORK_MANAGER
from components.ScaledPicture import ScaledPicture

class BookDetailComponent(QtWidgets.QWidget):

    def __init__(self, slug: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.book = Books.get_detail(slug)
        author = Authors.get_detail(self.book['author'])
        name = self.book.get('title')
        imageUrl = self.book.get('cover')
        if imageUrl is None:
            self.picture = ScaledPicture('./Images/book.png')
        else:
            image = NETWORK_MANAGER.httpGetImage(QUrl(imageUrl))
            self.picture = ScaledPicture('', image)
        self.picture.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        self.vl = QtWidgets.QVBoxLayout(self)
        self.hlSup = QtWidgets.QHBoxLayout()
        self.vlSup = QtWidgets.QVBoxLayout()
        self.name = QLabel()
        self.name.setText(name)

        self.name.setFont(QtGui.QFont("Times new roman", 20))
        self.name.setSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)

        self.characters1 = QtWidgets.QTextBrowser()
        self.characters1.setText('Год написания: ' + str(self.book.get('year_of_writing')) + '\n' +
                                               'Автор: ' + author['name'] + ' ' + author['surname'])
        self.characters1.setSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.characters1.setFont(QtGui.QFont("Times new roman", 16))
        self.descriptionText = QtWidgets.QTextBrowser()
        self.descriptionText.setText(self.book.get('description'))
        self.descriptionText.setFont(QtGui.QFont("Times new roman", 16))
        self.descriptionText.setAlignment(QtCore.Qt.AlignmentFlag.AlignJustify)
        self.descriptionText.setSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.user = Users.get_user_type()
        self.comments = components.Comments.Comments(slug, self.user)
        self.initUI()

    def initUI(self):

        self.vl.addWidget(self.name)
        self.hlSup.addWidget(self.picture)

        self.vlSup.addWidget(self.characters1)
        self.vlSup.addWidget(self.descriptionText)
        self.hlSup.addLayout(self.vlSup)

        self.vl.addLayout(self.hlSup)

        if self.user != UserTypes.GUEST:
            self.button = QtWidgets.QPushButton('Добавить на книжную полку')
            self.button.setFont(QtGui.QFont("Times new roman", 16))
            self.vlSup.addWidget(self.button)

        self.vl.addWidget(self.comments)
        self.name.setStyleSheet("QLabel {background-color: yellow;}")
        self.name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    def initAddButtom(self, f):
        self.button.clicked.connect(lambda: f(self.book['slug']))