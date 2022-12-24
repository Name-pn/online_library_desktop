import PyQt5.QtWidgets
import PyQt5.QtGui
import PyQt5.QtCore
from PyQt5.QtWebEngineCore import QWebEngineHttpRequest
from PyQt5.QtWebEngineWidgets import QWebEngineView

class PdfViewerComponent(PyQt5.QtWidgets.QWidget):

    def __init__(self, url, parent=None):
        super().__init__(parent)
        self.vl = PyQt5.QtWidgets.QVBoxLayout(self)
        self.viewer = QWebEngineView()
        self.initUI(url)

    def initUI(self, url):
        req = QWebEngineHttpRequest(PyQt5.QtCore.QUrl(url))

        self.settings = self.viewer.settings()
        self.settings.setAttribute(PyQt5.QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        self.viewer.load(req)
        self.viewer.loadFinished.connect(self.addPdf)

    def addPdf(self):
        self.vl.addWidget(self.viewer)