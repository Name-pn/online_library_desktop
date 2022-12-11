from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QLayout

from API.apps import Books
from ListElements.BookElement import BookElement


class BookListComponent(QtWidgets.QWidget):

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

        for book_properties in Books.get_all():
            layout.addWidget(BookElement(book_properties))

        return layout

    def paintEvent(self, a0: QtGui.QPaintEvent):
        self.scrollArea.setFixedSize(self.size())

    def initUI(self):
        self.scrollArea.setWidget(self.content)
        self.setMinimumSize(self.scrollArea.size())
