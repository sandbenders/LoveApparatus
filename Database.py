import random

from pymongo import MongoClient


class Database:
    def __init__(self):
        super().__init__()
        self.client = MongoClient()
        self.db = self.client.love_apparatus
        self.collection_sentences = self.db.love_sentences

    def get_love_sentence(self):
        pipeline = [
            {"$project": {"_id": 0, "text": 1}},
            {"$sample": {"size": 1}}
        ]

        sentence = list(self.collection_sentences.aggregate(pipeline))[0]

        return sentence['text']

