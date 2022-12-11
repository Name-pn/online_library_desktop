from typing import List

from requests import HTTPError

from API import config
from API.core import App, GetAllMixin, GetDetailMixin, get_data_from_request


class Authors(App, GetAllMixin, GetDetailMixin):
    """
    Реализует взаимодействие с приложением authors.
    Ключевое поле - slug.
    """

    root_url = config.API_ROOT + 'authors/'

    @classmethod
    def get_books(cls, author_slug: str) -> List[dict]:
        """
        :param author_slug: слаг, по которому выполняется поиск автора.
        :return: возращает список всех книг автора.
        """
        return get_data_from_request(cls.root_url + f'{author_slug}/books', 'GET')


class Books(App, GetAllMixin, GetDetailMixin):
    """
    Реализует взаимодействие с приложением books.
    Ключевое поле - slug.
    """

    root_url = config.API_ROOT + 'books/'

    @classmethod
    def get_comments(cls, book_slug: str) -> List[dict]:
        """
        :param book_slug: слаг, по которому выполняется поиск книги.
        :return: возращает список всех комментариев к книге
        """
        return get_data_from_request(cls.root_url + f'{book_slug}/comments', 'GET')


class Genres(App, GetAllMixin, GetDetailMixin):
    """
    Реализует взаимодействие с приложением genres.
    Ключевое поле - slug.
    """

    root_url = config.API_ROOT + 'genres/'

    @classmethod
    def get_authors(cls, genre_slug: str) -> List[dict]:
        """
        :param genre_slug: слаг, по которому выполняется поиск жанра.
        :return: возращает список всех авторов, работающих в жанре.
        """
        return get_data_from_request(cls.root_url + f'{genre_slug}/authors', 'GET')

    @classmethod
    def get_books(cls, genre_slug: str) -> List[dict]:
        """
        :param genre_slug: слаг, по которому выполняется поиск жанра.
        :return: возращает список всех книг жанра.
        """
        return get_data_from_request(cls.root_url + f'{genre_slug}/books', 'GET')


class Auth(App):
    root_url = config.API_ROOT + 'auth/token/'

    @classmethod
    def login(cls, login: str, password: str) -> bool:
        try:
            token = get_data_from_request(cls.root_url + '/login', 'POST', data={
                'username': login, 'password': password,
            }, with_exception=True)

            # Добавить в store

            return True

        except HTTPError:
            return False
