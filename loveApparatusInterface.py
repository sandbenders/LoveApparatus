# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loveApparatusInterface.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(80, 80, 581, 51))
        self.title.setStyleSheet("color: rgb(247, 169, 65);\n"
"font: 50pt \"Alternate Gothic No2 D\";\n"
"")
        self.title.setObjectName("title")
        self.info = QtWidgets.QLabel(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(80, 960, 611, 31))
        self.info.setStyleSheet("color: rgb(130, 150, 180);\n"
"font: 25pt \"Alternate Gothic No2 D\";\n"
"")
        self.info.setObjectName("info")
        self.mainText = QtWidgets.QTextEdit(self.centralwidget)
        self.mainText.setGeometry(QtCore.QRect(80, 240, 1760, 631))
        self.mainText.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.mainText.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 100pt \"AlternateGotNo3D\";")
        self.mainText.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mainText.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mainText.setReadOnly(True)
        self.mainText.setObjectName("mainText")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "#LoveApparatus"))
        self.title.setText(_translate("MainWindow", "#LoveApparatus"))
        self.info.setText(_translate("MainWindow", "tweet using the hashtag #LoveApparatus"))
        self.mainText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'AlternateGotNo3D\'; font-size:100pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

