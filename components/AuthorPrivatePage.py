from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QLayout, QLabel

from API.apps import Authors
from ListElements.AuthorElement import AutherElement
from Program.Networking import NETWORK_MANAGER
from components.ScaledPicture import ScaledPicture

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
        self.name.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        if imageUrl is None:
            self.picture = ScaledPicture('./images/undefined.png')
        else:
            image = NETWORK_MANAGER.httpGetImage(QUrl(imageUrl))
            self.picture = ScaledPicture('', image)
        self.descriptionText = QtWidgets.QTextEdit(author.get('description'))
        self.descriptionText.setAlignment(QtCore.Qt.AlignJustify)
        self.descriptionText.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.descriptionText.setFont(QtGui.QFont("Times new roman", 16))
        self.initUI()

    def initUI(self):
        self.vl.addWidget(self.name)
        self.hlSup.addWidget(self.picture)

        self.vlSup.addWidget(self.descriptionText)
        self.hlSup.addLayout(self.vlSup)

        self.vl.addLayout(self.hlSup)
        self.name.setStyleSheet("QLabel {background-color: yellow;}")
        self.name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)