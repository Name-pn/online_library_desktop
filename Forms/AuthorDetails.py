import PyQt6.QtWidgets
from Components import Top
from Components.AuthorPrivatePage import AuthorPrivatePageComponent


class AuthorDetails(PyQt6.QtWidgets.QWidget):

    def __init__(self, topComponent: Top, slug, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.vl = PyQt6.QtWidgets.QVBoxLayout(self)

        self.top = topComponent
        self.list = AuthorPrivatePageComponent(slug)

        self.initUI()

    def initUI(self):
        self.vl.addWidget(self.top)
        self.vl.addWidget(self.list)