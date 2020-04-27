# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stopwatch.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QLabel, QPushButton


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("دفة")
        Dialog.resize(800, 680)
        Dialog.setStyleSheet("background-color: white")
        logoLabel = QLabel(Dialog)
        pixmap = QPixmap("pic/logo_vsmall.png")
        pixmap.scaled(15, 10)
        logoLabel.setPixmap(pixmap)
        logoLabel.resize(250, 150)

        userLabel = QLabel(Dialog)
        pixmap = QPixmap("pic/user1.png")
        pixmap.scaled(15, 10)
        userLabel.setPixmap(pixmap)
        userLabel.resize(250, 150)
        userLabel.move(570,0)

        # define homeButton
        homeButton = QPushButton('', Dialog)
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

        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(126, 250, 561, 111))
        self.lcdNumber.setObjectName("lcdNumber")

        self.pushButtonStart = QtWidgets.QPushButton(Dialog)
        self.pushButtonStart.setGeometry(QtCore.QRect(50, 430, 89, 25))
        self.pushButtonStart.setObjectName("pushButtonStart")
        icon = QIcon()
        icon.addPixmap(QPixmap('pic/startTimer.png'))
        self.pushButtonStart.setIcon(icon)
        self.pushButtonStart.setStyleSheet("background-color: white")
        self.pushButtonStart.setStyleSheet("border: none")
        self.pushButtonStart.resize(200, 78)
        self.pushButtonStart.setIconSize(QSize(250, 190))


        self.pushButtonStop = QtWidgets.QPushButton(Dialog)
        self.pushButtonStop.setGeometry(QtCore.QRect(540, 430, 89, 25))
        self.pushButtonStop.setObjectName("pushButtonStop")
        icon = QIcon()
        icon.addPixmap(QPixmap('pic/stopTimer.png'))
        self.pushButtonStop.setIcon(icon)
        self.pushButtonStop.setStyleSheet("background-color: white")
        self.pushButtonStop.setStyleSheet("border: none")
        self.pushButtonStop.resize(200, 78)
        self.pushButtonStop.setIconSize(QSize(250, 190))

        self.pushButtonReset = QtWidgets.QPushButton(Dialog)
        self.pushButtonReset.setGeometry(QtCore.QRect(275, 430, 89, 25))
        self.pushButtonReset.setObjectName("pushButtonReset")
        icon = QIcon()
        icon.addPixmap(QPixmap('pic/restartToday.png'))
        self.pushButtonReset.setIcon(icon)
        self.pushButtonReset.setStyleSheet("background-color: white")
        self.pushButtonReset.setStyleSheet("border: none")
        self.pushButtonReset.resize(130, 78)
        self.pushButtonReset.setIconSize(QSize(250, 190))

        self.pushButtonPause = QtWidgets.QPushButton(Dialog)
        self.pushButtonPause.setGeometry(QtCore.QRect(450, 430, 89, 25))
        self.pushButtonPause.setObjectName("pushButtonPause")
        icon = QIcon()
        icon.addPixmap(QPixmap('pic/pause.png'))
        self.pushButtonPause.setIcon(icon)
        self.pushButtonPause.setStyleSheet("background-color: white")
        self.pushButtonPause.setStyleSheet("border: none")
        self.pushButtonPause.resize(100, 78)
        self.pushButtonPause.setIconSize(QSize(200, 190))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "دفة"))
