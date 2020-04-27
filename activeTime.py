# from __future__ import print_function
# import time
# from os import system
# from activity import *
# import json
# import datetime
# import sys
#
# if sys.platform in ['Windows', 'win32', 'cygwin']:
#     import win32gui
#     import uiautomation as auto
# elif sys.platform in ['Mac', 'darwin', 'os2', 'os2emx']:
#     from AppKit import NSWorkspace
#     from Foundation import *
# elif sys.platform in ['linux', 'linux2']:
#     import linux as l
#
# active_window_name = ""
# activity_name = ""
# start_time = datetime.datetime.now()
# activeList = AcitivyList([])
# first_time = True
#
#
# def url_to_name(url):
#     string_list = url.split('/')
#     return string_list[2]
#
#
# def get_active_window():
#     _active_window_name = None
#     if sys.platform in ['Windows', 'win32', 'cygwin']:
#         window = win32gui.GetForegroundWindow()
#         _active_window_name = win32gui.GetWindowText(window)
#     elif sys.platform in ['Mac', 'darwin', 'os2', 'os2emx']:
#         _active_window_name = (NSWorkspace.sharedWorkspace()
#             .activeApplication()['NSApplicationName'])
#     else:
#         print("sys.platform={platform} is not supported."
#               .format(platform=sys.platform))
#         print(sys.version)
#     return _active_window_name
#
#
# def get_chrome_url():
#     if sys.platform in ['Windows', 'win32', 'cygwin']:
#         window = win32gui.GetForegroundWindow()
#         chromeControl = auto.ControlFromHandle(window)
#         edit = chromeControl.EditControl()
#         return 'https://' + edit.GetValuePattern().Value
#     elif sys.platform in ['Mac', 'darwin', 'os2', 'os2emx']:
#         textOfMyScript = """tell app "google chrome" to get the url of the active tab of window 1"""
#         s = NSAppleScript.initWithSource_(
#             NSAppleScript.alloc(), textOfMyScript)
#         results, err = s.executeAndReturnError_(None)
#         return results.stringValue()
#     else:
#         print("sys.platform={platform} is not supported."
#               .format(platform=sys.platform))
#         print(sys.version)
#     return _active_window_name
#
#
# try:
#     activeList.initialize_me()
# except Exception:
#     print('No json')
#
# try:
#     while True:
#         previous_site = ""
#         if sys.platform not in ['linux', 'linux2']:
#             new_window_name = get_active_window()
#             if 'Google Chrome' in new_window_name:
#                 new_window_name = url_to_name(get_chrome_url())
#         if sys.platform in ['linux', 'linux2']:
#             new_window_name = l.get_active_window_x()
#             if 'Google Chrome' in new_window_name:
#                 new_window_name = l.get_chrome_url_x()
#
#         if active_window_name != new_window_name:
#             print(active_window_name)
#             activity_name = active_window_name
#
#             if not first_time:
#                 end_time = datetime.datetime.now()
#                 time_entry = TimeEntry(start_time, end_time, 0, 0, 0, 0)
#                 time_entry._get_specific_times()
#
#                 exists = False
#                 for activity in activeList.activities:
#                     if activity.name == activity_name:
#                         exists = True
#                         activity.time_entries.append(time_entry)
#
#                 if not exists:
#                     activity = Activity(activity_name, [time_entry])
#                     activeList.activities.append(activity)
#                 with open('activities.json', 'w') as json_file:
#                     json.dump(activeList.serialize(), json_file,
#                               indent=4, sort_keys=True)
#                     start_time = datetime.datetime.now()
#             first_time = False
#             active_window_name = new_window_name
#
#         time.sleep(1)
#
# except KeyboardInterrupt:
#     with open('activities.json', 'w') as json_file:
#         json.dump(activeList.serialize(), json_file, indent=4, sort_keys=True)


import sys
from pathlib import Path

import pandas as pd
import datetime
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize,QTimer
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QPlainTextEdit, QFileDialog, QLabel, QMessageBox, \
    QGridLayout, QGroupBox, QVBoxLayout, QCheckBox, QScrollArea, QProgressBar, QApplication, QLCDNumber, QDialog
