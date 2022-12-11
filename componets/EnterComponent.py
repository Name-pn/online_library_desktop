import PyQt5.QtWidgets
import PyQt5.QtGui
import PyQt5.QtCore
import componets.VLine

class EnterComponent(PyQt5.QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hl = PyQt5.QtWidgets.QHBoxLayout(self)

        self.buttonUser = PyQt5.QtWidgets.QPushButton("Войти")
        self.buttonExit = PyQt5.QtWidgets.QPushButton("Зарегистрироваться")
        self.vline = componets.VLine.VLine(10, 50)

        self.initUI()

    def initUI(self):

        self.vline.setHeight(20)
        self.hl.addWidget(self.buttonUser)
        self.hl.addWidget(self.vline)
        self.hl.addWidget(self.buttonExit)
        self.hl.setAlignment(PyQt5.QtCore.Qt.AlignLeft)
