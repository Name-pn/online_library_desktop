import PyQt5
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QCursor

from components.VLine import VLine


class RefComponent(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.hl = QtWidgets.QHBoxLayout(self)

        curs = QCursor()
        curs.setShape(PyQt5.QtCore.Qt.CursorShape.PointingHandCursor)

        self.main = QtWidgets.QPushButton("Главная")
        self.main.setFont(QFont('Times new roman', 12))
        self.main.setCursor(curs)

        self.vline1 = VLine(10, 20)

        self.books = QtWidgets.QPushButton("Книги")
        self.books.setFont(QFont('Times new roman', 12))
        self.books.setCursor(curs)

        self.vline2 = VLine(10, 20)

        self.authers = QtWidgets.QPushButton("Авторы")
        self.authers.setFont(QFont('Times new roman', 12))
        self.authers.setCursor(curs)

        self.initUI()

    def initUI(self):
        self.hl.setAlignment(QtCore.Qt.AlignLeft)
        self.hl.addWidget(self.main)
        self.hl.addWidget(self.vline1)
        self.hl.addWidget(self.books)
        self.hl.addWidget(self.vline2)
        self.hl.addWidget(self.authers)
