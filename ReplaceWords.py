from nltk.corpus import wordnet
from nltk.tag import pos_tag

import random
import re

REPLACEMENT_RATIO = 0.90

class ReplaceWords():
    def __init__(self):
        super().__init__()

    def replace(self, sentence):
        tagged_sentence = pos_tag(sentence.split())
        new_sentence = ''

        # identify nouns and verbs
        nouns = [word for word, pos in tagged_sentence if 'NN' in pos]
        verbs = [word for word, pos in tagged_sentence if 'VB' in pos]

        nouns = self.remove_words_from_list(nouns)
        verbs = self.remove_words_from_list(verbs)

        self.remove_words_from_list(nouns)

        # replace words
        sentence = self.search_and_replace(nouns, sentence)
        sentence = self.search_and_replace(verbs, sentence)

        return sentence.capitalize()

    def remove_words_from_list(self, list):
        words_to_remove = ['is',
                           'are',
                           'be',
                           'love',
                           'was',
                           'were',
                           'have',
                           'has',
                           'men',
                           'man',
                           'women',
                           'woman',
                           'lovers']
        for word in words_to_remove:
            while True:
                try:
                    list.remove(word)
                except:
                    break
        return list

    def search_and_replace(self, list, sentence):
        if list:
            for element in list:
                if random.uniform(0, 1) > REPLACEMENT_RATIO:
                    print(">>> replacing words")
                    synonyms = []
                    for syn in wordnet.synsets(element):
                        for l in syn.lemmas():
                            synonyms.append(l.name())
                    while True:
                        try:
                            synonyms.remove(element)
                        except:
                            break
                    if synonyms:
                        rx = r'\b{}\b'.format(element)
                        sentence = re.sub(rx, synonyms[0], sentence)
        return sentence
