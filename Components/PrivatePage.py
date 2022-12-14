from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QLayout, QLabel
import Program.Constrains

from API.apps import Authors, Users
from Program.Networking import NETWORK_MANAGER
from Components.ScaledPicture import ScaledPicture

class PrivatePageComponent(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        user = Users.current()
        name = user['username']
        imageUrl = user.get('photo')
        mail = user['email']
        staff = user['is_staff']

        self.vl = QtWidgets.QVBoxLayout(self)
        self.hlSup = QtWidgets.QHBoxLayout()
        self.vlSup = QtWidgets.QVBoxLayout()
        self.name = QLabel()
        self.name.setText(name)

        self.name.setFont(Program.Constrains.DEFAULT_CONSTRAINS.titleFont)
        self.name.setSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        if imageUrl is None:
            self.picture = ScaledPicture('./Images/undefined.png')
        else:
            image = NETWORK_MANAGER.httpGetImage(QUrl(imageUrl))
            self.picture = ScaledPicture('', image)

        self.picture.setFixedSize(200, 250)
        self.picture.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        self.mail = QtWidgets.QTextEdit('Электронная почта пользователя: ' + mail)
        self.mail.setAlignment(QtCore.Qt.AlignmentFlag.AlignJustify)
        self.mail.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        self.mail.setFont(Program.Constrains.DEFAULT_CONSTRAINS.mainFont)
        if staff:
            self.staff = QtWidgets.QTextEdit('Роль пользователя: администратор')
        else:
            self.staff = QtWidgets.QTextEdit('Роль пользователя: читатель')
        self.staff.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        self.staff.setFont(Program.Constrains.DEFAULT_CONSTRAINS.mainFont)
        self.initUI()

    def initUI(self):
        self.vl.addWidget(self.name)
        self.hlSup.addWidget(self.picture)

        self.vlSup.addWidget(self.mail)
        self.vlSup.addWidget(self.staff)
        self.hlSup.addLayout(self.vlSup)

        self.vl.addLayout(self.hlSup)
        self.name.setStyleSheet("QLabel {background-color: yellow;}")
        self.name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)