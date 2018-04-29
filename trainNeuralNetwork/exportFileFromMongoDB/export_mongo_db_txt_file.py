# awk '!seen[$0]++' filename

import pymongo
from IdentifyBadWords import *

MONGO_URI = 'mongodb://localhost:27017'
MONGO_DATABASE = 'love_apparatus'
COLLECTION_NAME = 'love_sentences'

client = pymongo.MongoClient(MONGO_URI)
db = client[MONGO_DATABASE]

bad_words = IdentifyBadWords('../../listBadWords/full-list-of-bad-words-utf-8.txt')

pipeline = [
            {'$project': {'_id': 0, 'text': 1}},
            # {'$redact': {'$cond': [{'$lte': [{'$strLenCP': '$text'}, 140]}, '$$KEEP', '$$PRUNE']}}
        ]

texts = list(db[COLLECTION_NAME].aggregate(pipeline))

for text in texts:
    only_text = text['text']
    if not bad_words.has_bad_words(only_text):
        with open('loveQuotes.txt', 'ab') as output_file:
            only_text = only_text.replace('...', ' ')
            only_text = " ".join(only_text.split()) + ' '
            only_text = only_text.replace('. . .', '')
            only_text = only_text + '\n'
            output_file.write(only_text.encode("utf-8"))
            print(only_text)

client.close()
