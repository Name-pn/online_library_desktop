from API.apps import Genres, Books, Authors


class Constrains():

    def __init__(self):
        self.table = {}
        self.prop = Authors.get_all()
        for el in self.prop:
            self.table[el['name'] + ' ' + el['surname']] = el['slug']
        self.genres = Genres.get_all()
        self.books = Books.get_all()


DEFAULT_CONSTRAINS = Constrains()