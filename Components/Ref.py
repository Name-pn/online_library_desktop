import PyQt6
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QFont
from PyQt6.QtGui import QCursor

import Program.Constrains
from Components.VLine import VLine


class RefComponent(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.hl = QtWidgets.QHBoxLayout(self)

        curs = QCursor()
        curs.setShape(PyQt6.QtCore.Qt.CursorShape.PointingHandCursor)

        self.main = QtWidgets.QPushButton("Главная")
        self.main.setFont(Program.Constrains.DEFAULT_CONSTRAINS.buttonsFont)
        self.main.setCursor(curs)

        self.vline1 = VLine(10, 20)

        self.books = QtWidgets.QPushButton("Книги")
        self.books.setFont(Program.Constrains.DEFAULT_CONSTRAINS.buttonsFont)
        self.books.setCursor(curs)

        self.vline2 = VLine(10, 20)

        self.authers = QtWidgets.QPushButton("Авторы")
        self.authers.setFont(Program.Constrains.DEFAULT_CONSTRAINS.buttonsFont)

        #QFont('Times new roman', 20)
        #Program.Constrains.DEFAULT_CONSTRAINS.mainFont
        self.authers.setCursor(curs)

        self.initUI()

    def initUI(self):
        self.hl.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.hl.addWidget(self.main)
        self.hl.addWidget(self.vline1)
        self.hl.addWidget(self.books)
        self.hl.addWidget(self.vline2)
        self.hl.addWidget(self.authers)
