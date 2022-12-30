from PyQt6 import QtGui, QtCore, QtWidgets
from PyQt6.QtCore import QUrl
import Program.Constrains
import PyQt6.QtGui

from API.apps import Users
from Program.Networking import NETWORK_MANAGER
from Components.VLine import VLine


class UserComponent(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        curs = QtGui.QCursor()
        curs.setShape(PyQt6.QtCore.Qt.CursorShape.PointingHandCursor)

        self.hlFirst = QtWidgets.QHBoxLayout(self)
        self.hl = QtWidgets.QHBoxLayout()
        self.imageForm = QtWidgets.QLabel("some text")
        properties = Users.current()
        if properties['photo'] is None:
            self.image = QtGui.QPixmap(".\images\man.png")
        else:
            image = NETWORK_MANAGER.httpGetImage(QUrl(properties['photo']))
            self.image = QtGui.QPixmap.fromImage(image)

        self.buttonUser = QtWidgets.QPushButton("User")
        self.buttonUser.setFont(Program.Constrains.DEFAULT_CONSTRAINS.buttonsFont)
        self.buttonUser.setCursor(curs)

        self.buttonBooks = QtWidgets.QPushButton("Книжная полка")
        self.buttonBooks.setFont(Program.Constrains.DEFAULT_CONSTRAINS.buttonsFont)
        self.buttonBooks.setCursor(curs)

        self.buttonExit = QtWidgets.QPushButton("Выйти")
        self.buttonExit.setFont(Program.Constrains.DEFAULT_CONSTRAINS.buttonsFont)
        self.buttonExit.setCursor(curs)

        self.vline = VLine(10, 50)
        self.vline2 = VLine(10, 50)
        self.vline3 = VLine(10, 50)
        self.space = QtWidgets.QSpacerItem(int(self.width() * 2 / 4), 0)

        self.initUI()

    def initUI(self):
        self.hl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.image = self.image.scaled(30, 30)
        self.imageForm.setPixmap(self.image)
        self.vline.setHeight(self.image.height())
        self.vline2.setHeight(self.image.height())
        self.hl.addWidget(self.imageForm)
        self.hl.addWidget(self.vline)
        self.hl.addWidget(self.buttonUser)
        self.hl.addWidget(self.vline2)
        self.hl.addWidget(self.buttonBooks)
        self.hl.addWidget(self.vline3)
        self.hl.addWidget(self.buttonExit)
        self.hl.addSpacerItem(self.space)

        self.hlFirst.addLayout(self.hl)
