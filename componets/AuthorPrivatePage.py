from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QLayout

from API.apps import Authors
from ListElements.AuthorElement import AutherElement
from Program.Networking import NETWORK_MANAGER
from componets.ScaledPicture import ScaledPicture


class AuthorListComponent(QtWidgets.QWidget):

    def __init__(self, slug: str, *args, **kwargs):
        super().__init__(*args, **kwargs)


        author = Authors.get_detail(slug)
        name = author.get('name') + ' ' + author.get('surname')
        imageUrl = author.get('image')

        self.vl = QtWidgets.QVBoxLayout(self)

        self.name = name
        if imageUrl is None:
            self.picture = ScaledPicture('./images/undefined.png')
        else:
            image = NETWORK_MANAGER.httpGetImage(imageUrl)
            self.picture = ScaledPicture()


    def initLayout(self) -> QLayout:
        layout = QtWidgets.QVBoxLayout(self)

        for auther_properties in Authors.get_all():
            layout.addWidget(AutherElement(auther_properties))

        return layout

    def paintEvent(self, a0: QtGui.QPaintEvent):
        self.scrollArea.setFixedSize(self.size())

    def initUI(self):
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setWidget(self.content)
        self.setMinimumSize(self.scrollArea.size())
