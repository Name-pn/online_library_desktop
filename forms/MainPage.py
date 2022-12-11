import PyQt5
from PyQt5 import QtWidgets

from componets.MainPageComponent import MainPageComponent
from componets.TopComponent import TopComponent


class MainPage(PyQt5.QtWidgets.QWidget):

    def __init__(self, topComponent: TopComponent, parent=None):
        super().__init__(parent)
        self.vl = PyQt5.QtWidgets.QVBoxLayout(self)

        self.comp = topComponent
        self.list = MainPageComponent()

        self.initUI()

    def initUI(self):

        self.vl.addWidget(self.comp)
        self.vl.addWidget(self.list)
