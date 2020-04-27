import datetime
from stopwatch import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QApplication
import sys


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.timer = QtCore.QTimer(self)
        # print(QtCore.QTimer.timerType(QtCore.QTimer(self)))
        # self.timer.setTimerType(4)
        self.timer.timeout.connect(self.run_watch)
        self.timer.setInterval(1)
        self.mscounter = 0
        self.isreset = True
        self.ui.pushButtonStart.clicked.connect(self.start_watch)
        self.ui.pushButtonStop.clicked.connect(self.stop_watch)
        self.ui.pushButtonPause.clicked.connect(self.watch_pause)
        self.ui.pushButtonReset.clicked.connect(self.watch_reset)
        # self.show()
        self.showLCD()

    def showLCD(self):
        text = str(datetime.timedelta(milliseconds=self.mscounter))[:-3]
        # print(text)
        self.ui.lcdNumber.setDigitCount(11)
        if not self.isreset:  # if "isreset" is False
            self.ui.lcdNumber.display(text)
        else:
            self.ui.lcdNumber.display('0:00:00.000')

    def run_watch(self):
        self.mscounter += 1
        self.showLCD()

    def start_watch(self):
        self.timer.start()
        self.isreset = False
        self.ui.pushButtonReset.setDisabled(True)
        self.ui.pushButtonStart.setDisabled(True)
        self.ui.pushButtonStop.setDisabled(False)
        self.ui.pushButtonPause.setDisabled(False)

    def stop_watch(self):
        self.timer.stop()
        # self.mark_time()
        self.mscounter = 0

        self.ui.pushButtonReset.setDisabled(False)
        self.ui.pushButtonStart.setDisabled(False)
        self.ui.pushButtonStop.setDisabled(True)
        self.ui.pushButtonPause.setDisabled(True)

    def watch_pause(self):
        self.timer.stop()

        self.ui.pushButtonReset.setDisabled(False)
        self.ui.pushButtonStart.setDisabled(False)
        self.ui.pushButtonStop.setDisabled(True)
        self.ui.pushButtonPause.setDisabled(True)

    def watch_reset(self):
        self.timer.stop()
        self.mscounter = 0
        self.isreset = True
        self.showLCD()

        self.ui.pushButtonReset.setDisabled(True)
        self.ui.pushButtonStart.setDisabled(False)
        self.ui.pushButtonStop.setDisabled(True)
        self.ui.pushButtonPause.setDisabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
