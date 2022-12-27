import PyQt6.QtWidgets
import PyQt6.QtGui
import PyQt6.QtCore
from PyQt6 import QtCore, QtWidgets, QtPdfWidgets
from PyQt6.QtPdfWidgets import QPdfView
import Program

class PdfViewerComponent(PyQt6.QtWidgets.QWidget):

    def __init__(self, url, parent=None):
        super().__init__(parent)
        self.vl = PyQt6.QtWidgets.QVBoxLayout(self)
        self.viewer = QtPdfWidgets.QPdfView(self)
        self.downloader = Program.Networking.Networking()
        a = self.downloader.httpGetPdf(QtCore.QUrl(url), self)
        self.viewer.setDocument(a)
        self.viewer.setPageMode(QPdfView.PageMode.MultiPage)
        self.initUI(url)

    def initUI(self, url):
        self.addPdf()

    def addPdf(self):
        self.vl.addWidget(self.viewer)