from requests import HTTPError
from API.apps import Auth, Users, UserTypes
from PyQt5 import QtGui, QtWidgets
import Program.GlStack
import componets.UserComponent
import componets.EnterComponent
import componets.TopComponent
import forms.MainPage
import forms.BookList
import forms.AuthorList
import forms.EntryForm
from API.store import Store
from forms.AuthorDetails import AuthorDetails
from forms.Bookshelf import Bookshelf
from forms.PrivatePage import PrivatePage


class MainWidget(QtWidgets.QWidget):
    def getTopComponentGuest(self, withoutConnect: bool = False):
        a = componets.TopComponent.TopComponent(componets.EnterComponent.EnterComponent())
        if not withoutConnect:
            a.left.buttonUser.clicked.connect(self.toLogin)
            a.refC.main.clicked.connect(self.toMainMove)
            a.refC.books.clicked.connect(self.toBookList)
            a.refC.authers.clicked.connect(self.toAuthorList)
            return a

        return a

    def getTopComponentAuth(self, withoutConnect: bool = False):
        a = componets.TopComponent.TopComponent(componets.UserComponent.UserComponent())
        user = Users.current()
        a.left.buttonUser.setText(user['username'])
        if not withoutConnect:
            a.left.buttonUser.clicked.connect(self.addAndMovePrivateP) #toPrivatePage #todo Добавить переход на личную страницу
            a.left.buttonExit.clicked.connect(self.outLogin)
            a.left.buttonBooks.clicked.connect(self.addAndMoveBookshelf)
            a.refC.main.clicked.connect(self.toMainMove)
            a.refC.books.clicked.connect(self.toBookList)
            a.refC.authers.clicked.connect(self.toAuthorList)
            return a
        return a


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Онлайн библиотека (Локальное приложение)')
        icon = QtGui.QIcon('./images/lib.png')
        self.setWindowIcon(icon)

        # Основные элементы
        self.stack = QtWidgets.QStackedWidget()
        self.vl = QtWidgets.QVBoxLayout()

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
        type = Users.get_user_type()
        if type == UserTypes.GUEST:
            self.mainW = forms.MainPage.MainPage(self.getTopComponentGuest())
            self.stack.addWidget(self.mainW)

            self.AListW = forms.AuthorList.AuthorList(self.getTopComponentGuest())
            self.AListW.initButtons(lambda slug: self.addAndMoveAuthorD(slug))
            self.stack.addWidget(self.AListW)

            self.BListW = forms.BookList.BookList(self.getTopComponentGuest())
            self.stack.addWidget(self.BListW)

        else:
            self.mainW = forms.MainPage.MainPage(self.getTopComponentAuth())
            self.stack.addWidget(self.mainW)

            self.AListW = forms.AuthorList.AuthorList(self.getTopComponentAuth())
            self.AListW.initButtons(lambda slug: self.addAndMoveAuthorD(slug))
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
            self.enterWidget.enter.toGreen()
            self.reinitTopComponent()
        except HTTPError as err:
            if err.response.status_code == 400:
                self.enterWidget.enter.statusOutput.setText('Неправильное имя или пароль!')
                self.enterWidget.enter.toRed()
            else:
                self.enterWidget.enter.statusOutput.setText('Неожиданная http ошибка!')
                self.enterWidget.enter.toRed()
                print(err)
                print(err.response.json())

    def initGI(self):
        self.vl.addWidget(self.stack)
        self.setLayout(self.vl)
        self.stack.setCurrentIndex(0)

    def CTD1(self, wid):
        self.stack.removeWidget(wid),
        self.stack.setCurrentIndex(0),
        self.outLogin()
        return

    def CTD1_alt(self, wid):
        self.stack.removeWidget(wid),
        self.stack.setCurrentIndex(0),
        self.toLogin()
        return

    def CTD2(self, wid):
        self.stack.removeWidget(wid)
        self.toMainMove()
        return

    def CTD3(self, wid):
        self.stack.removeWidget(wid)
        self.toBookList()
        return

    def CTD4(self, wid):
        self.stack.removeWidget(wid)
        self.toAuthorList()
        return

    def CTD_user(self, wid):
        self.stack.removeWidget(wid)
        self.addAndMovePrivateP()
        return

    def CTD_bookshelf(self, wid):
        self.stack.removeWidget(wid)
        self.addAndMoveBookshelf()
        return

    def connectTopWithDelete(self, toDelete):
        if isinstance(toDelete.top.left, componets.UserComponent.UserComponent):
            toDelete.top.left.buttonBooks.clicked.connect(lambda: self.CTD_bookshelf(toDelete))
            toDelete.top.left.buttonUser.clicked.connect(lambda: self.CTD_user(toDelete))
            toDelete.top.left.buttonExit.clicked.connect(lambda: self.CTD1(toDelete))
            toDelete.top.refC.main.clicked.connect(lambda: self.CTD2(toDelete))
            toDelete.top.refC.books.clicked.connect(lambda: self.CTD3(toDelete))
            toDelete.top.refC.authers.clicked.connect(lambda: self.CTD4(toDelete))
            return

        toDelete.top.left.buttonUser.clicked.connect(lambda: self.CTD1_alt(toDelete))
        toDelete.top.refC.main.clicked.connect(lambda: self.CTD2(toDelete))
        toDelete.top.refC.books.clicked.connect(lambda: self.CTD3(toDelete))
        toDelete.top.refC.authers.clicked.connect(lambda: self.CTD4(toDelete))

    def addAndMoveAuthorD(self, slug):
        type = Users.get_user_type()
        if type == UserTypes.GUEST:
            self.addition = AuthorDetails(self.getTopComponentGuest(True), slug)
        else:
            self.addition = AuthorDetails(self.getTopComponentAuth(True), slug)
        self.connectTopWithDelete(self.addition)
        self.stack.addWidget(self.addition)

        self.stack.setCurrentIndex(3)

    def addAndMovePrivateP(self):
        self.addition = PrivatePage(self.getTopComponentAuth(True))
        self.connectTopWithDelete(self.addition)
        self.stack.addWidget(self.addition)
        self.stack.setCurrentIndex(3)

    def addAndMoveBookshelf(self):
        self.addition = Bookshelf(self.getTopComponentAuth(True))
        self.connectTopWithDelete(self.addition)
        self.stack.addWidget(self.addition)
        self.stack.setCurrentIndex(3)