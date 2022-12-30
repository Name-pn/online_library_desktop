from enum import Enum

from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtWidgets import QLayout, QSizePolicy, QVBoxLayout
import Program.Constrains
from API.apps import Books
from ListElements.BookElement import BookElement

class TypeUpdateListBook(Enum):
    GENRE = 0
    DATE = 1
    AUTHOR = 2
    ALL = 3

class BookListComponent(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.f = None
        self.mainVL = QVBoxLayout(self)
        self.scrollArea = QtWidgets.QScrollArea()
        self.mainVL.addWidget(self.scrollArea)
        self.scrollArea.setWidgetResizable(True)
        self.array = []
        self.mainLayout = self.initLayout()
        self.content = QtWidgets.QWidget()
        self.content.setLayout(self.mainLayout)
        self.initUI()

    def reinitList(self, mode, key = None):
        mode = TypeUpdateListBook(mode)
        for el in self.array:
            self.mainLayout.removeWidget(el)
            el.deleteLater()

        self.array = []
        if mode == TypeUpdateListBook.ALL:
            key = key.split('|')
            genres = key[0]
            time = key[1]
            name = key[2]
            name = Program.Constrains.DEFAULT_CONSTRAINS.table.table.get(name)
            if name is None:
                name = ''
            for book_properties in Books.get_filter(genres, name, time.split(' ')[1], time.split(' ')[4]):
                el = BookElement(book_properties)
                self.array.append(el)
                el.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
                self.mainLayout.addWidget(el)
            self.initButtons(self.f)
            return
        elif mode == TypeUpdateListBook.GENRE:
            for book_properties in Books.get_filter(key):
                el = BookElement(book_properties)
                self.array.append(el)
                el.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
                self.mainLayout.addWidget(el)
        elif mode == TypeUpdateListBook.AUTHOR:
            key = Program.Constrains.DEFAULT_CONSTRAINS.table.get(key)
            if key is not None:
                for book_properties in Books.get_filter(author=key):
                    el = BookElement(book_properties)
                    self.array.append(el)
                    el.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
                    self.mainLayout.addWidget(el)
        else:
            if mode == TypeUpdateListBook.DATE:
                for book_properties in Books.get_filter(year_of_writing_min=key.split(' ')[1], year_of_writing_max=key.split(' ')[4]):
                    el = BookElement(book_properties)
                    self.array.append(el)
                    el.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
                    self.mainLayout.addWidget(el)
        self.initButtons(self.f)



    def initLayout(self) -> QLayout:
        layout = QtWidgets.QVBoxLayout(self)

        for book_properties in Books.get_all():
            el = BookElement(book_properties)
            self.array.append(el)
            el.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            layout.addWidget(el)

        return layout

    def initUI(self):
        self.scrollArea.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.scrollArea.setWidget(self.content)

    def initButtons(self, f):
        if self.f == None:
            self.f = f
        for el in self.array:
            el.initButton(f)