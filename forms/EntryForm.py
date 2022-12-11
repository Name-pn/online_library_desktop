import PyQt5.QtWidgets
import PyQt5.QtGui
import PyQt5.QtCore
import componets.TopComponent
import componets.EnterComponent
import componets.AccessComponent

class EntryForm(PyQt5.QtWidgets.QWidget):

    def __init__(self, f, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.f = f
        self.vl = PyQt5.QtWidgets.QVBoxLayout(self)
        self.enter = componets.AccessComponent.AccessComponent()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Форма входа')
        icon = PyQt5.QtGui.QIcon('./images/lib.png')
        self.setWindowIcon(icon)

        self.setGeometry(0, 0, 100, 150)
        #self.setSizePolicy(PyQt5.QtWidgets.QSizePolicy.Maximum, PyQt5.QtWidgets.QSizePolicy.Maximum)
        #self.setMinimumSize(240, 200)
        #self.setSizePolicy()
        #self.vl.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        self.vl.addWidget(self.enter)

    def closeEvent(self, a0: PyQt5.QtGui.QCloseEvent) -> None:
        self.f()


