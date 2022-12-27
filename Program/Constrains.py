import Utilities.TableAuthorSlug
from API.apps import Genres, Books


class Constrains():

    def __init__(self):
        self.table = Utilities.TableAuthorSlug.TableAuthorSlug()
        self.genres = Genres.get_all()
        self.books = Books.get_all()

DEFAULT_CONSTRAINS = Constrains()