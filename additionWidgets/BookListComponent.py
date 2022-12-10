import PyQt5.QtWidgets
import PyQt5.QtGui
import PyQt5.QtCore
from PyQt5 import Qt

import additionWidgets.VLine
import additionWidgets.Plug
from API.apps import Books
from  ListElements.BookElement import BookElement



class BookListComponent(PyQt5.QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.listBooks = [BookElement(book) for book in Books.get_all()]

        self.scrollArea = PyQt5.QtWidgets.QScrollArea()
        self.scrollArea.setParent(self)

        class testW(PyQt5.QtWidgets.QWidget):
            arr = self.listBooks

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.vl = PyQt5.QtWidgets.QVBoxLayout(self)

                for item in self.arr:
                    self.vl.addWidget(item)

        self.ex = testW()
        self.initUI()

    def paintEvent(self, a0: PyQt5.QtGui.QPaintEvent):
        self.scrollArea.setFixedSize(self.size())

    def initUI(self):

        self.scrollArea.setWidget(self.ex)
        self.setMinimumSize(self.scrollArea.size())


