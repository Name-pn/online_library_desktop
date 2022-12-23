import PyQt5.QtWidgets
from componets import TopComponent
from componets.AuthorPrivatePage import AuthorPrivatePageComponent


class AuthorDetails(PyQt5.QtWidgets.QWidget):

    def __init__(self, topComponent: TopComponent, slug, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.vl = PyQt5.QtWidgets.QVBoxLayout(self)

        self.top = topComponent
        self.list = AuthorPrivatePageComponent(slug)

        self.initUI()

    def initUI(self):
        self.vl.addWidget(self.top)
        self.vl.addWidget(self.list)