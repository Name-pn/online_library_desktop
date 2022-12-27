import PyQt6
from PyQt6 import QtWidgets

from Components.PrivatePage import PrivatePageComponent
from Components.Top import TopComponent


class PrivatePage(PyQt6.QtWidgets.QWidget):

    def __init__(self, topComponent: TopComponent, parent=None):
        super().__init__(parent)
        self.vl = PyQt6.QtWidgets.QVBoxLayout(self)

        self.top = topComponent
        self.list = PrivatePageComponent()

        self.initUI()

    def initUI(self):

        self.vl.addWidget(self.top)
        self.vl.addWidget(self.list)
