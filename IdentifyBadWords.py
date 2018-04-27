import nltk


class IdentifyBadWords:
    def __init__(self):
        super().__init__()

        # load list of bad words
        self.list_of_bad_words = set(line.strip() for line in open('listBadWords/full-list-of-bad-words-utf-8.txt'))

    def has_bad_words(self, sentence):
        return self.list_of_bad_words.intersection(nltk.word_tokenize(sentence))
