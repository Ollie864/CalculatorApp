
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class MainWindow(QMainWindow):

    tempNums = []
    resultField = ""
    finNums = 0
    storedAnswer = ""
    degreeToggle = True

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("ui/main.ui", self)
        self.show()

        self.actionQuit.triggered.connect(exit)

        self.buttonDot.clicked.connect(lambda: self.numPress("."))
        self.button0.clicked.connect(lambda: self.numPress("0"))
        self.button1.clicked.connect(lambda: self.numPress("1"))
        self.button2.clicked.connect(lambda: self.numPress("2"))
        self.button3.clicked.connect(lambda: self.numPress("3"))
        self.button4.clicked.connect(lambda: self.numPress("4"))
        self.button5.clicked.connect(lambda: self.numPress("5"))
        self.button6.clicked.connect(lambda: self.numPress("6"))
        self.button7.clicked.connect(lambda: self.numPress("7"))
        self.button8.clicked.connect(lambda: self.numPress("8"))
        self.button9.clicked.connect(lambda: self.numPress("9"))

        self.buttonDiv.clicked.connect(lambda: self.funcPres("/"))
        self.buttonTimes.clicked.connect(lambda: self.funcPres("*"))
        self.buttonAdd.clicked.connect(lambda: self.funcPres("+"))
        self.buttonMinus.clicked.connect(lambda: self.funcPres("-"))

        self.buttonClear.clicked.connect(self.clear)
        self.buttonCE.clicked.connect(self.clearEntry)

        self.buttonToggle.clicked.connect(self.toggle)

    def toggle(self):
        self.degreeToggle = not self.degreeToggle
        if self.degreeToggle:
            self.buttonToggle.setText("Degrees")
        elif not self.degreeToggle:
            self.buttonToggle.setText("Radians")

    def funcPres(self, n):
        self.tempNums.append(n)
        self.update()

    def clearEntry(self):
        try:
            del self.tempNums[-1]
        except:
            pass
        self.update()

    def clear(self):
        self.tempNums.clear()
        self.update()

    def update(self):
        s = "".join(self.tempNums)
        self.lineEdit.setText(s)

    def numPress(self, n: str):
        if n in ["sin(", "cos(", "tan("]:
            if self.degreeToggle:
                self.tempNums.append(n + "°(")
                # )
            if not self.degreeToggle:
                self.tempNums.append(n)
                # )
        else:
            self.tempNums.append(n)

        self.update()


app = QApplication([])
widget = QtWidgets.QStackedWidget()

mainWindow = MainWindow()
widget.addWidget(mainWindow)

widget.setWindowTitle("Calculator")
widget.setFixedHeight(750)
widget.setMaximumWidth(1400)

widget.show()
app.exec_()
