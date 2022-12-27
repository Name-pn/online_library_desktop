import PyQt6.QtWidgets
import PyQt6.QtGui
import PyQt6.QtCore
import Program.MainWidget
import sys

from pprint import pprint
from API.apps import Books, Authors
from ListElements.BookElement import BookElement

if __name__ == '__main__':
    app = PyQt6.QtWidgets.QApplication(sys.argv)
    w = Program.MainWidget.MainWidget()
    w.show()
    sys.exit(app.exec())
