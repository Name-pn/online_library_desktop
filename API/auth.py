from requests.auth import AuthBase


class TokenAuth(AuthBase):
    """Класс аутентификации по токену, небходимый для выполнения запросов требующих аутентификацию"""

    def __init__(self, token: str):
        self.__token = token

    def __call__(self, request):
        request.headers['authorization'] = f"Token {self.__token}"
        return request
