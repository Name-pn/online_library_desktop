from PyQt6 import QtGui
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QListWidget, QVBoxLayout, QTextBrowser, QAbstractItemView, QSizePolicy, QStyle
import Program.Constrains

class AuthorBookList(QListWidget):
    def __init__(self, slug, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.vl = QVBoxLayout(self)
        self.list = QListWidget()
        self.list.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.list.setFont(Program.Constrains.DEFAULT_CONSTRAINS.mainFont)
        self.vl.addWidget(self.list)
        self.books = []
        integer = 1
        for el in Program.Constrains.DEFAULT_CONSTRAINS.books:
            if el['author'] == slug:
                self.books.append(el)
                self.list.addItem(str(integer) + ': "' + el['title'] + '" изданная в ' + str(el['year_of_writing']))
                integer = integer + 1

        self.text = QTextBrowser()
        self.text.setText('Книги автора доступные в библиотеке:')
        self.text.setStyleSheet("background-color: rgba(200, 250, 255, .5);")
        self.text.setMaximumHeight(50)
        self.text.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        self.text.setFont(Program.Constrains.DEFAULT_CONSTRAINS.mainFont)
        self.initGI()

    def initGI(self):
        self.vl.addWidget(self.text)
        self.vl.addWidget(self.list)


