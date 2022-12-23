import PyQt5
from PyQt5 import QtWidgets

from componets.BookshelfComponent import BookshelfComponent
from componets.TopComponent import TopComponent

class Bookshelf(PyQt5.QtWidgets.QWidget):

    def __init__(self, topComponent: TopComponent, parent=None):
        super().__init__(parent)
        self.vl = PyQt5.QtWidgets.QVBoxLayout(self)

        self.top = topComponent
        self.list = BookshelfComponent()

        self.initUI()

    def initUI(self):

        self.vl.addWidget(self.top)
        self.vl.addWidget(self.list)
