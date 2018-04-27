import pymongo


MONGO_URI = 'mongodb://localhost:27017'
MONGO_DATABASE = 'goodreads_quotes'
COLLECTION_NAME = 'love'

client = pymongo.MongoClient(MONGO_URI)
db = client[MONGO_DATABASE]

texts = db[COLLECTION_NAME].distinct('text')

for text in texts:
    with open('loveQuotes.txt', 'ab') as output_file:
        text = text.replace('...', ' ')
        text = " ".join(text.split()) + ' '
        text = text.replace('. . .', '')
        output_file.write(text.encode("utf-8"))

client.close()