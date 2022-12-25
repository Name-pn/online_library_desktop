import PyQt5.QtWidgets
import PyQt5.QtGui
import PyQt5.QtCore
import components.Top
import components.Enter
import components.Access

class EntryForm(PyQt5.QtWidgets.QWidget):

    def __init__(self, f, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.f = f
        self.vl = PyQt5.QtWidgets.QVBoxLayout(self)
        self.enter = components.Access.AccessComponent(lambda: self.close())
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Форма входа')
        icon = PyQt5.QtGui.QIcon('./images/lib.png')
        self.setWindowIcon(icon)

        self.setFixedWidth(400)
        self.setFixedHeight(300)
        self.vl.addWidget(self.enter)

    def closeEvent(self, a0: PyQt5.QtGui.QCloseEvent) -> None:
        self.enter.reinit()
        self.f()