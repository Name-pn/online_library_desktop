import PyQt5.QtWidgets
import additionWidgets.TopComponent
import additionWidgets.EnterComponent
import additionWidgets.AccessComponent

class EntryForm(PyQt5.QtWidgets.QWidget):

    def __init__(self, topComponent: additionWidgets.TopComponent, parent = None):
        super().__init__(parent)
        self.vl = PyQt5.QtWidgets.QVBoxLayout(self)

        self.comp = topComponent
        self.enter = additionWidgets.AccessComponent.AccessComponent()

        self.initUI()

    def initUI(self):
        self.vl.addWidget(self.comp)
        self.vl.addWidget(self.enter)




