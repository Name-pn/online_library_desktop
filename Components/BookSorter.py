from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import Qt, QObject, QDate
from PyQt6.QtWidgets import QWidget, QListWidget, QDateEdit, QVBoxLayout, QDateTimeEdit, QComboBox, QTextBrowser, \
    QStackedWidget, QTextEdit, QPushButton, QSizePolicy, QHBoxLayout, QAbstractItemView

import Program.Constrains
from Components.BookList import TypeUpdateListBook
from Components.MultiFilter import MultiFilter, myItem


class Communicate(QObject):
    upsig = QtCore.pyqtSignal(int, str)

class BookSorter(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vl = QVBoxLayout(self)
        self.varyes = QComboBox()
        self.sig = Communicate()

        def stackChange():
            i = self.varyes.currentIndex()
            self.stack.setCurrentIndex(i)

        self.commentToTime = QTextBrowser(self)
        self.commentFromTime = QTextBrowser(self)

        self.varyes.currentIndexChanged.connect(stackChange)
        self.list = QListWidget()
        self.timeFrom = QDateEdit()
        self.timeTo = QDateEdit()
        self.property = Program.Constrains.DEFAULT_CONSTRAINS.genres
        self.text = QTextBrowser(self)
        self.stack = QStackedWidget()
        self.textInput = QTextEdit('')
        self.multi = MultiFilter()
        self.button = QPushButton('Активировать фильтр')

        self.zeroW = QWidget()
        self.initGI()

    def initGI(self):
        self.text.setText('Панель фильтров')
        self.text.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.text.setFont(Program.Constrains.DEFAULT_CONSTRAINS.mainFont)
        self.button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        self.varyes.setFont(Program.Constrains.DEFAULT_CONSTRAINS.mainFont)
        self.button.setFont(Program.Constrains.DEFAULT_CONSTRAINS.mainFont)
        self.textInput.setFont(Program.Constrains.DEFAULT_CONSTRAINS.mainFont)
        self.commentToTime.setFont(Program.Constrains.DEFAULT_CONSTRAINS.mainFont)
        self.commentFromTime.setFont(Program.Constrains.DEFAULT_CONSTRAINS.mainFont)
        self.commentToTime.setText('Заканчивая годом')
        self.commentToTime.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        self.commentFromTime.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        self.commentFromTime.setText('Начиная с года')

        self.vl.addWidget(self.text)
        self.vl.addWidget(self.varyes)
        self.vl.addWidget(self.stack)
        self.vl.addWidget(self.button)

        self.timeW = QWidget()
        self.timeHL = QHBoxLayout()
        self.timeVL1 = QVBoxLayout()
        self.timeVL2 = QVBoxLayout()
        self.timeVL1.addWidget(self.commentFromTime)
        self.timeVL1.addWidget(self.timeFrom)
        self.timeHL.addLayout(self.timeVL1)
        self.timeVL2.addWidget(self.commentToTime)
        self.timeVL2.addWidget(self.timeTo)
        self.timeHL.addLayout(self.timeVL2)
        self.timeW.setLayout(self.timeHL)

        self.varyes.addItem('По жанрам')
        self.varyes.addItem('По году издания')
        self.varyes.addItem('По автору')
        self.varyes.addItem('Расширенный фильтр')

        self.stack.addWidget(self.list)
        self.stack.addWidget(self.timeW)
        self.stack.addWidget(self.textInput)
        self.stack.addWidget(self.multi)

        self.timeFrom.setCurrentSection(QDateTimeEdit.Section.YearSection)
        self.timeFrom.setDisplayFormat('yyyy')
        self.timeFrom.setDate(QDate(1990, 1, 1))
        self.timeFrom.setFont(Program.Constrains.DEFAULT_CONSTRAINS.mainFont)
        self.timeFrom.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)

        self.timeTo.setCurrentSection(QDateTimeEdit.Section.YearSection)
        self.timeTo.setDisplayFormat('yyyy')
        self.timeTo.setDate(QDate(2010, 1, 1))
        self.timeTo.setFont(Program.Constrains.DEFAULT_CONSTRAINS.mainFont)
        self.timeTo.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)

        self.list.setFont(Program.Constrains.DEFAULT_CONSTRAINS.mainFont)
        self.list.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.list.setSortingEnabled(True)
        self.list.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        for el in self.property:
            self.list.addItem(myItem(el['name'], el['slug']))

        self.button.clicked.connect(lambda: self.sig.upsig.emit(self.getTypeStack(), self.getSlug()))

    def getTypeStack(self):
        i = self.stack.currentIndex()
        return i

    def getSlug(self):
        i = self.stack.currentIndex()
        i = TypeUpdateListBook(i)
        if i == TypeUpdateListBook.ALL:
            array = self.multi.list.selectedItems()
            res = ''
            for el in array:
                index = self.multi.list.indexFromItem(el)
                var = self.multi.list.itemFromIndex(index)
                res = res + var.getKey() + ', '
            ln = len(res)
            res = res[:(ln - 2)]+'|'+self.multi.timeFrom.text() + ' ' + self.multi.timeTo.text()+'|' + self.multi.textInput.toPlainText()
            return res
        elif i == TypeUpdateListBook.DATE:
            return self.timeFrom.text() + ' ' + self.timeTo.text()
        elif i == TypeUpdateListBook.GENRE:
            array = self.list.selectedItems()
            res = ''
            for el in array:
                index = self.list.indexFromItem(el)
                el = self.list.itemFromIndex(index)
                res = res + el.getKey() + ', '
            ln = len(res)
            return res[:(ln-2)]
        elif i == TypeUpdateListBook.AUTHOR:
            return self.textInput.toPlainText()