from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QLayout, QLabel

from API.apps import Books
from Program.Networking import NETWORK_MANAGER
from componets.ScaledPicture import ScaledPicture

class BookDetailComponent(QtWidgets.QWidget):

    def __init__(self, slug: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        book = Books.get_detail(slug)
        name = book.get('title')
        imageUrl = book.get('cover')
        if imageUrl is None:
            self.picture = ScaledPicture('./images/undefined.png')
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
        if imageUrl is None:
            self.picture = ScaledPicture('./images/undefined.png')
        else:
            image = NETWORK_MANAGER.httpGetImage(QUrl(imageUrl))
            self.picture = ScaledPicture('', image)
        self.descriptionText = QtWidgets.QTextEdit(book.get('description'))
        self.descriptionText.setAlignment(QtCore.Qt.AlignJustify)
        self.descriptionText.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.initUI()

    def initUI(self):
        self.vl.addWidget(self.name)
        self.hlSup.addWidget(self.picture)

        self.vlSup.addWidget(self.descriptionText)
        self.hlSup.addLayout(self.vlSup)

        self.vl.addLayout(self.hlSup)
        self.name.setStyleSheet("QLabel {background-color: yellow;}")
        self.name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)