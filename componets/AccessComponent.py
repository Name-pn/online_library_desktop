import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWidgets


class AccessComponent(PyQt5.QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.vl = PyQt5.QtWidgets.QVBoxLayout(self)
        self.hl = PyQt5.QtWidgets.QHBoxLayout()
        self.vlLeft = PyQt5.QtWidgets.QVBoxLayout()
        self.vlRight = PyQt5.QtWidgets.QVBoxLayout()

        self.enterToSyte = PyQt5.QtWidgets.QPushButton("Войти")

        self.nameLabel = PyQt5.QtWidgets.QTextEdit("")
        #self.nameLabel.setCurrentCharFormat()
        self.passwordLabel = PyQt5.QtWidgets.QTextEdit("")

        self.nameInput = PyQt5.QtWidgets.QTextBrowser()
        self.passwordInput = PyQt5.QtWidgets.QTextBrowser()

        self.initUI()

    def initUI(self):
        #self.nameInput.setSizePolicy(PyQt5.QtWidgets.QSizePolicy.Minimum, PyQt5.QtWidgets.QSizePolicy.Minimum)
        #self.passwordInput.setSizePolicy(PyQt5.QtWidgets.QSizePolicy.Minimum, PyQt5.QtWidgets.QSizePolicy.Minimum)
        #self.setSizePolicy(PyQt5.QtWidgets.QSizePolicy.Minimum, PyQt5.QtWidgets.QSizePolicy.Minimum)
        self.nameInput.setText("Имя пользователя:")

        self.passwordInput.setText("Пароль:")
        self.nameInput.setMinimumSize(100, 25)
        self.passwordInput.setMinimumSize(100, 25)
        self.passwordInput.setSizePolicy(PyQt5.QtWidgets.QSizePolicy.Minimum, PyQt5.QtWidgets.QSizePolicy.Minimum)
        self.nameInput.setSizePolicy(PyQt5.QtWidgets.QSizePolicy.Minimum, PyQt5.QtWidgets.QSizePolicy.Minimum)

        #self.nameInput.setMaximumSize(100, 25)
        #self.passwordInput.setMaximumSize(100, 25)
        #self.nameLabel.setMaximumSize(100, 25)
        #self.passwordLabel.setMaximumSize(100, 25)

        self.vlLeft.addWidget(self.nameInput)
        self.vlLeft.addWidget(self.passwordInput)

        self.vlRight.addWidget(self.nameLabel)
        self.vlRight.addWidget(self.passwordLabel)

        self.hl.addLayout(self.vlLeft)
        self.hl.addLayout(self.vlRight)

        self.vl.addLayout(self.hl)
        self.vl.addWidget(self.enterToSyte)

        #self.hl.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        #self.vl.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        self.setLayout(self.vl)
