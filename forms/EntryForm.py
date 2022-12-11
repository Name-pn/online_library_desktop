import PyQt5.QtWidgets
import componets.TopComponent
import componets.EnterComponent
import componets.AccessComponent

class EntryForm(PyQt5.QtWidgets.QWidget):

    def __init__(self, topComponent: componets.TopComponent, parent = None):
        super().__init__(parent)
        self.vl = PyQt5.QtWidgets.QVBoxLayout(self)

        self.comp = topComponent
        self.enter = componets.AccessComponent.AccessComponent()

        self.initUI()

    def initUI(self):
        self.vl.addWidget(self.comp)
        self.vl.addWidget(self.enter)




