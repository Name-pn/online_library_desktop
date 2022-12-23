from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QLayout, QLabel

from API.apps import Authors, Users
from Program.Networking import NETWORK_MANAGER
from componets.ScaledPicture import ScaledPicture

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

        self.name.setFont(QtGui.QFont("Helvetica", 16))
        self.name.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        if imageUrl is None:
            self.picture = ScaledPicture('./images/undefined.png')
        else:
            image = NETWORK_MANAGER.httpGetImage(QUrl(imageUrl))
            self.picture = ScaledPicture('', image)
        self.picture.setBaseSize(200, 100)
        self.picture.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        self.mail = QtWidgets.QTextEdit('Электронная почта пользователя: ' + mail)
        self.mail.setAlignment(QtCore.Qt.AlignJustify)
        self.mail.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        if staff:
            self.staff = QtWidgets.QTextEdit('Роль пользователя: администратор')
        else:
            self.staff = QtWidgets.QTextEdit('Роль пользователя: читатель')
        self.staff.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
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