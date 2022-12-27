from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QLayout, QLabel

from API.apps import Authors
from Program.Networking import NETWORK_MANAGER
from Components.AuthorBookList import AuthorBookList
from Components.ScaledPicture import ScaledPicture

class AuthorPrivatePageComponent(QtWidgets.QWidget):

    def __init__(self, slug: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        author = Authors.get_detail(slug)
        name = author.get('name') + ' ' + author.get('surname')
        imageUrl = author.get('image')

        self.vl = QtWidgets.QVBoxLayout(self)
        self.hlSup = QtWidgets.QHBoxLayout()
        self.vlSup = QtWidgets.QVBoxLayout()
        self.name = QLabel()
        self.name.setText(name)

        self.name.setFont(QtGui.QFont("Times new roman", 20))
        self.name.setSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        if imageUrl is None:
            self.picture = ScaledPicture('./Images/undefined.png')
        else:
            image = NETWORK_MANAGER.httpGetImage(QUrl(imageUrl))
            self.picture = ScaledPicture('', image)
        self.descriptionText = QtWidgets.QTextEdit(author.get('description'))
        self.descriptionText.setAlignment(QtCore.Qt.AlignmentFlag.AlignJustify)
        self.descriptionText.setSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        self.descriptionText.setFont(QtGui.QFont("Times new roman", 16))
        self.list = AuthorBookList(author['slug'])
        self.initUI()

    def initUI(self):
        self.vl.addWidget(self.name)
        self.hlSup.addWidget(self.picture)

        self.vlSup.addWidget(self.descriptionText)
        self.vlSup.addWidget(self.list)
        self.hlSup.addLayout(self.vlSup)

        self.vl.addLayout(self.hlSup)
        self.name.setStyleSheet("QLabel {background-color: yellow;}")
        self.name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)