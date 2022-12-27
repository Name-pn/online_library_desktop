import PyQt6
from PyQt6 import QtWidgets

from components.MainPage import MainPageComponent
from components.Top import TopComponent

class MainPage(PyQt6.QtWidgets.QWidget):

    def __init__(self, topComponent: TopComponent, parent=None):
        super().__init__(parent)
        self.vl = PyQt6.QtWidgets.QVBoxLayout(self)

        self.comp = topComponent
        self.list = MainPageComponent()
        self.initUI()

    def initUI(self):

        self.vl.addWidget(self.comp)
        self.vl.addWidget(self.list)

    def resetTop(self, component):
        self.vl.removeWidget(self.comp)
        self.comp.deleteLater()
        self.vl.insertWidget(0, component)
        self.comp = component