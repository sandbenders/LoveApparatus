import sys
import os
import platform

from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from nltk import sent_tokenize

from Twitter import *
from Database import *
from IdentifyBadWords import *
from ReplaceWords import *
from GenerateSample import *
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

        # first sentence
        self.love_sentences()

        # loop
        timer.timeout.connect(self.love_sentences)
        timer.start(INTERVAL_SENTENCES)

    def love_sentences(self):
        type_sentence = ''
        sentence = ''

        if bool(random.getrandbits(1)):
            # normal sentence
            type_sentence = 'normal'
            sentence = self.generate_normal_sentence()
        else:
            # AI sentence
            type_sentence = 'AI'
            sentence = self.generate_ai_sentence()

        sentence_new = self.fix_sentence(sentence)

        self.mainText.setHtml(MAIN_TEXT_FORMAT.replace('MESSAGE', sentence_new))

        # insert sentences in the database
        self.database.insert_generated_sentences(sentence, sentence_new, type_sentence)

        print("{} {}".format(sentence_new, len(sentence_new)))

        # post to twitter
        sentence_new += ' #LoveLeics'
        if len(sentence_new) < 140:
            twitter = Twitter()
            twitter.update_status(sentence_new)


    def check_bad_words(self):
        bad_words = IdentifyBadWords()

        has_bad_words = True
        sentence = ''
        while has_bad_words:
            sentence = self.database.get_love_sentence()
            has_bad_words = bad_words.has_bad_words(sentence)

        return sentence

    def generate_ai_sentence(self):
        print(">>> AI")
        sample = GenerateSample()
        sentence = ''
        with_love = []

        sampled_sentence = ''
        found_sentence = False

        while not found_sentence:
            # get sampled sentence and fix the issue with '.'
            sampled_sentence = self.check_bad_words()
            sampled_sentence = re.sub('[.]+', ',', sampled_sentence)
            
            if 'tegra' in platform.release():
                # jetson
                trained_model = 'trainNeuralNetwork/trainedModel/jetson/jetson.ckpt'
            else:
                trained_model = 'trainNeuralNetwork/trainedModel/charRNN_1.4856_1.2345_bo.ckpt'

            ai_generated_sentence = sample.get_sample(os.path.join(os.path.dirname(__file__), trained_model),
                                                      True, 1000, sampled_sentence, 10)
            sentences = sent_tokenize(ai_generated_sentence)

            for s in sentences:
                if 'love' in s.lower() and len(s) < 140:
                    with_love.append(s)

            if with_love:
                sentence = with_love[random.randint(0, len(with_love) - 1)]
                found_sentence = True

        replace_words = ReplaceWords()

        return replace_words.replace(sentence)

    def generate_normal_sentence(self):
        print(">>> NORMAL SENTENCE")
        replace_words = ReplaceWords()
        sentence = self.check_bad_words()
        return replace_words.replace(sentence)

    def fix_sentence(self, sentence):
        # fix "I" and "I'm"
        rx = r"\bi\b"
        sentence = re.sub(rx, 'I', sentence)
        rx = r"\bi'm\b"
        sentence = re.sub(rx, "I'm", sentence)
        sentence = sentence.replace("_", " ")

        # insert line break after '.'
        rx = r"\. "
        sentence = re.sub(rx, '.<br />', sentence)

        return sentence


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    prog = Window(window)
    window.showFullScreen()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
