import PyQt5.QtWidgets

class Plug(PyQt5.QtWidgets.QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setMinimumSize(100, 100)
