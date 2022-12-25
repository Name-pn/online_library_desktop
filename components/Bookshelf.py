import PyQt5
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLayout, QWidget, QAbstractScrollArea

from API.apps import Books, Users
from ListElements.BookshelfElement import BookshelfElement

class BookshelfComponent(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setSizePolicy(PyQt5.QtWidgets.QSizePolicy.Minimum, PyQt5.QtWidgets.QSizePolicy.Maximum)
        self.scrollArea.setWidgetResizable(True)
        self.setSizePolicy(PyQt5.QtWidgets.QSizePolicy.Minimum, PyQt5.QtWidgets.QSizePolicy.Minimum)

        self.scrollArea.setParent(self)
        self.array = []
        self.mainLayout = self.initLayout()

        self.content = QtWidgets.QWidget()
        self.content.setSizePolicy(PyQt5.QtWidgets.QSizePolicy.Maximum, PyQt5.QtWidgets.QSizePolicy.Maximum)

        self.content.setLayout(self.mainLayout)

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

    def removeW(self, el):
        el.deleteLater()
        self.mainLayout.removeWidget(el)
        self.mainLayout.update()
        self.content.update()
        self.scrollArea.update()
        self.update()

    def initButtonsToRemove(self, f):
        for el in self.array:
            el.initButtonToRemove(f, lambda elArg: self.removeW(elArg))


    def initButtonsToDetails(self, f):
        for el in self.array:
            el.initButtonToDetails(f)
