# pyuic5 loveApparatusInterface.ui -o ../loveApparatusInterface.py
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')

import sys
import re

from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer

from Database import *
from IdentifyBadWords import *
from ReplaceWords import *
from loveApparatusInterface import Ui_MainWindow

MAIN_TEXT_FORMAT = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\"><html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">p, li { white-space: pre-wrap; }</style></head><body style=\" font-family:\'AlternateGotNo3D\'; font-size:95pt; font-weight:400; font-style:normal;\"><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:80%;\">MESSAGE</p></body></html>"
INTERVAL_SENTENCES = 30000

# loop - it is here to do not get garbage collected!!!
timer = QTimer()


class Window(Ui_MainWindow):
    def __init__(self, window):
        Ui_MainWindow.__init__(self)

        # config the window
        self.setupUi(window)

        # database
        self.database = Database()

        # bad words
        self.bad_words = IdentifyBadWords()

        # replace words
        self.replace_words = ReplaceWords()

        # first sentence
        self.love_sentences()

        # loop
        timer.timeout.connect(self.love_sentences)
        timer.start(INTERVAL_SENTENCES)

    def love_sentences(self):
        has_bad_words = True
        sentence = ''
        while has_bad_words:
            sentence = self.database.get_love_sentence()
            has_bad_words = self.bad_words.has_bad_words(sentence)

        # replace words
        mixed_sentence = self.replace_words.replace(sentence)

        # insert line break after '.'
        rx = r"\. "
        sentence_new_lines = re.sub(rx, '.<br />', mixed_sentence)
        self.mainText.setHtml(MAIN_TEXT_FORMAT.replace('MESSAGE', sentence_new_lines))
        print("{} {}".format(sentence_new_lines, len(sentence_new_lines)))

        # insert sentences in the database
        self.database.insert_generated_sentences(sentence, mixed_sentence)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    prog = Window(window)
    window.showFullScreen()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
