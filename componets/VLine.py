from PyQt5 import QtWidgets, QtGui, QtCore


class VLine(QtWidgets.QWidget):

    def __init__(self, width, height, parent=None):
        super().__init__(parent)
        self.width = width
        self.center = width / 2
        self.height = height
        self.setGeometry(0, 0, 3, height)
        self.setMinimumSize(5, int(height / 2))

    def paintEvent(self, a0: QtGui.QPaintEvent):
        painter = QtGui.QPainter(self)
        pen = QtGui.QPen(QtCore.Qt.black, 3)
        painter.setPen(pen)
        painter.drawLine(int(self.center), 0, int(self.center), self.height)

    def setHeight(self, height):
        self.height = height
        self.setGeometry(0, 0, 3, height)
        self.setMinimumSize(5, height)
