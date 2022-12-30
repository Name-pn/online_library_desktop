import PyQt6
from PyQt6.QtCore import Qt, QDate
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

        self.commentToTime = QTextBrowser(self)
        self.commentFromTime = QTextBrowser(self)

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
        self.list.setFont(Program.Constrains.DEFAULT_CONSTRAINS.mainFont)
        self.list.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.timeFrom.setFont(Program.Constrains.DEFAULT_CONSTRAINS.mainFont)
        self.timeFrom.setDisplayFormat('yyyy')
        self.timeFrom.setDate(QDate(1990, 1, 1))
        self.timeTo.setDisplayFormat('yyyy')
        self.timeTo.setDate(QDate(2010, 1, 1))
        self.timeFrom.setCurrentSection(QDateTimeEdit.Section.YearSection)
        self.timeFrom.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.timeTo.setCurrentSection(QDateTimeEdit.Section.YearSection)
        self.timeTo.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.timeTo.setFont(Program.Constrains.DEFAULT_CONSTRAINS.mainFont)
        self.textInput.setFont(Program.Constrains.DEFAULT_CONSTRAINS.mainFont)
        self.textBr1.setFont(Program.Constrains.DEFAULT_CONSTRAINS.mainFont)
        self.textBr2.setFont(Program.Constrains.DEFAULT_CONSTRAINS.mainFont)
        self.textBr3.setFont(Program.Constrains.DEFAULT_CONSTRAINS.mainFont)
        self.commentToTime.setFont(Program.Constrains.DEFAULT_CONSTRAINS.mainFont)
        self.commentFromTime.setFont(Program.Constrains.DEFAULT_CONSTRAINS.mainFont)
        self.commentToTime.setText('Заканчивая годом')
        self.commentToTime.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        self.commentFromTime.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        self.commentFromTime.setText('Начиная с года')

        self.timeHL.addWidget(self.textBr2)
        self.timeVL1 = QVBoxLayout()
        self.timeVL2 = QVBoxLayout()
        self.timeVL1.addWidget(self.commentFromTime)
        self.timeVL1.addWidget(self.timeFrom)
        self.timeHL.addLayout(self.timeVL1)
        self.timeVL2.addWidget(self.commentToTime)
        self.timeVL2.addWidget(self.timeTo)
        self.timeHL.addLayout(self.timeVL2)

        self.listHL.addWidget(self.textBr1)
        self.listHL.addWidget(self.list)

        self.nameHL.addWidget(self.textBr3)
        self.nameHL.addWidget(self.textInput)

        self.vl.addLayout(self.listHL)
        self.vl.addLayout(self.timeHL)
        self.vl.addLayout(self.nameHL)


