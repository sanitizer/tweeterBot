import tweepy
import json


class TwitterClient:

    config_path = "resources/tweepy_config.json"

    def __init__(self, path=config_path):
        self.config_path = path

    def connect(self):
        config = json.load(open(self.config_path, 'r'))
        auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
        auth.set_access_token(config["access_token"], config["access_token_secret"])
        return tweepy.API(auth)
