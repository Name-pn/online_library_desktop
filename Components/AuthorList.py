from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QLayout, QVBoxLayout, QSizePolicy

from API.apps import Authors
from ListElements.AuthorElement import AutherElement

class AuthorListComponent(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lv = QVBoxLayout(self)

        self.scrollArea = QtWidgets.QScrollArea()
        self.lv.addWidget(self.scrollArea)
        self.content = QtWidgets.QWidget()

        self.array = []
        self.mainLayout = self.initLayout()
        self.content.setLayout(self.mainLayout)

        self.initUI()

    def initLayout(self) -> QLayout:
        layout = QtWidgets.QVBoxLayout(self)

        for auther_properties in Authors.get_all():
            el = AutherElement(auther_properties)
            el.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            layout.addWidget(el)
            self.array.append(el)

        return layout

    def initButtons(self, f):
        for el in self.array:
            el.initButton(f)

    def initUI(self):
        self.scrollArea.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.scrollArea.setWidget(self.content)
