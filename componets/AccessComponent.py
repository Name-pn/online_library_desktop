import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWidgets


class AccessComponent(PyQt5.QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.hl = PyQt5.QtWidgets.QHBoxLayout()
        self.vl = PyQt5.QtWidgets.QVBoxLayout(self)
        self.vlLeft = PyQt5.QtWidgets.QVBoxLayout()
        self.vlRight = PyQt5.QtWidgets.QVBoxLayout()

        self.enterToSyte = PyQt5.QtWidgets.QPushButton("Войти")

        self.nameLabel = PyQt5.QtWidgets.QTextEdit("Введите логин")
        self.passwordLabel = PyQt5.QtWidgets.QTextEdit("Введите пароль")

        self.nameInput = PyQt5.QtWidgets.QTextBrowser()
        self.passwordInput = PyQt5.QtWidgets.QTextBrowser()

        self.initUI()

    def initUI(self):
        self.nameInput.setText("Имя пользователя:")
        self.passwordInput.setText("Пароль:")

        self.vlLeft.addWidget(self.nameInput)
        self.vlLeft.addWidget(self.passwordInput)

        self.vlRight.addWidget(self.nameLabel)
        self.vlRight.addWidget(self.passwordLabel)

        self.hl.addLayout(self.vlLeft)
        self.hl.addLayout(self.vlRight)

        self.vl.addLayout(self.hl)
        self.vl.addWidget(self.enterToSyte)
