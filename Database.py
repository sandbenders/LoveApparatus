import random

from pymongo import MongoClient


class Database:
    def __init__(self):
        super().__init__()
        self.client = MongoClient()
        self.db = self.client.goodreads_quotes
        self.collection = self.db.love

    def get_love_sentence(self):
        pipeline = [
            {"$project": {"_id": 0, "text": 1}},
            {"$sample": {"size": 1}}
        ]

        sentence = list(self.collection.aggregate(pipeline))[0]

        return sentence['text']


# def thread_func():
#     print("Thread works")
#     timer = QtCore.QTimer()
#     timer.timeout.connect(timer_func)
#     timer.start(1000)
#     print(timer.remainingTime())
#     print(timer.isActive())
#     timers.append(timer)
#
# def timer_func():
#     print("Timer works")
