import PyQt6
from PyQt6 import QtWidgets

from Components.PdfViewer import PdfViewerComponent
from Components.Top import TopComponent

class PdfViewer(PyQt6.QtWidgets.QWidget):

    def __init__(self, topComponent: TopComponent, url, parent=None):
        super().__init__(parent)
        self.vl = PyQt6.QtWidgets.QVBoxLayout(self)

        self.top = topComponent
        self.list = PdfViewerComponent(url)

        self.initUI()

    def initUI(self):

        self.vl.addWidget(self.top)
        self.vl.addWidget(self.list)
