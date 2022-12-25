import PyQt5
from PyQt5 import QtWidgets

from components.BookList import BookListComponent
from components.Top import TopComponent


class BookList(PyQt5.QtWidgets.QWidget):

    def __init__(self, topComponent: TopComponent, parent=None):
        super().__init__(parent)
        self.vl = PyQt5.QtWidgets.QVBoxLayout(self)

        self.comp = topComponent
        self.list = BookListComponent()

        self.initUI()

    def initUI(self):

        self.vl.addWidget(self.comp)
        self.vl.addWidget(self.list)

    def initButtons(self, f):
        self.list.initButtons(f)