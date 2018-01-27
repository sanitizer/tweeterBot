from tweeterBot.tweepy_connector.tweepy_client import TwitterClient


class Bot:

    def __init__(self):
        self.connector = TwitterClient().connect()

    def get_home_timeline(self):
        return self.connector.home_timeline()

    def get_friend_tweets(self, userId):
        return self.connector.user_timeline(userId)

    def get_tweet_calls_stats(self):
        stats = Stats()
        data = self.connector.rate_limit_status()
        stats.limit = data["resources"]["tweets"]["/tweets/search/:product/:label"]["limit"]
        stats.remaining = data["resources"]["tweets"]["/tweets/search/:product/:label"]["remaining"]
        return stats

    def create_tweet(self, tweet):
        return self.connector.update_status(tweet)

    def get_followers(self):
        return self.connector.followers()


class Stats:

    def __init__(self):
        self.limit = 0
        self.remaining = 0

    def __str__(self):
        return "limit: {} remaining: {}".format(self.limit, self.remaining)


bot = Bot()
