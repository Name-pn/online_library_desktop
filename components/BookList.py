from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QLayout, QSizePolicy

from API.apps import Books
from ListElements.BookElement import BookElement

class BookListComponent(QtWidgets.QWidget):

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

        for book_properties in Books.get_all():
            el = BookElement(book_properties)
            self.array.append(el)
            el.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            layout.addWidget(el)

        return layout

    def paintEvent(self, a0: QtGui.QPaintEvent):
        self.scrollArea.setFixedSize(self.size())

    def initUI(self):
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setWidget(self.content)
        self.setMinimumSize(self.scrollArea.size())

    def initButtons(self, f):
        for el in self.array:
            el.initButton(f)