import PyQt6.QtWidgets

from Components import BookDetail, Top


class BookDetails(PyQt6.QtWidgets.QWidget):
    def __init__(self, topComponent: Top, slug, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.vl = PyQt6.QtWidgets.QVBoxLayout(self)

        self.top = topComponent
        self.list = BookDetail.BookDetailComponent(slug)

        self.initUI()

    def initUI(self):
        self.vl.addWidget(self.top)
        self.vl.addWidget(self.list)

    def initAddButtom(self, f):
        self.list.initAddButtom(f)