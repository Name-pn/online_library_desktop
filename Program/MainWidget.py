import copy

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

        def getTopComponent():
            a = componets.TopComponent.TopComponent(componets.EnterComponent.EnterComponent())
            a.comp.buttonUser.clicked.connect(self.toLogin)
            a.refC.main.clicked.connect(self.toMainMove)
            a.refC.books.clicked.connect(self.toBookList)
            a.refC.authers.clicked.connect(self.toAuthorList)

            return a

        a = forms.MainPage.MainPage(getTopComponent())
        self.stack.addWidget(a)

        b = forms.AuthorList.AuthorList(getTopComponent())
        self.stack.addWidget(b)

        c = forms.BookList.BookList(getTopComponent())
        self.stack.addWidget(c)

        self.stack.setMinimumSize(self.size())

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


    def initGI(self):
        self.vl.addWidget(self.stack)
        self.setLayout(self.vl)
        #self.setFixedSize(self.mainPage.size())
        self.stack.setCurrentIndex(0)