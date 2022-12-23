import PyQt5
from PyQt5 import QtWidgets

from componets.BookListComponent import BookListComponent
from componets.AuthorListComponent import AuthorListComponent
from componets.TopComponent import TopComponent


class AuthorList(PyQt5.QtWidgets.QWidget):

    def __init__(self, topComponent: TopComponent, parent=None):
        super().__init__(parent)
        self.vl = PyQt5.QtWidgets.QVBoxLayout(self)
        self.comp = topComponent
        self.list = AuthorListComponent()
        self.initUI()
        self.array = self.list.array

    def initUI(self):
        self.vl.addWidget(self.comp)
        self.vl.addWidget(self.list)

    def initButtons(self, f):
        self.list.initButtons(f)