from PyQt6.QtWidgets import QWidget, QHBoxLayout, QSizePolicy

from Components.BookSorter import BookSorter
from Components.BookList import BookListComponent


class BookWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.hl = QHBoxLayout(self)
        self.list = BookListComponent()
        self.sorter = BookSorter()
        self.sorter.sig.upsig.connect(lambda a, b: self.list.reinitList(a, b))
        self.sorter.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        self.initGI()

    def initGI(self):
        self.hl.addWidget(self.sorter)
        self.hl.addWidget(self.list)

    def initButtons(self, f):
        self.list.initButtons(f)