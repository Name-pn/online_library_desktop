import PyQt5.QtWidgets
from componets import TopComponent


class BookDetails(PyQt5.QtWidgets.QWidget):

    def __init__(self, topComponent: TopComponent, slug, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.vl = PyQt5.QtWidgets.QVBoxLayout(self)

        self.top = topComponent
        self.list = BookDetailsComponent(slug)

        self.initUI()

    def initUI(self):
        self.vl.addWidget(self.top)
        self.vl.addWidget(self.list)