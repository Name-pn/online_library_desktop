import PyQt6
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QTextEdit, QDateEdit, QListWidget, QHBoxLayout, QVBoxLayout, QTextBrowser, \
    QAbstractItemView, QListWidgetItem, QDateTimeEdit, QSizePolicy
import Program.Constrains

class myItem(QListWidgetItem):
    def __init__(self, str, key, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText(str)
        self.key = key

    def getKey(self):
        return self.key

class MultiFilter(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list = QListWidget()
        self.timeFrom = QDateEdit()
        self.timeTo = QDateEdit()
        self.timeHL = QHBoxLayout()
        self.listHL = QHBoxLayout()
        self.nameHL = QHBoxLayout()
        self.textInput = QTextEdit('')
        self.textBr1 = QTextBrowser()
        self.textBr2 = QTextBrowser()
        self.textBr3 = QTextBrowser()
        self.vl = QVBoxLayout(self)

        self.property = Program.Constrains.DEFAULT_CONSTRAINS.genres
        for el in self.property:
            self.list.addItem(myItem(el['name'], el['slug']))

        self.initGI()

    def initGI(self):
        self.textBr1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.textBr2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.textBr3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.textBr1.setText('Жанровый фильтр')
        self.textBr2.setText('Временной фильтр')
        self.textBr2.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        self.textBr3.setText('Фильтр по автору')
        self.list.setFont(PyQt6.QtGui.QFont('Times new roman', 16))
        self.list.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.timeFrom.setFont(PyQt6.QtGui.QFont('Times new roman', 16))
        self.timeFrom.setDisplayFormat('yyyy год')
        self.timeTo.setDisplayFormat('yyyy год')
        self.timeFrom.setCurrentSection(QDateTimeEdit.Section.YearSection)
        self.timeFrom.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.timeTo.setCurrentSection(QDateTimeEdit.Section.YearSection)
        self.timeTo.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.timeTo.setFont(PyQt6.QtGui.QFont('Times new roman', 16))
        self.textInput.setFont(PyQt6.QtGui.QFont('Times new roman', 16))
        self.textBr1.setFont(PyQt6.QtGui.QFont('Times new roman', 16))
        self.textBr2.setFont(PyQt6.QtGui.QFont('Times new roman', 16))
        self.textBr3.setFont(PyQt6.QtGui.QFont('Times new roman', 16))

        self.timeHL.addWidget(self.textBr2)
        self.timeHL.addWidget(self.timeFrom)
        self.timeHL.addWidget(self.timeTo)

        self.listHL.addWidget(self.textBr1)
        self.listHL.addWidget(self.list)

        self.nameHL.addWidget(self.textBr3)
        self.nameHL.addWidget(self.textInput)

        self.vl.addLayout(self.listHL)
        self.vl.addLayout(self.timeHL)
        self.vl.addLayout(self.nameHL)
