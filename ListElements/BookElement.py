import PyQt5.QtWidgets
import PyQt5.QtGui
import PyQt5.QtCore

from API.apps import Authors


class BookElement(PyQt5.QtWidgets.QWidget):
    def __init__(self, properties: dict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.properties = properties
        self.vl = PyQt5.QtWidgets.QVBoxLayout(self)
        self.name = PyQt5.QtWidgets.QTextBrowser()
        self.name.setText(properties.get('title'))

        self.hl = PyQt5.QtWidgets.QHBoxLayout()

        self.picture = PyQt5.QtWidgets.QLabel()
        if self.properties.get('cover') is None:
            self.picture.setPixmap(PyQt5.QtGui.QPixmap('./images/book.png'))
        else:
            self.picture.setPixmap(PyQt5.QtGui.QPixmap('./images/book.png')) # todo Загрузить с сервера обложки, вставить в pixmap

        self.vlIn = PyQt5.QtWidgets.QVBoxLayout()

        self.author = Authors.get_detail(properties.get('author'))

        self.autherName = PyQt5.QtWidgets.QTextBrowser()
        self.autherName.setText(self.author.get('name') + ' ' + self.author.get('surname'))

        self.annotation = PyQt5.QtWidgets.QTextBrowser()
        self.annotation.setText('Аннотация: ' + properties.get('description'))

        self.date = PyQt5.QtWidgets.QTextBrowser()
        self.date.setText('Год выпуска: ' + str(properties.get('year_of_writing')))

        self.button = PyQt5.QtWidgets.QPushButton('Перейти к описанию')

        self.initUI()

    def initUI(self):
        #self.vl.setAlignment(PyQt5.QtCore.Qt.AlignRight)
        self.vl.addWidget(self.name)

        self.hl.addWidget(self.picture)

        self.vlIn.addWidget(self.autherName)
        self.vlIn.addWidget(self.annotation)
        self.vlIn.addWidget(self.date)


        self.hl.addLayout(self.vlIn)

        self.vl.addLayout(self.hl)
        self.vl.addWidget(self.button)