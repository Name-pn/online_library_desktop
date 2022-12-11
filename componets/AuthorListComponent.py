from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QLayout

from API.apps import Authors
from ListElements.AuthorElement import AutherElement

class AuthorListComponent(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setParent(self)

        mainLayout = self.initLayout()

        self.content = QtWidgets.QWidget()
        self.content.setLayout(mainLayout)

        self.initUI()

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
