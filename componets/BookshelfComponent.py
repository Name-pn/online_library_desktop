from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QLayout

from API.apps import Books, Users
from ListElements.BookshelfElement import BookshelfElement

class BookshelfComponent(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setParent(self)
        self.array = []
        mainLayout = self.initLayout()


        self.content = QtWidgets.QWidget()
        self.content.setLayout(mainLayout)

        self.initUI()

    def initLayout(self) -> QLayout:
        layout = QtWidgets.QVBoxLayout(self)

        for book_properties in Users.get_my_books():
            property = Books.get_detail(book_properties['book'])
            el = BookshelfElement(property)
            self.array.append(el)
            layout.addWidget(el)

        return layout

    def paintEvent(self, a0: QtGui.QPaintEvent):
        self.scrollArea.setFixedSize(self.size())

    def initUI(self):
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setWidget(self.content)
        self.setMinimumSize(self.scrollArea.size())

    def initButtonsToPdf(self, f):
        for el in self.array:
            el.initButtonToPdf(f)

    def initButtonsToDetails(self, f):
        for el in self.array:
            el.initButtonToDetails(f)