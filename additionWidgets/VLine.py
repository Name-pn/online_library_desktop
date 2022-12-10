import PyQt5.QtWidgets
import PyQt5.QtGui
import PyQt5.QtCore

class VLine(PyQt5.QtWidgets.QWidget):

    def __init__(self, width, height, parent = None):
        super().__init__(parent)
        self.width = width
        self.center = width / 2
        self.height = height
        self.setGeometry(0, 0, 3, height)
        self.setMinimumSize(5, int(height/2))

    def paintEvent(self, a0: PyQt5.QtGui.QPaintEvent):
        painter = PyQt5.QtGui.QPainter(self)
        pen = PyQt5.QtGui.QPen(PyQt5.QtCore.Qt.black, 3)
        painter.setPen(pen)
        painter.drawLine(int(self.center), 0, int(self.center), self.height)

    def setHeight(self, height):
        self.height = height
        self.setGeometry(0, 0, 3, height)
        self.setMinimumSize(5, height)