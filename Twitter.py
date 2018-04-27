from tweepy import *

TWITTER_CONSUMER_KEY = 'egHmh9cS3AaQGqT9iFgDTOjxs'
TWITTER_CONSUMER_SECRET = '3QpjqsiQCczr2krubmJMvXFWj001Ea8HPdXCQQL4OCS6CAUOVe'
TWITTER_ACCESS_TOKEN = '976787781417566208-lQUqKu8IC9yQSPCehDErkaVxv6oGkTa'
TWITTER_ACCESS_TOKEN_SECRET = 'dzNA4XMSzCmlMLtCHXtrFvqJbGXCAnytRJuQf7A9CAW6g'

class Twitter:
    def __init__(self):
        super().__init__()
        self.auth = OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
        self.auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
        self.api = API(self.auth)

    def update_status(self, sentence):
        self.api.update_status(sentence)