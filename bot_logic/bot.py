from tweeterBot.tweepy_connector.tweepy_client import TwitterClient


class Bot:

    def __init__(self):
        self.connector = TwitterClient().connect()

    def get_my_twitts(self):
        return self.connector.home_timeline()


print(Bot().get_my_twitts())