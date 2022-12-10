import PyQt5.QtWidgets
import PyQt5.QtGui
import PyQt5.QtCore
import additionWidgets.VLine
import additionWidgets.Plug

class UserComponent(PyQt5.QtWidgets.QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.hlFirst = PyQt5.QtWidgets.QHBoxLayout(self)
        self.hl = PyQt5.QtWidgets.QHBoxLayout()
        self.imageForm = PyQt5.QtWidgets.QLabel("some text")
        self.image = PyQt5.QtGui.QPixmap(".\images\man.png")

        self.buttonUser = PyQt5.QtWidgets.QPushButton("User")
        self.buttonExit = PyQt5.QtWidgets.QPushButton("Выйти")
        self.vline = additionWidgets.VLine.VLine(10, 50)
        self.vline2 = additionWidgets.VLine.VLine(10, 50)
        self.space = PyQt5.QtWidgets.QSpacerItem(int(self.width()*2/4), 0)

        self.plug = additionWidgets.Plug.Plug(None)

        self.initUI()

    def initUI(self):
        self.hl.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        self.image = self.image.scaled(30, 30)
        self.imageForm.setPixmap(self.image)
        self.vline.setHeight(self.image.height())
        self.vline2.setHeight(self.image.height())
        self.hl.addWidget(self.imageForm)
        self.hl.addWidget(self.vline)
        self.hl.addWidget(self.buttonUser)
        self.hl.addWidget(self.vline2)
        self.hl.addWidget(self.buttonExit)
        self.hl.addSpacerItem(self.space)

        self.hlFirst.addWidget(self.plug)
        self.hlFirst.addLayout(self.hl)