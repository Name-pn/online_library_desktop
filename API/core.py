from abc import ABC, abstractmethod
from typing import List, Literal

import requests

from API.config import API_ROOT

Method = Literal['GET', 'OPTIONS', 'HEAD', 'POST', 'PUT', 'PATCH', 'DELETE']

def get_data_from_request(url: str, method: Method, with_exception=False, *args, **kwargs):
    """
    :param url: адрес запроса
    :param method: метод запроса
    :param with_exception: если True, при неудачном запросе возникнет исключение HTTPError
    :return: возвращает данные полученные из запроса
    """

    response = requests.request(method, url, *args, **kwargs)

    if with_exception:
        response.raise_for_status()

    return response.json()


class AbstractApp(ABC):

    @classmethod
    @abstractmethod
    def get_root(cls) -> str:
        pass


class App(AbstractApp):
    root_url = API_ROOT

    @classmethod
    def get_root(cls) -> str:
        return cls.root_url


class GetAllMixin(AbstractApp):
    @classmethod
    def get_all(cls, *args, **kwargs) -> List[dict]:
        return get_data_from_request(cls.get_root(), 'GET', *args, **kwargs)


class GetDetailMixin(AbstractApp):
    @classmethod
    def get_detail(cls, key: str, *args, **kwargs) -> dict:
        return get_data_from_request(cls.get_root() + f'{key}/', 'GET', *args, **kwargs)
