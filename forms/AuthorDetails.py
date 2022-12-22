import PyQt5.QtWidgets
from componets import TopComponent


class AuthorDetails(PyQt5.QtWidgets.QWidget):

    def __init__(self, topComponent: TopComponent, parent=None):
        super().__init__(parent)
        self.vl = PyQt5.QtWidgets.QVBoxLayout(self)

        self.comp = topComponent
        self.list = AuthorPrivatePage()

        self.initUI()

    def initUI(self):
        self.vl.addWidget(self.comp)
        self.vl.addWidget(self.list)