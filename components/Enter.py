import PyQt5.QtWidgets
import PyQt5.QtGui
import PyQt5.QtCore
import components.VLine

class EnterComponent(PyQt5.QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hl = PyQt5.QtWidgets.QHBoxLayout(self)

        curs = PyQt5.QtGui.QCursor()
        curs.setShape(PyQt5.QtCore.Qt.CursorShape.PointingHandCursor)

        self.buttonUser = PyQt5.QtWidgets.QPushButton("Войти")
        self.buttonUser.setFont(PyQt5.QtGui.QFont('Times new roman', 12))
        self.buttonUser.setCursor(curs)

        self.buttonExit = PyQt5.QtWidgets.QPushButton("Зарегистрироваться")
        self.buttonExit.setFont(PyQt5.QtGui.QFont('Times new roman', 12))
        self.buttonExit.setCursor(curs)

        self.vline = components.VLine.VLine(10, 50)

        self.initUI()

    def initUI(self):

        self.vline.setHeight(20)
        self.hl.addWidget(self.buttonUser)
        self.hl.addWidget(self.vline)
        self.hl.addWidget(self.buttonExit)
        self.hl.setAlignment(PyQt5.QtCore.Qt.AlignLeft)
