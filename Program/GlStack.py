from PyQt5 import QtWidgets

class GlobalStack:
    STACK = None

    @classmethod
    def init(cls):
        cls.STACK = QtWidgets.QStackedWidget()

    @classmethod
    def get_instance(cls):
        if cls.STACK is None:
            raise Exception('Windows is\'nt init')
        return cls.STACK
