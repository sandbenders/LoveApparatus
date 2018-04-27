# pyuic5 loveApparatusInterface.ui -o ../loveApparatusInterface.py

import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer

from Database import *
from loveApparatusInterface import Ui_MainWindow

MAIN_TEXT_FORMAT = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\"><html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">p, li { white-space: pre-wrap; }</style></head><body style=\" font-family:\'AlternateGotNo3D\'; font-size:95pt; font-weight:400; font-style:normal;\"><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:80%;\">MESSAGE</p></body></html>"
INTERVAL_SENTENCES = 1000

# loop - it is here to do not get garbage collected!!!
timer = QTimer()


class Window(Ui_MainWindow):
    def __init__(self, window):
        Ui_MainWindow.__init__(self)

        # config the window
        self.setupUi(window)

        # database
        self.database = Database()

        # first sentence
        self.love_sentences()

        # loop
        timer.timeout.connect(self.love_sentences)
        timer.start(30000)

    def love_sentences(self):
        sentence = self.database.get_love_sentence()
        self.mainText.setHtml(MAIN_TEXT_FORMAT.replace('MESSAGE', sentence))
        print("{} {}".format(sentence, len(sentence)))

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    prog = Window(window)
    window.showFullScreen()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
