from enum import IntEnum
from typing import List

import requests
from requests import HTTPError

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


class Comments(App, GetAllMixin):
    """
        Реализует взаимодействие с приложением comments.
        Ключевое поле - book, user, score.
    """

    root_url = API_ROOT + 'comments/'

    @classmethod
    def post_comment(cls, book, score, text):
        response = get_data_from_request(cls.root_url, 'POST', data={'book': book,
                                                                      'text': text,
                                                                      'score': score},
                                         auth=Auth.get_token())

        return response

    @classmethod
    def remove_comment(cls, id):
        response = get_data_from_request(cls.root_url+str(id)+'/', 'DELETE',
                                         auth=Auth.get_token())


    @classmethod
    def get_comments(cls, book = '', user = '', score = ''):
        response = get_data_from_request(cls.root_url, 'GET', params={'book': book,
                                                                  'user': user,
                                                                  'score': score})

        return response

class Books(App, GetAllMixin, GetDetailMixin):
    """
    Реализует взаимодействие с приложением books.
    Ключевое поле - slug.
    """

    root_url = API_ROOT + 'books/'

    @classmethod
    def get_filter(cls, genre = '', author = '', year_of_writing_min = '', year_of_writing_max = ''):
        response = get_data_from_request(API_ROOT + 'books/', 'GET', params={'genres': genre,
                                                                             'author': author,
                                                                             'year_of_writing_min': year_of_writing_min,
                                                                             'year_of_writing_max': year_of_writing_max})

        return response


    @classmethod
    def add_to_bookshelf(cls, slug):
        response = requests.post(API_ROOT + 'readings/', data={'book': slug}, auth=Auth.get_token())
        if response.status_code != 400:
            response.raise_for_status()

    @classmethod
    def remove_from_bookshelf(cls, slug):
        user = Users.current()
        response = get_data_from_request(API_ROOT + 'readings/', 'GET', params={'book': slug, 'user': user['username']}, auth=Auth.get_token())
        get_data_from_request(API_ROOT + 'readings/' + str(response[0]['id']) + '/', 'DELETE', True,  auth=Auth.get_token()),


class Genres(App, GetAllMixin, GetDetailMixin):
    """
    Реализует взаимодействие с приложением genres.
    Ключевое поле - slug.
    """

    root_url = API_ROOT + 'genres/'

class UserTypes(IntEnum):
    GUEST  = 0
    READER = 1
    ADMIN  = 2

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

        current_user = Users.current()
        Store.data()['user'] = int(UserTypes.ADMIN if current_user['is_staff'] else UserTypes.READER)

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
        Store.data()['user'] = None
        Store.data()['token'] = None

    @staticmethod
    def get_token() -> TokenAuth:
        """Возращает класс аутентификации пользователя по токену."""

        return TokenAuth(Store.data().get('token'))


class Users(App):
    root_url = API_ROOT + 'users/'

    @classmethod
    def get_user_type(cls) -> UserTypes:
        type = Store.data().get('user')
        if type is None:
            return UserTypes.GUEST
        return UserTypes(type)

    @classmethod
    def get_my_books(cls) -> [dict]:
        return get_data_from_request(
            cls.root_url + 'me/readings/', 'GET', with_exception=True, auth=Auth.get_token()
        )

    @classmethod
    def current(cls) -> dict:
        """
        :return: данные пользователя в случае, если он залогинен, иначе возбуждает исключение HTTPError
        :raise: HTTPError
        """

        return get_data_from_request(
            cls.root_url + 'me/', 'GET', with_exception=True, auth=Auth.get_token()
        )
