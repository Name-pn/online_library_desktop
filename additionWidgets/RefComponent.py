import PyQt5.QtWidgets
import PyQt5.QtGui
import PyQt5.QtCore
import additionWidgets.VLine
import additionWidgets.Plug

class RefComponent(PyQt5.QtWidgets.QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.hl = PyQt5.QtWidgets.QHBoxLayout(self)

        self.main = PyQt5.QtWidgets.QPushButton("Главная")
        self.vline1 = additionWidgets.VLine.VLine(10, 20)
        self.books = PyQt5.QtWidgets.QPushButton("Книги")
        self.vline2 = additionWidgets.VLine.VLine(10, 20)
        self.authers = PyQt5.QtWidgets.QPushButton("Авторы")

        self.initUI()

    def initUI(self):
        self.hl.setAlignment(PyQt5.QtCore.Qt.AlignLeft)
        self.hl.addWidget(self.main)
        self.hl.addWidget(self.vline1)
        self.hl.addWidget(self.books)
        self.hl.addWidget(self.vline2)
        self.hl.addWidget(self.authers)
