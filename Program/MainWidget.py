from requests import HTTPError
from API.apps import Auth, Users, UserTypes
from PyQt5 import QtGui, QtCore, QtWidgets
import Program.User
import componets.UserComponent
import componets.EnterComponent
import componets.TopComponent
import forms.MainPage
import forms.BookList
import forms.AuthorList
import forms.EntryForm

class MainWidget(QtWidgets.QWidget):

    def getTopComponentGuest(self):
        a = componets.TopComponent.TopComponent(componets.EnterComponent.EnterComponent())
        a.comp.buttonUser.clicked.connect(self.toLogin)
        a.refC.main.clicked.connect(self.toMainMove)
        a.refC.books.clicked.connect(self.toBookList)
        a.refC.authers.clicked.connect(self.toAuthorList)

        return a

    def getTopComponentAuth(self):
        a = componets.TopComponent.TopComponent(componets.UserComponent.UserComponent())
        user = Users.current()
        a.comp.buttonUser.setText(user['username'])
        #a.comp.buttonUser.clicked.connect(self.toLogin) #toPrivatePage
        a.comp.buttonExit.clicked.connect(self.outLogin)
        a.refC.main.clicked.connect(self.toMainMove)
        a.refC.books.clicked.connect(self.toBookList)
        a.refC.authers.clicked.connect(self.toAuthorList)

        return a

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Онлайн библиотека (Локальное приложение)')
        icon = QtGui.QIcon('./images/lib.png')
        self.setWindowIcon(icon)

        # Основные элементы
        self.user = Program.User.User()
        self.stack = QtWidgets.QStackedWidget()
        self.vl = QtWidgets.QVBoxLayout()

        # Событийные элементы
        # Элементы верхней панели
        self.userComponent = componets.UserComponent.UserComponent()
        self.enterComponent = componets.EnterComponent.EnterComponent()
        self.topComponent = componets.TopComponent.TopComponent(self.enterComponent)

        # Рабочие окна основного окна
        self.mainPage = forms.MainPage.MainPage(self.topComponent)
        #self.bookListPage = forms.BookList.BookList(self.topComponent)
        #self.authorListPage = forms.AuthorList.AuthorList(self.topComponent)

        # Окно входа
        self.enterWidget = forms.EntryForm.EntryForm(lambda: self.setEnabled(True))
        self.enterWidget.enter.enterToSyte.clicked.connect(self.runLogin)

        self.initStack()

        self.initGI()

    def toMainMove(self):
        self.stack.setCurrentIndex(0)

    def toAuthorList(self):
        self.stack.setCurrentIndex(1)

    def toBookList(self):
        self.stack.setCurrentIndex(2)

    def toLogin(self):
        self.enterWidget.show()
        self.setEnabled(False)
        self.enterWidget.setEnabled(True)

    def outLogin(self):
        Auth.logout()
        self.reinitTopComponent()

    def initStack(self):
        self.stack.setMinimumSize(self.size())
        type = Users.get_user_type()
        if type == UserTypes.GUEST:
            self.mainW = forms.MainPage.MainPage(self.getTopComponentGuest())
            self.stack.addWidget(self.mainW)

            self.AListW = forms.AuthorList.AuthorList(self.getTopComponentGuest())
            self.stack.addWidget(self.AListW)

            self.BListW = forms.BookList.BookList(self.getTopComponentGuest())
            self.stack.addWidget(self.BListW)

        else:
            self.mainW = forms.MainPage.MainPage(self.getTopComponentAuth())
            self.stack.addWidget(self.mainW)

            self.AListW = forms.AuthorList.AuthorList(self.getTopComponentAuth())
            self.stack.addWidget(self.AListW)

            self.BListW = forms.BookList.BookList(self.getTopComponentAuth())
            self.stack.addWidget(self.BListW)

    def reinitTopComponent(self):
        self.vl.removeWidget(self.stack)
        index = self.stack.currentIndex()
        self.stack = QtWidgets.QStackedWidget()
        self.initStack()

        self.stack.setCurrentIndex(index)
        self.vl.addWidget(self.stack)
        self.update()

    def runLogin(self):
        login = self.enterWidget.enter.nameLabel.toPlainText()
        password = self.enterWidget.enter.passwordLabel.toPlainText()
        try:
            Auth.login(login, password)
            self.enterWidget.enter.statusOutput.setText('Вы залогинились')
            self.reinitTopComponent()
        except HTTPError as err:
            if err.response.status_code == 400:
                self.enterWidget.enter.statusOutput.setText('Неправильное имя или пароль!')
            else:
                self.enterWidget.enter.statusOutput.setText('Неожиданная http ошибка!')
                print(err)
                print(err.response.json())

    def initGI(self):
        self.vl.addWidget(self.stack)
        self.setLayout(self.vl)
        self.stack.setCurrentIndex(0)