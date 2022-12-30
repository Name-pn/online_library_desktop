from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QLabel, QSizePolicy
import Program.Constrains

import Components.Comments
from API.apps import Books, Authors, Users, UserTypes
from Program.Networking import NETWORK_MANAGER
from Components.ScaledPicture import ScaledPicture

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
        self.picture.setFixedSize(350, 500)
        self.vl = QtWidgets.QVBoxLayout(self)
        self.hlSup = QtWidgets.QHBoxLayout()
        self.vlSup = QtWidgets.QVBoxLayout()
        self.name = QLabel()
        self.name.setText(name)

        self.name.setFont(Program.Constrains.DEFAULT_CONSTRAINS.titleFont)
        self.name.setSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)

        self.characters1 = QtWidgets.QTextBrowser()
        self.characters1.setText('Год написания: ' + str(self.book.get('year_of_writing')) + '\n' +
                                               'Автор: ' + author['name'] + ' ' + author['surname'])
        self.characters1.setSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.characters1.setFont(Program.Constrains.DEFAULT_CONSTRAINS.mainFont)
        self.descriptionText = QtWidgets.QTextBrowser()
        self.descriptionText.setText(self.book.get('description'))
        self.descriptionText.setFont(Program.Constrains.DEFAULT_CONSTRAINS.mainFont)
        self.descriptionText.setAlignment(QtCore.Qt.AlignmentFlag.AlignJustify)
        self.descriptionText.setSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.user = Users.get_user_type()
        self.comments = Components.Comments.Comments(slug, self.user)
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
            self.button.setFont(Program.Constrains.DEFAULT_CONSTRAINS.mainFont)
            self.vlSup.addWidget(self.button)

        self.vl.addWidget(self.comments)
        self.name.setStyleSheet("QLabel {background-color: yellow;}")
        self.name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    def initAddButtom(self, f):
        self.button.clicked.connect(lambda: f(self.book['slug']))