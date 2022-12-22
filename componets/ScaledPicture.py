from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QImage


class ScaledPicture(QtWidgets.QWidget):

    def __init__(self, fileName: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMinimumSize(100, 100)
        self.pix = QtGui.QPixmap(".\images\imageLib.png")
        self.pix = self.pix.scaled(self.size())
        self.label = QtWidgets.QLabel()
        self.label.setParent(self)
        self.initGI()

    def paintEvent(self, a0: QtGui.QPaintEvent):
        self.pix = QtGui.QPixmap(".\images\imageLib.png")
        self.pix = self.pix.scaled(self.size())
        self.label.setPixmap(self.pix)
        self.label.setFixedSize(self.size())

    def initGI(self):
        self.label.setPixmap(self.pix)
