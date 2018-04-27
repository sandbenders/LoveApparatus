from pymongo import MongoClient

import datetime


class Database:
    def __init__(self):
        super().__init__()
        self.client = MongoClient()
        self.db = self.client.love_apparatus
        self.collection_sentences = self.db.love_sentences
        self.collection_generated_sentences = self.db.generated_sentences

    def get_love_sentence(self):
        pipeline = [
            {'$match': {'$text': {'$search': 'love'}}},
            {'$project': {'_id': 0, 'text': 1}},
            {'$redact': {'$cond': [{'$lte': [{'$strLenCP': '$text'}, 140]}, '$$KEEP', '$$PRUNE']}},
            {'$sample': {'size': 1}}
        ]

        sentence = list(self.collection_sentences.aggregate(pipeline))[0]

        return sentence['text']

    def insert_generated_sentences(self, original, mixed):
        generated_sentence = {
            'original_sentence': original,
            'mixed_sentence': mixed,
            'date': datetime.datetime.utcnow()
        }

        self.collection_generated_sentences.insert(generated_sentence)
