import PyQt6.QtWidgets
import PyQt6.QtGui
import PyQt6.QtCore
import Components.VLine

class EnterComponent(PyQt6.QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hl = PyQt6.QtWidgets.QHBoxLayout(self)

        curs = PyQt6.QtGui.QCursor()
        curs.setShape(PyQt6.QtCore.Qt.CursorShape.PointingHandCursor)

        self.buttonUser = PyQt6.QtWidgets.QPushButton("Войти")
        self.buttonUser.setFont(PyQt6.QtGui.QFont('Times new roman', 12))
        self.buttonUser.setCursor(curs)


        self.initUI()

    def initUI(self):
        self.hl.addWidget(self.buttonUser)
        self.hl.setAlignment(PyQt6.QtCore.Qt.AlignmentFlag.AlignLeft)
