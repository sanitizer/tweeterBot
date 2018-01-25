import tweepy
import json

class TwitterClient:

    def __init__(self):
        config = json.load(open("config.json", 'r'))
        auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
        auth.set_access_token(config["access_token"], config["access_token_secret"])
        self.client = tweepy.API(auth)