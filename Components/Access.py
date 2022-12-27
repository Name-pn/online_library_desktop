import PyQt6.QtCore
import PyQt6.QtGui
import PyQt6.QtWidgets
from PyQt6 import QtGui


class AccessComponent(PyQt6.QtWidgets.QWidget):

    def __init__(self, f, parent=None):
        super().__init__(parent)
        self.f = f
        self.vl = PyQt6.QtWidgets.QVBoxLayout(self)
        self.hl = PyQt6.QtWidgets.QHBoxLayout()
        self.vlLeft = PyQt6.QtWidgets.QVBoxLayout()
        self.vlRight = PyQt6.QtWidgets.QVBoxLayout()

        self.enterToSyte = PyQt6.QtWidgets.QPushButton("Войти")
        self.enterToSyte.setFont(QtGui.QFont("Times new roman", 12))

        self.nameLabel = PyQt6.QtWidgets.QTextEdit("")
        self.passwordLabel = PyQt6.QtWidgets.QTextEdit("")
        self.statusLabel = PyQt6.QtWidgets.QTextBrowser()
        self.statusOutput = PyQt6.QtWidgets.QTextBrowser()

        self.nameInput = PyQt6.QtWidgets.QTextBrowser()
        self.passwordInput = PyQt6.QtWidgets.QTextBrowser()

        self.nameLabel.setAlignment(PyQt6.QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.statusLabel.setAlignment(PyQt6.QtCore.Qt.AlignmentFlag.AlignVCenter)

        self.nameInput.setAlignment(PyQt6.QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.passwordInput.setAlignment(PyQt6.QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.passwordLabel.setAlignment(PyQt6.QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.statusOutput.setAlignment(PyQt6.QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.nameLabel.setFont(QtGui.QFont("Times new roman", 16))
        self.statusLabel.setFont(QtGui.QFont("Times new roman", 16))

        self.nameInput.setFont(QtGui.QFont("Times new roman", 16))
        self.passwordInput.setFont(QtGui.QFont("Times new roman", 16))

        self.passwordLabel.setFont(QtGui.QFont("Times new roman", 16))
        self.statusOutput.setFont(QtGui.QFont("Times new roman", 16))

        self.initUI()

    def initUI(self):
        self.nameInput.setText("Имя пользователя:")
        self.statusLabel.setText("Статус:")
        self.statusOutput.setText("Ожидаю ввод пользователя")

        self.passwordInput.setText("Пароль:")

        self.vlLeft.addWidget(self.nameInput)
        self.vlLeft.addWidget(self.passwordInput)
        self.vlLeft.addWidget(self.statusLabel)

        self.vlRight.addWidget(self.nameLabel)
        self.vlRight.addWidget(self.passwordLabel)
        self.vlRight.addWidget(self.statusOutput)

        self.hl.addLayout(self.vlLeft)
        self.hl.addLayout(self.vlRight)

        self.vl.addLayout(self.hl)
        self.vl.addWidget(self.enterToSyte)

        self.setLayout(self.vl)

    def reinit(self):
        self.nameLabel.setText('')
        self.passwordLabel.setText('')

        self.statusOutput.setText('Программа ожидает ввод пользователя')

        self.toWhite()

    def toRed(self):
        self.statusOutput.setStyleSheet("QTextEdit {background-color: red;}")

    def toGreen(self):
        self.statusOutput.setStyleSheet("QTextEdit {background-color: green;"
                                        "color: white;"
                                        "}")
        self.f()

    def toWhite(self):
        self.statusOutput.setStyleSheet("QTextEdit {background-color: white;}")
