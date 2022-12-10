import PyQt5.QtWidgets
import PyQt5.QtGui
import PyQt5.QtCore
from PyQt5.QtNetwork import QNetworkAccessManager

import additionWidgets.UserComponent
import additionWidgets.EnterComponent
import additionWidgets.TopComponent
import forms.EntryForm
import forms.BookList
import ListElements.BookElement
import sys

from pprint import pprint
from API.apps import Books, Authors, Genres
from ListElements.BookElement import BookElement

if __name__ != '__main__':
    books = Books.get_all()
    pprint(books)

if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
#    QNetworkAccessManager
# additionWidgets.VLine.VLine(100)
    compComp = additionWidgets.UserComponent.UserComponent()
    comp = additionWidgets.TopComponent.TopComponent(compComp)
    w2 = forms.BookList.BookList(comp)

    #w2.resize(250, 150)
    #w2.move(300, 300)
    w2.setWindowTitle('Desktop library')
    icon = PyQt5.QtGui.QIcon('./images/lib.png')
    w2.setWindowIcon(icon)
    w2.show()

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