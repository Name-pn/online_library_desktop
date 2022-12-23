from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QImage


class ScaledPicture(QtWidgets.QWidget):

    def __init__(self, fileName: str, image: QImage = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMinimumSize(100, 100)
        if image is None:
            self.pix = QtGui.QPixmap(fileName)
        else:
            self.pix = QtGui.QPixmap.fromImage(image)

        self.pixReal = self.pix.scaled(self.size())
        self.label = QtWidgets.QLabel()
        self.label.setParent(self)
        self.initGI()

    def paintEvent(self, a0: QtGui.QPaintEvent):
        #self.pix = QtGui.QPixmap(".\images\imageLib.png")
        self.pixReal = self.pix.scaled(self.size())
        self.label.setPixmap(self.pixReal)
        self.label.setFixedSize(self.size())

    def initGI(self):
        self.label.setPixmap(self.pixReal)
