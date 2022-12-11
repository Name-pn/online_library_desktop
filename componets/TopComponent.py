from PyQt5 import QtGui, QtCore, QtWidgets

from componets.UserComponent import UserComponent
from componets.RefComponent import RefComponent


class TopComponent(QtWidgets.QWidget):
    def __init__(self, userComponent: UserComponent, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.comp = userComponent
        self.hl = QtWidgets.QHBoxLayout(self)
        self.spacer = QtWidgets.QSpacerItem(0, 0)
        self.spacer2 = QtWidgets.QSpacerItem(0, 0)
        self.refC = RefComponent()

        self.initUI()

    def paintEvent(self, a0: QtGui.QPaintEvent):
        painter = QtGui.QPainter(self)
        brush = QtGui.QBrush(QtCore.Qt.gray)
        painter.setBrush(brush)
        painter.drawRect(0, 0, self.width(), self.height())

    def initUI(self):
        self.setMaximumHeight(75)
        self.hl.setAlignment(QtCore.Qt.AlignLeft)
        self.hl.addWidget(self.comp)
        self.hl.addSpacerItem(self.spacer)
        self.hl.addWidget(self.refC)
        self.hl.addSpacerItem(self.spacer2)
