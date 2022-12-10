import PyQt5.QtWidgets
import PyQt5.QtGui
import PyQt5.QtCore
import additionWidgets.VLine
import additionWidgets.Plug

class AccessComponent(PyQt5.QtWidgets.QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)

        self.hl = PyQt5.QtWidgets.QHBoxLayout()
        self.vl = PyQt5.QtWidgets.QVBoxLayout(self)
        self.vlLeft = PyQt5.QtWidgets.QVBoxLayout()
        self.vlRight = PyQt5.QtWidgets.QVBoxLayout()

        self.enterToSyte = PyQt5.QtWidgets.QPushButton("Войти")

        self.name = PyQt5.QtWidgets.QTextEdit("Введите логин")
        self.password = PyQt5.QtWidgets.QTextEdit("Введите пароль")

        self.nameInput = PyQt5.QtWidgets.QTextBrowser()
        self.passwordInput = PyQt5.QtWidgets.QTextBrowser()

        self.initUI()

    def initUI(self):
        self.nameInput.setText("Имя пользователя:")
        self.passwordInput.setText("Пароль:")

        self.vlLeft.addWidget(self.nameInput)
        self.vlLeft.addWidget(self.passwordInput)

        self.vlRight.addWidget(self.name)
        self.vlRight.addWidget(self.password)

        self.hl.addLayout(self.vlLeft)
        self.hl.addLayout(self.vlRight)

        self.vl.addLayout(self.hl)
        self.vl.addWidget(self.enterToSyte)
