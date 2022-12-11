import PyQt5.QtWidgets
import PyQt5.QtGui
import PyQt5.QtCore
from PyQt5.QtNetwork import QNetworkAccessManager

import componets.UserComponent
import componets.EnterComponent
import componets.TopComponent
import forms.EntryForm
import forms.BookList
import forms.AuthorList
import Program.MainWidget
import forms.MainPage
import ListElements.BookElement
import sys

from pprint import pprint
from API.apps import Books, Authors, Genres
from ListElements.BookElement import BookElement

if __name__ != '__main__':
    authers = Authors.get_all()
    pprint(authers)

if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    #compComp = componets.UserComponent.UserComponent()
    #comp = componets.TopComponent.TopComponent(compComp)
    enterComponent = componets.EnterComponent.EnterComponent()
    topComponent = componets.TopComponent.TopComponent(enterComponent)
    #w = forms.MainPage.MainPage(topComponent)
    w = Program.MainWidget.MainWidget()
    #w2.resize(250, 150)
    #w2.move(300, 300)

    w.show()

    sys.exit(app.exec_())

if __name__ != '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    listBooks = [BookElement(book) for book in Books.get_all()]
    scrollArea = PyQt5.QtWidgets.QScrollArea()
    w = listBooks[0]

    class testW(PyQt5.QtWidgets.QWidget):
        arr = listBooks

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.vl = PyQt5.QtWidgets.QVBoxLayout(self)
            for item in self.arr:
                self.vl.addWidget(item)
    ex = testW()
    scrollArea.setWidget(ex)
    scrollArea.setVerticalScrollBarPolicy(PyQt5.QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
    scrollArea.show()
    scrollArea.setWindowTitle('Desktop library')
    icon = PyQt5.QtGui.QIcon('./images/lib.png')
    scrollArea.setWindowIcon(icon)
    scrollArea.show()

    sys.exit(app.exec_())