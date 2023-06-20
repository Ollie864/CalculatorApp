
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("ui/main.ui", self)
        self.show()


app = QApplication([])
widget = QtWidgets.QStackedWidget()

mainWindow = MainWindow()
widget.addWidget(mainWindow)

widget.show()
app.exec_()