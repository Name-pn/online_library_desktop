import os
import pickle

from API.config import STORE_CACHE_FILE

class Store:
    """
    Хранилище. Представляет собой класс-одиночку, не требует явного инстацирования, оно выполняется автоматически.
    Доступ к данным реализуется с помощью статического метода data.
    При инициализации хранилища создается файл, куда сбрасываются данные при его удалении, если такой файл уже
    существует, то данные из него загружаются в хранилище.
    """

    @staticmethod
    def data() -> dict:
        """Возвращает данные хранилища в виде словаря"""

        return Store.__get_instance().__data

    __instance = None

    @classmethod
    def __get_instance(cls) -> 'Store':
        if cls.__instance is None:
            cls.__instance = Store()

        return cls.__instance

    def __init__(self):
        self.__data = {}

        if os.path.exists(STORE_CACHE_FILE):
            with open(STORE_CACHE_FILE, 'rb') as file:
                self.__data = pickle.load(file)

        #self.file = open(STORE_CACHE_FILE, 'wb')

    def __del__(self):
        pass
        #pickle.dump(self.__data, self.file)
        #self.file.close()

