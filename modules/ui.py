# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from random import randint
from PIL import Image, ImageColor
from PyQt5.QtWidgets import (QWidget, QSlider,
    QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

hex_color = "{:06x}".format(randint(0, 0xFFFFFF))
hex_new = hex_color
rgb_gen = f"#{hex_color}"
h = hex_new
rgb = ImageColor.getrgb(f"{rgb_gen}")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        icon = QtGui.QIcon('modules/images/logo.png')
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 120, 81, 21))
        self.label_4.setObjectName("label_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(60, 40, 104, 31))
        self.plainTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.plainTextEdit.setLineWidth(0)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(60, 80, 104, 31))
        self.plainTextEdit_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.plainTextEdit_2.setLineWidth(0)
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 227, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.labels = QtWidgets.QLabel(MainWindow)
        self.labels.setPixmap(QPixmap('modules/images/rectangle.png'))
        self.labels.setGeometry(60, 100, 200, 200)
        MainWindow.resize(227, 295)

        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Colour Generator"))
        self.label_4.setText(_translate("MainWindow", "Colour:"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", f"{hex_color}"))
        self.plainTextEdit_2.setPlainText(_translate("MainWindow", f"{rgb}"))