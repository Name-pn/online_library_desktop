from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QLayout, QLabel

from API.apps import Books, Authors, Users, UserTypes
from Program.Networking import NETWORK_MANAGER
from componets.ScaledPicture import ScaledPicture

class BookDetailComponent(QtWidgets.QWidget):

    def __init__(self, slug: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.book = Books.get_detail(slug)
        author = Authors.get_detail(self.book['author'])
        name = self.book.get('title')
        imageUrl = self.book.get('cover')
        if imageUrl is None:
            self.picture = ScaledPicture('./images/book.png')
        else:
            image = NETWORK_MANAGER.httpGetImage(QUrl(imageUrl))
            self.picture = ScaledPicture('', image)

        self.vl = QtWidgets.QVBoxLayout(self)
        self.hlSup = QtWidgets.QHBoxLayout()
        self.vlSup = QtWidgets.QVBoxLayout()
        self.name = QLabel()
        self.name.setText(name)

        self.name.setFont(QtGui.QFont("Helvetica", 16))
        self.name.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.characters1 = QtWidgets.QTextEdit('Год написания: ' + str(self.book.get('year_of_writing')))
        self.characters1.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        self.characters2 = QtWidgets.QTextEdit('Автор: ' + author['name'] + ' ' + author['surname'])
        self.descriptionText = QtWidgets.QTextEdit(self.book.get('description'))
        self.characters2.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        self.descriptionText.setAlignment(QtCore.Qt.AlignJustify)
        self.descriptionText.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.initUI()

    def initUI(self):

        self.vl.addWidget(self.name)
        self.hlSup.addWidget(self.picture)

        self.vlSup.addWidget(self.characters1)
        self.vlSup.addWidget(self.descriptionText)
        self.vlSup.addWidget(self.characters2)
        self.hlSup.addLayout(self.vlSup)

        self.vl.addLayout(self.hlSup)
        user = Users.get_user_type()
        if user != UserTypes.GUEST:
            self.button = QtWidgets.QPushButton('Добавить на книжную полку')
            self.vl.addWidget(self.button)


        self.name.setStyleSheet("QLabel {background-color: yellow;}")
        self.name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    def initAddButtom(self, f):
        self.button.clicked.connect(f(self.book['slug']))