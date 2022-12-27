from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import QUrl

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
        self.font = QtGui.QFont("Times new roman", 16)
        self.name.setFont(self.font)

        self.picture = self.initPicture()

        self.annotation = QtWidgets.QTextBrowser()
        self.annotation.setText('Описание: ' + self.properties.get('description'))
        self.annotation.setAlignment(QtCore.Qt.AlignmentFlag.AlignJustify)
        self.annotation.setFont(QtGui.QFont("Times new roman", 16))

        self.button = QtWidgets.QPushButton('Перейти к личной странице')
        self.button.setFont(QtGui.QFont("Times new roman", 12))

        # Лейауты
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainHLayout = QtWidgets.QHBoxLayout(self)
        self.infoAndPictureLayout = QtWidgets.QHBoxLayout()
        self.InfoLayout = QtWidgets.QVBoxLayout()

        self.initUI()

    def initButton(self, f):
        self.button.clicked.connect(lambda: f(self.properties['slug']))

    def initPicture(self) -> QtWidgets.QLabel:
        picture = QtWidgets.QLabel()
        picture.setMaximumSize(100, 200)
        if self.properties['image'] is None:
            picture.setPixmap(QtGui.QPixmap('./images/undefined.png').scaled(100, 100))
        else:
            image = NETWORK_MANAGER.httpGetImage(QUrl(self.properties['image']))
            pixmap = QtGui.QPixmap.fromImage(image)

            pixmap = pixmap.scaled(picture.size())
            picture.setPixmap(pixmap)
            #picture.setPixmap(QtGui.QPixmap('./images/undefined.png'))  # todo Масштабирование бы поправить


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
