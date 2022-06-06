from tweepy import *

TWITTER_CONSUMER_KEY = 'REPLACE'
TWITTER_CONSUMER_SECRET = 'REPLACE'
TWITTER_ACCESS_TOKEN = 'REPLACE'
TWITTER_ACCESS_TOKEN_SECRET = 'REPLACE'

class Twitter:
    def __init__(self):
        super().__init__()
        self.auth = OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
        self.auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
        self.api = API(self.auth)

    def update_status(self, sentence):
        try:
            self.api.update_status(sentence.replace('<br />', ' '))
        except:
            pass
