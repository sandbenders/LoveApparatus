# pyuic5 loveApparatusInterface.ui -o ../loveApparatusInterface.py

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from loveApparatusInterface import Ui_MainWindow
from Database import *

MAIN_TEXT_FORMAT = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\"><html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">p, li { white-space: pre-wrap; }</style></head><body style=\" font-family:\'AlternateGotNo3D\'; font-size:100pt; font-weight:400; font-style:normal;\"><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:80%;\">MESSAGE</p></body></html>"


class Window(Ui_MainWindow):
    def __init__(self, window):
        Ui_MainWindow.__init__(self)

        # config the window
        self.setupUi(window)

        self.mainText.setHtml(MAIN_TEXT_FORMAT.replace('MESSAGE', 'oi'))

        self.database = Database()
        self.database.get_love_sentence()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    prog = Window(window)
    # window.showFullScreen()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
