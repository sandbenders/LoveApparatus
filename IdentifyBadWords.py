# http://pad.yohdah.com/401/python-has-bad-words

import nltk
import os


class IdentifyBadWords:
    def __init__(self, list_bad_words_file=os.path.join(os.path.dirname(__file__), 'listBadWords/full-list-of-bad-words-utf-8.txt')):
        super().__init__()

        # load list of bad words
        self.list_of_bad_words = set(line.strip() for line in open(list_bad_words_file))

    def has_bad_words(self, sentence):
        return self.list_of_bad_words.intersection(nltk.word_tokenize(sentence))
