import PyQt5.QtWidgets
from componets import TopComponent, BookDetailsComponent


class BookDetails(PyQt5.QtWidgets.QWidget):

    def __init__(self, topComponent: TopComponent, slug, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.vl = PyQt5.QtWidgets.QVBoxLayout(self)

        self.top = topComponent
        self.list = BookDetailsComponent.BookDetailComponent(slug)

        self.initUI()

    def initUI(self):
        self.vl.addWidget(self.top)
        self.vl.addWidget(self.list)

    def initAddButtom(self, f):
        self.list.initAddButtom(f)