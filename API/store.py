import os
import pickle

from API.config import STORE_CACHE_FILE


class Store:

    @staticmethod
    def get(key: str) -> object or None:
        return Store.__get_instance().data.get(key)

    @staticmethod
    def set(key: str, value) -> None:
        Store.__get_instance().data[key] = value

    @staticmethod
    def delete(key: str):
        del Store.__get_instance().data[key]

    __instance = None

    @classmethod
    def __get_instance(cls) -> 'Store':
        if cls.__instance is None:
            cls.__instance = Store()

        return cls.__instance

    def __init__(self):
        self.data = {}

        if os.path.exists(STORE_CACHE_FILE):
            with open(STORE_CACHE_FILE, 'rb') as file:
                self.data = pickle.load(file)

    def __del__(self):
        with open(STORE_CACHE_FILE, 'wb') as file:
            pickle.dump(self.data, file)
