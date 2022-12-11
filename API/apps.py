from typing import List

import requests

from API.auth import TokenAuth
from API.config import API_ROOT
from API.core import App, GetAllMixin, GetDetailMixin, get_data_from_request
from API.store import Store


class Authors(App, GetAllMixin, GetDetailMixin):
    """
    Реализует взаимодействие с приложением authors.
    Ключевое поле - slug.
    """

    root_url = API_ROOT + 'authors/'

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

    root_url = API_ROOT + 'books/'

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

    root_url = API_ROOT + 'genres/'

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
    root_url = API_ROOT + 'auth/token/'

    @classmethod
    def login(cls, login: str, password: str) -> None:
        """
        :param login: имя пользователя.
        :param password: пароль.
        :return выполняет аутентификацию пользователя, в случае успеха ничего не возвращает.
        :raise в случае неудачи возбуждает исключение HTTPError
        """

        response_data = get_data_from_request(cls.root_url + 'login/', 'POST', data={
            'username': login, 'password': password,
        }, with_exception=True)

        Store.data()['token'] = response_data['auth_token']

    @classmethod
    def logout(cls) -> None:
        """
        Выполняет выход пользователя из системы.
        :return: В случае успеха ничего не возвращает.
        :raise В случае неудачи возбуждает исключение HTTPError.
        """

        # Используем request напрямую, так как запрос по этому эндпоинту не возвращает данные
        response = requests.post(cls.root_url + 'logout/', auth=cls.get_token())
        response.raise_for_status()

        Store.data()['token'] = None

    @staticmethod
    def get_token() -> TokenAuth:
        """Возращает класс аутентификации пользователя по токену."""

        return TokenAuth(Store.data().get('token'))


class Users(App):
    root_url = API_ROOT + 'users/'

    @classmethod
    def current(cls) -> dict:
        """
        :return: данные пользователя в случае, если он залогинен, иначе возбуждает исключение HTTPError
        :raise: HTTPError
        """

        return get_data_from_request(
            cls.root_url + 'me/', 'GET', with_exception=True, auth=Auth.get_token()
        )
