import PyQt6.QtWidgets
import PyQt6.QtGui
import PyQt6.QtCore
import Components.Top
import Components.Enter
import Components.Access

class EntryForm(PyQt6.QtWidgets.QWidget):

    def __init__(self, f, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.f = f
        self.vl = PyQt6.QtWidgets.QVBoxLayout(self)
        self.enter = Components.Access.AccessComponent(lambda: self.close())
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Форма входа')
        icon = PyQt6.QtGui.QIcon('./Images/lib.png')
        self.setWindowIcon(icon)

        self.setFixedWidth(400)
        self.setFixedHeight(300)
        self.vl.addWidget(self.enter)

    def closeEvent(self, a0: PyQt6.QtGui.QCloseEvent) -> None:
        self.enter.reinit()
        self.f()