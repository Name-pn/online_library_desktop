import PyQt6
from PyQt6 import QtWidgets

from Components.BookList import BookListComponent
from Components.AuthorList import AuthorListComponent
from Components.Top import TopComponent


class AuthorList(PyQt6.QtWidgets.QWidget):

    def __init__(self, topComponent: TopComponent, parent=None):
        super().__init__(parent)
        self.vl = PyQt6.QtWidgets.QVBoxLayout(self)
        self.comp = topComponent
        self.list = AuthorListComponent()
        self.initUI()
        self.array = self.list.array

    def initUI(self):
        self.vl.addWidget(self.comp)
        self.vl.addWidget(self.list)

    def initButtons(self, f):
        self.list.initButtons(f)

    def resetTop(self, component):
        self.vl.removeWidget(self.comp)
        self.comp.deleteLater()
        self.vl.insertWidget(0, component)
        self.comp = component