from PyQt5.uic.properties import QtCore
from self import self
import os

from stopwatch import Ui_Dialog


class activeTime:

    class TutorialFirstInterface(QtWidgets.QMainWindow):

        def __init__(self):
            QWidget.__init__(self)
            self.setFixedSize(800, 680)
            self.setWindowTitle('دفـة')
            oImage = QImage('pic/logo.png')
            sImage = oImage.scaled(QSize(790, 618))    # resize Image to widgets size
            palette = QPalette()
            palette.setBrush(10, QBrush(sImage))      # 10 = Windowrole
            self.setPalette(palette)

            # define signupButton
            signupButton = QPushButton('', self)
            # set image to signupButton
            icon = QIcon()
            icon.addPixmap(QPixmap('pic/signup.png'))
            signupButton.setIcon(icon)
            signupButton.setStyleSheet("background-color: white")
            signupButton.setStyleSheet("border: none")
            signupButton.resize(200, 78)
            signupButton.setIconSize(QSize(250, 190))
            # set signupButton position
            signupButton.move(100, 550)

            # define loginButton
            loginButton = QPushButton('', self)
            # set image to loginButton
            icon = QIcon()
            icon.addPixmap(QPixmap('pic/login.png'))
            loginButton.setIcon(icon)
            loginButton.setStyleSheet("background-color: white")
            loginButton.setStyleSheet("border: none")
            loginButton.resize(200, 78)
            loginButton.setIconSize(QSize(250, 190))
            # set loginButton position
            loginButton.move(500, 550)

            self.signupInterface = activeTime.signupInterface()
            self.loginInterface = activeTime.loginInterface()
            loginButton.clicked.connect(self.login)
            signupButton.clicked.connect(self.signup)

        # go to next tutorial interface
        def login(self):
            if self.loginInterface.isHidden():
                self.loginInterface.show()
                self.window().hide()
            else:
                self.loginInterface.hide()

        # skip the tutorial
        def signup(self):
            if self.signupInterface.isHidden():
                self.signupInterface.show()
                self.window().hide()
            else:
                self.signupInterface.hide()

    class loginInterface(QtWidgets.QMainWindow):

        def __init__(self):
            QWidget.__init__(self)
            self.setFixedSize(800, 680)
            self.setWindowTitle('دفة')
            self.setStyleSheet("background-color: white")
            # self.text = text

            logoLabel = QLabel(self)
            pixmap = QPixmap("pic/logo_vsmall.png")
            pixmap.scaled(20, 10)
            logoLabel.setPixmap(pixmap)
            logoLabel.resize(300, 150)

            emailLabel = QLabel(self)
            pixmap = QPixmap("pic/email.png")
            pixmap.scaled(20, 10)
            emailLabel.setPixmap(pixmap)
            emailLabel.resize(300, 150)
            emailLabel.move(320,100)

            # Add text field
            self.email = QPlainTextEdit(self)
            self.email.setStyleSheet("background:white; border:1px solid rgb(161,192,229)")
            # self.textToDetect.setPlainText(self.text)
            self.email.move(275, 200)
            self.email.resize(250, 30)

            passLabel = QLabel(self)
            pixmap = QPixmap("pic/pass.png")
            pixmap.scaled(20, 10)
            passLabel.setPixmap(pixmap)
            passLabel.resize(300, 150)
            passLabel.move(340,240)

            # Add text field
            self.password = QPlainTextEdit(self)
            self.password.setStyleSheet("background:white; border:1px solid rgb(161,192,229)")
            # self.textToDetect.setPlainText(self.text)
            self.password.move(275, 335)
            self.password.resize(250, 30)

            # # define skipButton
            # skipButton = QPushButton('', self)
            # # set image to skipButton
            # icon = QIcon()
            # icon.addPixmap(QPixmap('pic/skip.png'))
            # skipButton.setIcon(icon)
            # skipButton.setStyleSheet("background-color: white")
            # skipButton.setStyleSheet("border: none")
            # skipButton.resize(200, 78)
            # skipButton.setIconSize(QSize(250, 190))
            # # set skipButton position
            # skipButton.move(100, 550)

            # define nextButton
            loginButton2 = QPushButton('', self)
            # set image to nextButton
            icon = QIcon()
            icon.addPixmap(QPixmap('pic/login.png'))
            loginButton2.setIcon(icon)
            loginButton2.setStyleSheet("background-color: white")
            loginButton2.setStyleSheet("border: none")
            loginButton2.resize(200, 78)
            loginButton2.setIconSize(QSize(250, 190))
            # set nextButton position
            loginButton2.move(317, 550)

            # self.first_interface = activeTime.signupInterface()
            self.homeInterface = activeTime.homeInterface()
            loginButton2.clicked.connect(self.next)
            # skipButton.clicked.connect(self.skip)

        def next(self):
            if self.homeInterface.isHidden():
                self.homeInterface.show()
                self.window().hide()
            else:
                self.homeInterface.hide()

        # def skip(self):
        #     if self.first_interface.isHidden():
        #         self.first_interface.show()
        #         self.window().hide()
        #     else:
        #         self.first_interface.hide()

    class homeInterface(QtWidgets.QMainWindow):

        def __init__(self):
            QWidget.__init__(self)
            self.setFixedSize(800, 680)
            self.setWindowTitle('دفة')
            self.setStyleSheet("background-color: white")

            logoLabel = QLabel(self)
            pixmap = QPixmap("pic/logo_vsmall.png")
            pixmap.scaled(15, 10)
            logoLabel.setPixmap(pixmap)
            logoLabel.resize(250, 150)

            userLabel = QLabel(self)
            pixmap = QPixmap("pic/user1.png")
            pixmap.scaled(15, 10)
            userLabel.setPixmap(pixmap)
            userLabel.resize(250, 150)
            userLabel.move(570,0)

            # define startButton
            startButton = QPushButton('', self)
            # set image to startButton
            icon = QIcon()
            icon.addPixmap(QPixmap('pic/start.png'))
            startButton.setIcon(icon)
            startButton.setStyleSheet("background-color: white")
            startButton.setStyleSheet("border: none")
            startButton.resize(226, 200)
            startButton.setIconSize(QSize(250, 190))
            # set startButton position
            startButton.move(100, 300)

            # define dashboardButton
            dashboardButton = QPushButton('', self)
            # set image to dashboardButton
            icon = QIcon()
            icon.addPixmap(QPixmap('pic/dashboard.png'))
            dashboardButton.setIcon(icon)
            dashboardButton.setStyleSheet("background-color: white")
            dashboardButton.setStyleSheet("border: none")
            dashboardButton.resize(226, 200)
            dashboardButton.setIconSize(QSize(250, 190))
            # set nextButton position
            dashboardButton.move(500, 300)

            self.timerInterface = activeTime.timerInterface()
            self.dashboardInterface = activeTime.dashboardInterface()
            startButton.clicked.connect(self.next)
            dashboardButton.clicked.connect(self.nextDashboard)

        def next(self):
            if self.timerInterface.isHidden():
                self.timerInterface.show()
                self.window().hide()
            else:
                self.timerInterface.hide()

        def nextDashboard(self):
            if self.dashboardInterface.isHidden():
                self.dashboardInterface.show()
                self.window().hide()
            else:
                self.dashboardInterface.hide()

    class signupInterface(QtWidgets.QMainWindow):

        def __init__(self):
            QWidget.__init__(self)
            self.setFixedSize(800, 680)
            self.setWindowTitle('دفة')
            self.setStyleSheet("background-color: white")
            # self.text = text

            logoLabel = QLabel(self)
            pixmap = QPixmap("pic/logo_vsmall.png")
            pixmap.scaled(20, 10)
            logoLabel.setPixmap(pixmap)
            logoLabel.resize(300, 150)

            namelLabel = QLabel(self)
            pixmap = QPixmap("pic/name.png")
            pixmap.scaled(20, 10)
            namelLabel.setPixmap(pixmap)
            namelLabel.resize(300, 150)
            namelLabel.move(565, 135)

            # Add text field
            self.name = QPlainTextEdit(self)
            self.name.setStyleSheet("background:white; border:1px solid rgb(161,192,229)")
            # self.textToDetect.setPlainText(self.text)
            self.name.move(500, 250)
            self.name.resize(250, 30)

            jobnamelLabel = QLabel(self)
            pixmap = QPixmap("pic/jobName.png")
            pixmap.scaled(20, 10)
            jobnamelLabel.setPixmap(pixmap)
            jobnamelLabel.resize(300, 150)
            jobnamelLabel.move(150, 135)

            # Add text field
            self.jobnamelLabel = QPlainTextEdit(self)
            self.jobnamelLabel.setStyleSheet("background:white; border:1px solid rgb(161,192,229)")
            # self.textToDetect.setPlainText(self.text)
            self.jobnamelLabel.move(50, 250)
            self.jobnamelLabel.resize(250, 30)

            emailLabel = QLabel(self)
            pixmap = QPixmap("pic/email.png")
            pixmap.scaled(20, 10)
            emailLabel.setPixmap(pixmap)
            emailLabel.resize(300, 150)
            emailLabel.move(555,300)

            # Add text field
            self.email = QPlainTextEdit(self)
            self.email.setStyleSheet("background:white; border:1px solid rgb(161,192,229)")
            # self.textToDetect.setPlainText(self.text)
            self.email.move(500, 400)
            self.email.resize(250, 30)

            passLabel = QLabel(self)
            pixmap = QPixmap("pic/pass.png")
            pixmap.scaled(20, 10)
            passLabel.setPixmap(pixmap)
            passLabel.resize(300, 150)
            passLabel.move(130,300)

            # Add text field
            self.password = QPlainTextEdit(self)
            self.password.setStyleSheet("background:white; border:1px solid rgb(161,192,229)")
            # self.textToDetect.setPlainText(self.text)
            self.password.move(50, 400)
            self.password.resize(250, 30)

            # define nextButton
            signupButton = QPushButton('', self)
            # set image to nextButton
            icon = QIcon()
            icon.addPixmap(QPixmap('pic/signup.png'))
            signupButton.setIcon(icon)
            signupButton.setStyleSheet("background-color: white")
            signupButton.setStyleSheet("border: none")
            signupButton.resize(200, 78)
            signupButton.setIconSize(QSize(250, 190))
            # set nextButton position
            signupButton.move(300, 550)

            # self.first_interface = activeTime.signupInterface()
            self.homeInterface = activeTime.homeInterface()
            signupButton.clicked.connect(self.next)
            # skipButton.clicked.connect(self.skip)

        def next(self):
            if self.homeInterface.isHidden():
                self.homeInterface.show()
                self.window().hide()
            else:
                self.homeInterface.hide()

    class SecondInterface(QtWidgets.QMainWindow):

        def __init__(self, text):
            QWidget.__init__(self)
            self.setFixedSize(800, 680)
            self.setWindowTitle('دفة')
            self.setStyleSheet("background:rgb(249,249,242)")
            # self.text = text

            logoLabel = QLabel(self)
            pixmap = QPixmap("pic/logo_vsmall.png")
            pixmap.scaled(15, 10)
            logoLabel.setPixmap(pixmap)
            logoLabel.resize(250, 150)

            # Add text field
            self.textToDetect = QPlainTextEdit(self)
            self.textToDetect.setStyleSheet("background:white; border:1px solid rgb(161,192,229)")
            # self.textToDetect.setPlainText(self.text)
            self.textToDetect.move(47, 155)
            self.textToDetect.resize(700, 400)

    class timerInterface(QDialog):

        def __init__(self):
            QWidget.__init__(self)
            self.setFixedSize(800, 680)
            self.setWindowTitle('دفة')
            self.setStyleSheet("background-color: white")
            icon = "pic/logo_vsmall.png"
            self.setWindowIcon(QIcon(icon))

            logoLabel = QLabel(self)
            pixmap = QPixmap("pic/logo_vsmall.png")
            pixmap.scaled(15, 10)
            logoLabel.setPixmap(pixmap)
            logoLabel.resize(250, 150)

            userLabel = QLabel(self)
            pixmap = QPixmap("pic/user1.png")
            pixmap.scaled(15, 10)
            userLabel.setPixmap(pixmap)
            userLabel.resize(250, 150)
            userLabel.move(570,0)

            # define startButton
            startButton = QPushButton('', self)
            # set image to nextButton
            icon = QIcon()
            icon.addPixmap(QPixmap('pic/startTimer.png'))
            startButton.setIcon(icon)
            startButton.setStyleSheet("background-color: white")
            startButton.setStyleSheet("border: none")
            startButton.resize(200, 78)
            startButton.setIconSize(QSize(250, 190))
            # set nextButton position
            startButton.move(50, 400)

            # define pauseButton
            pauseButton = QPushButton('', self)
            # set image to pauseButton
            icon = QIcon()
            icon.addPixmap(QPixmap('pic/pause.png'))
            pauseButton.setIcon(icon)
            pauseButton.setStyleSheet("background-color: white")
            pauseButton.setStyleSheet("border: none")
            pauseButton.resize(200, 78)
            pauseButton.setIconSize(QSize(250, 190))
            # set pauseButton position
            pauseButton.move(310, 400)

            # define stopButton
            stopButton = QPushButton('', self)
            # set image to stopButton
            icon = QIcon()
            icon.addPixmap(QPixmap('pic/stopTimer.png'))
            stopButton.setIcon(icon)
            stopButton.setStyleSheet("background-color: white")
            stopButton.setStyleSheet("border: none")
            stopButton.resize(200, 78)
            stopButton.setIconSize(QSize(250, 190))
            # set stopButton position
            stopButton.move(540, 400)

            # define homeButton
            homeButton = QPushButton('', self)
            # set image to homeButton
            icon = QIcon()
            icon.addPixmap(QPixmap('pic/home.png'))
            homeButton.setIcon(icon)
            homeButton.setStyleSheet("background-color: white")
            homeButton.setStyleSheet("border: none")
            homeButton.resize(200, 78)
            homeButton.setIconSize(QSize(250, 190))
            # set homeButton position
            homeButton.move(637, 120)

            homeButton.clicked.connect(self.home)
            # skipButton.clicked.connect(self.skip)

        def home(self):
            self.homeInterface = activeTime.homeInterface()
            if self.homeInterface.isHidden():
                self.homeInterface.show()
                self.window().hide()
            else:
                self.homeInterface.hide()

    class dashboardInterface (QtWidgets.QMainWindow):
        def __init__(self):
            QWidget.__init__(self)
            self.setFixedSize(800, 680)
            self.setWindowTitle('دفة')
            self.setStyleSheet("background-color: white")

            logoLabel = QLabel(self)
            pixmap = QPixmap("pic/logo_vsmall.png")
            pixmap.scaled(15, 10)
            logoLabel.setPixmap(pixmap)
            logoLabel.resize(250, 150)

            userLabel = QLabel(self)
            pixmap = QPixmap("pic/user1.png")
            pixmap.scaled(15, 10)
            userLabel.setPixmap(pixmap)
            userLabel.resize(250, 150)
            userLabel.move(570,0)

            # define homeButton
            homeButton = QPushButton('', self)
            # set image to homeButton
            icon = QIcon()
            icon.addPixmap(QPixmap('pic/home.png'))
            homeButton.setIcon(icon)
            homeButton.setStyleSheet("background-color: white")
            homeButton.setStyleSheet("border: none")
            homeButton.resize(200, 78)
            homeButton.setIconSize(QSize(250, 190))
            # set homeButton position
            homeButton.move(637, 120)

            homeButton.clicked.connect(self.home)
            # skipButton.clicked.connect(self.skip)

        def home(self):
            self.homeInterface = activeTime.homeInterface()
            if self.homeInterface.isHidden():
                self.homeInterface.show()
                self.window().hide()
            else:
                self.homeInterface.hide()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = activeTime.TutorialFirstInterface()
    gui.show()
    app.exec_()