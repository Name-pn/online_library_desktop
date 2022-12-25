from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QSizePolicy

from components.User import UserComponent
from components.Ref import RefComponent
from enum import Enum


class TopDetail(Enum):
    USER = 0
    GUEST = 1

class TopComponent(QtWidgets.QWidget):
    def __init__(self, userComponent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if (isinstance(self, UserComponent)):
            self.type = TopDetail.USER
        else:
            self.type = TopDetail.GUEST
        self.left = userComponent
        self.hl = QtWidgets.QHBoxLayout(self)
        self.refC = RefComponent()

        self.initUI()

    def paintEvent(self, a0: QtGui.QPaintEvent):
        painter = QtGui.QPainter(self)
        brush = QtGui.QBrush(QtCore.Qt.gray)
        painter.setBrush(brush)
        painter.drawRect(0, 0, self.width(), self.height())

    def initUI(self):
        #self.setFixedHeight(75)
        self.hl.addWidget(self.left)
        self.hl.addWidget(self.refC)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)

