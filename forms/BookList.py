import PyQt5
from PyQt5 import QtWidgets

from componets.BookListComponent import BookListComponent
from componets.TopComponent import TopComponent


class BookList(PyQt5.QtWidgets.QWidget):

    def __init__(self, topComponent: TopComponent, parent=None):
        super().__init__(parent)
        self.vl = PyQt5.QtWidgets.QVBoxLayout(self)

        self.comp = topComponent
        self.list = BookListComponent()

        self.initUI()

    # def paintEvent(self, a0: PyQt5.QtGui.QPaintEvent):
    #    painter = PyQt5.QtGui.QPainter(self)
    #    brush = PyQt5.QtGui.QBrush(PyQt5.QtCore.Qt.green)
    #    painter.setBrush(brush)
    #    painter.drawRect(0, 0, self.width(), self.height())

    def initUI(self):
        # self.vl.setAlignment(PyQt5.QtCore.Qt.AlignCenter)

        self.vl.addWidget(self.comp)
        self.vl.addWidget(self.list)
