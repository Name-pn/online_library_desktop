from PyQt5 import QtCore, QtWidgets

from componets.VLine import VLine


class RefComponent(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.hl = QtWidgets.QHBoxLayout(self)

        self.main = QtWidgets.QPushButton("Главная")
        self.vline1 = VLine(10, 20)
        self.books = QtWidgets.QPushButton("Книги")
        self.vline2 = VLine(10, 20)
        self.authers = QtWidgets.QPushButton("Авторы")

        self.initUI()

    def initUI(self):
        self.hl.setAlignment(QtCore.Qt.AlignLeft)
        self.hl.addWidget(self.main)
        self.hl.addWidget(self.vline1)
        self.hl.addWidget(self.books)
        self.hl.addWidget(self.vline2)
        self.hl.addWidget(self.authers)
