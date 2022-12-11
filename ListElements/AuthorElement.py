from PyQt5 import QtWidgets, QtGui, QtCore

from API.apps import Authors

class AutherElement(QtWidgets.QWidget):

    def paintEvent(self, a0: QtGui.QPaintEvent):
        painter = QtGui.QPainter(self)
        brush = QtGui.QBrush(QtCore.Qt.yellow)
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
        self.font = QtGui.QFont("Helvetica", 16)
        self.name.setFont(self.font)

        self.picture = self.initPicture()

        self.annotation = QtWidgets.QTextBrowser()
        self.annotation.setText('Описание: ' + self.properties.get('description'))
        self.annotation.setAlignment(QtCore.Qt.AlignJustify)

        self.button = QtWidgets.QPushButton('Перейти к личной странице')

        self.spacer1 = QtWidgets.QSpacerItem(100, 100)
        self.spacer2 = QtWidgets.QSpacerItem(100, 100)

        # Лейауты
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainHLayout = QtWidgets.QHBoxLayout(self)
        self.infoAndPictureLayout = QtWidgets.QHBoxLayout()
        self.InfoLayout = QtWidgets.QVBoxLayout()

        self.initUI()

    def initPicture(self) -> QtWidgets.QLabel:
        picture = QtWidgets.QLabel()

        if self.properties.get('cover') is None:
            picture.setPixmap(QtGui.QPixmap('./images/undefined.png').scaled(100, 100))
        else:
            picture.setPixmap(
                QtGui.QPixmap('./images/undefined.png'))  # todo Загрузить с сервера обложки, вставить в pixmap


        return picture

    def initUI(self):
        self.mainLayout.addWidget(self.name)

        self.infoAndPictureLayout.addWidget(self.picture)

        self.InfoLayout.addWidget(self.annotation)

        self.infoAndPictureLayout.addLayout(self.InfoLayout)

        self.mainLayout.addLayout(self.infoAndPictureLayout)
        self.mainLayout.addWidget(self.button)

        self.mainHLayout.addLayout(self.mainLayout)
        self.mainHLayout.setAlignment(QtCore.Qt.AlignCenter)
