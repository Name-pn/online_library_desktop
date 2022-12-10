import PyQt5.QtWidgets
import PyQt5.QtGui
import PyQt5.QtCore
import additionWidgets.VLine
import additionWidgets.UserComponent
import additionWidgets.EnterComponent
import additionWidgets.RefComponent
import additionWidgets.Plug

class TopComponent(PyQt5.QtWidgets.QWidget):
    def __init__(self, UserComponent, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.comp = UserComponent
        self.hl = PyQt5.QtWidgets.QHBoxLayout(self)
        self.spacer = PyQt5.QtWidgets.QSpacerItem(0, 0)
        self.spacer2 = PyQt5.QtWidgets.QSpacerItem(0, 0)
        self.refC = additionWidgets.RefComponent.RefComponent()

        self.initUI()

    def paintEvent(self, a0: PyQt5.QtGui.QPaintEvent):
        painter = PyQt5.QtGui.QPainter(self)
        brush = PyQt5.QtGui.QBrush(PyQt5.QtCore.Qt.gray)
        painter.setBrush(brush)
        painter.drawRect(0, 0, self.width(), self.height())

    def initUI(self):
        self.setMaximumHeight(75)
        self.hl.setAlignment(PyQt5.QtCore.Qt.AlignLeft)
        self.hl.addWidget(self.comp)
        self.hl.addSpacerItem(self.spacer)
        self.hl.addWidget(self.refC)
        self.hl.addSpacerItem(self.spacer2)


