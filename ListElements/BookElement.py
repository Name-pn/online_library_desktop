from PyQt5 import QtWidgets, QtGui, QtCore

from API.apps import Authors

class BookElement(QtWidgets.QWidget):

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
        self.name.setText(self.properties.get('title'))
        self.font = QtGui.QFont("Helvetica", 16)
        self.name.setFont(self.font)

        self.picture = self.initPicture()

        self.authorName = self.initAuthorNameLabel()

        self.annotation = QtWidgets.QTextBrowser()
        self.annotation.setText('Аннотация: ' + self.properties.get('description'))
        self.annotation.setAlignment(QtCore.Qt.AlignJustify)

        self.genres = self.initGenres()

        self.date = QtWidgets.QLabel()
        self.date.setText('Год выпуска: ' + str(self.properties.get('year_of_writing')))

        self.button = QtWidgets.QPushButton('Перейти к описанию')

        self.spacer1 = QtWidgets.QSpacerItem(100, 100)
        self.spacer2 = QtWidgets.QSpacerItem(100, 100)

        # Лейауты
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainHLayout = QtWidgets.QHBoxLayout(self)
        self.infoAndPictureLayout = QtWidgets.QHBoxLayout()
        self.InfoLayout = QtWidgets.QVBoxLayout()

        self.initUI()

    def initAuthorNameLabel(self):
        author = Authors.get_detail(self.properties.get('author'))

        authorName = QtWidgets.QLabel()
        authorName.setText(f"Автор: {author.get('name')} {author.get('surname')}")

        return authorName

    def initPicture(self) -> QtWidgets.QLabel:
        picture = QtWidgets.QLabel()

        if self.properties.get('cover') is None:
            picture.setPixmap(QtGui.QPixmap('./images/book.png'))
        else:
            picture.setPixmap(
                QtGui.QPixmap('./images/book.png'))  # todo Загрузить с сервера обложки, вставить в pixmap

        return picture

    def initGenres(self):
        genresNames = [genre['name'].lower() for genre in self.properties['genres']]

        genresLabel = QtWidgets.QLabel()
        genresLabel.setText('Жанры: ' + ', '.join(genresNames))
        genresLabel.setWordWrap(True)  # Перенос текста на следующую строку

        return genresLabel

    def initUI(self):
        # self.vl.setAlignment(PyQt5.QtCore.Qt.AlignRight)
        self.mainLayout.addWidget(self.name)

        self.infoAndPictureLayout.addWidget(self.picture)

        self.InfoLayout.addWidget(self.authorName)
        self.InfoLayout.addWidget(self.annotation)
        self.InfoLayout.addWidget(self.genres)
        self.InfoLayout.addWidget(self.date)

        self.infoAndPictureLayout.addLayout(self.InfoLayout)

        self.mainLayout.addLayout(self.infoAndPictureLayout)
        self.mainLayout.addWidget(self.button)

        self.mainHLayout.addLayout(self.mainLayout)
        self.mainHLayout.setAlignment(QtCore.Qt.AlignCenter)
