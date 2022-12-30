import PyQt6.QtGui

from API.apps import Genres, Books, Authors


class Constrains():

    def __init__(self):
        self.table = {}
        self.prop = Authors.get_all()
        for el in self.prop:
            self.table[el['name'] + ' ' + el['surname']] = el['slug']
        self.genres = Genres.get_all()
        self.books = Books.get_all()
        self.titleFont = PyQt6.QtGui.QFont('Georgia', 20)
        self.titleBoldFont = PyQt6.QtGui.QFont('Georgia', 20)
        self.titleBoldFont.setBold(True)
        self.mainFont = PyQt6.QtGui.QFont('Georgia', 16)
        self.supFont = PyQt6.QtGui.QFont('Georgia', 14)
        self.buttonsFont = PyQt6.QtGui.QFont('Helvetica', 12)


DEFAULT_CONSTRAINS = Constrains()