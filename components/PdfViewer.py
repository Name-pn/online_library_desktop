import PyQt5.QtWidgets
import PyQt5.QtGui
import PyQt5.QtCore
from PyQt5 import QtCore, QtWebEngineWidgets, QtWidgets
from PyQt5.QtWebEngineCore import QWebEngineHttpRequest
from PyQt5.QtWebEngineWidgets import QWebEngineView

class PdfViewerComponent(PyQt5.QtWidgets.QWidget):

    def __init__(self, url, parent=None):
        super().__init__(parent)

        self.vl = PyQt5.QtWidgets.QVBoxLayout(self)
        self.viewer = QWebEngineView()
        QtWebEngineWidgets.QWebEngineProfile.defaultProfile().downloadRequested.connect(self.on_downloadRequested)

        #QtWebEngineWidgets.QWebEngineProfile.defaultProfile().setDownloadPath('.')
        #QtWebEngineWidgets.QWebEngineProfile.defaultProfile().setCachePath('.')
        #QtWebEngineWidgets.QWebEngineProfile.defaultProfile().setPersistentStoragePath('.')
        #a = QtWebEngineWidgets.QWebEngineProfile.defaultProfile().downloadPath()
        #b = QtWebEngineWidgets.QWebEngineProfile.defaultProfile().cachePath()

        self.initUI(url)

    def initUI(self, url):
        req = QWebEngineHttpRequest(PyQt5.QtCore.QUrl(url))
        self.settings = self.viewer.settings()
        self.settings.setAttribute(PyQt5.QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        #self.settings.setAttribute(PyQt5.QtWebEngineWidgets.QWebEngineSettings.PdfViewerEnabled, True)
        self.viewer.loadFinished.connect(self.addPdf)
        self.viewer.load(req)

    @QtCore.pyqtSlot(QtWebEngineWidgets.QWebEngineDownloadItem)
    def on_downloadRequested(self, download):
        path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save File", "sample.pdf", "*.pdf"
        )
        if path:
            download.setPath(path)
            download.accept()

    def addPdf(self):
        self.vl.addWidget(self.viewer)