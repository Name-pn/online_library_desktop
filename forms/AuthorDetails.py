import PyQt5.QtWidgets
from components import Top
from components.AuthorPrivatePage import AuthorPrivatePageComponent


class AuthorDetails(PyQt5.QtWidgets.QWidget):

    def __init__(self, topComponent: Top, slug, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.vl = PyQt5.QtWidgets.QVBoxLayout(self)

        self.top = topComponent
        self.list = AuthorPrivatePageComponent(slug)

        self.initUI()

    def initUI(self):
        self.vl.addWidget(self.top)
        self.vl.addWidget(self.list)