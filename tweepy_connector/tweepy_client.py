import tweepy
import json

class TwitterClient:

    config_path = "resources/config.json"

    def __init__(self):
        config = json.load(open(self.config_path, 'r'))
        auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
        auth.set_access_token(config["access_token"], config["access_token_secret"])
        self.connector = tweepy.API(auth)