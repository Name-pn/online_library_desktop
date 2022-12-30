from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QSizePolicy

import Program.Constrains

from Program.Networking import NETWORK_MANAGER

class AutherElement(QtWidgets.QWidget):

    def paintEvent(self, a0: QtGui.QPaintEvent):
        painter = QtGui.QPainter(self)
        brush = QtGui.QBrush(QtGui.QColor(255, 253, 98))
        painter.setBrush(brush)
        painter.drawRect(0, 0, self.width(), self.height())

    def __init__(self, properties: dict, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Свойства-данные объекта
        self.properties = properties

        # Виджеты-компоненты
        self.name = QtWidgets.QLabel()
        self.name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name.setText(self.properties.get('name') + ' ' + self.properties.get('surname'))
        self.font = Program.Constrains.DEFAULT_CONSTRAINS.mainFont
        self.name.setFont(Program.Constrains.DEFAULT_CONSTRAINS.titleBoldFont)
        self.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        self.name.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.picture = self.initPicture(300, 400)

        self.annotation = QtWidgets.QTextBrowser()
        self.annotation.setText('Описание: ' + self.properties.get('description'))
        self.annotation.setMinimumWidth(500)
        self.annotation.setAlignment(QtCore.Qt.AlignmentFlag.AlignJustify)
        self.annotation.setFont(Program.Constrains.DEFAULT_CONSTRAINS.mainFont)
        self.annotation.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.button = QtWidgets.QPushButton('Перейти к личной странице')
        self.button.setFont(Program.Constrains.DEFAULT_CONSTRAINS.buttonsFont)
        self.button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        # Лейауты
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainHLayout = QtWidgets.QHBoxLayout(self)
        self.infoAndPictureLayout = QtWidgets.QHBoxLayout()
        self.InfoLayout = QtWidgets.QVBoxLayout()

        self.initUI()

    def initButton(self, f):
        self.button.clicked.connect(lambda: f(self.properties['slug']))

    def initPicture(self, x, y) -> QtWidgets.QLabel:
        picture = QtWidgets.QLabel()
        picture.setFixedSize(x, y)
        if self.properties['image'] is None:
            picture.setPixmap(QtGui.QPixmap('./Images/undefined.png').scaled(100, 100))
        else:
            image = NETWORK_MANAGER.httpGetImage(QUrl(self.properties['image']))
            pixmap = QtGui.QPixmap.fromImage(image)

            pixmap = pixmap.scaled(picture.size())
            picture.setPixmap(pixmap)


            #picture.setPixmap(QtGui.QPixmap('./Images/undefined.png'))  # todo Масштабирование бы поправить


        return picture

    def initUI(self):
        self.mainLayout.addWidget(self.name)

        self.infoAndPictureLayout.addWidget(self.picture)

        self.InfoLayout.addWidget(self.annotation)

        self.infoAndPictureLayout.addLayout(self.InfoLayout)

        self.mainLayout.addLayout(self.infoAndPictureLayout)
        self.mainLayout.addWidget(self.button)

        self.mainHLayout.addLayout(self.mainLayout)
        self.mainHLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

