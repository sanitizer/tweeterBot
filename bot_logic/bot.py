from tweeterBot.api_connector.tweepy_client import TwitterClient
from tweeterBot.api_connector.aylien_client import AylienClient


class Bot:

    def __init__(self):
        self.twitter_connector = TwitterClient().connect()
        self.aylien_connector = AylienClient().connect()

    def get_home_timeline(self):
        return self.twitter_connector.home_timeline()

    def get_friend_tweets(self, userId):
        return self.twitter_connector.user_timeline(userId)

    def get_tweet_calls_stats(self):
        stats = Stats()
        data = self.twitter_connector.rate_limit_status()
        stats.limit = data["resources"]["tweets"]["/tweets/search/:product/:label"]["limit"]
        stats.remaining = data["resources"]["tweets"]["/tweets/search/:product/:label"]["remaining"]
        return stats

    def create_tweet(self, tweet):
        return self.twitter_connector.update_status(tweet)

    def get_followers(self):
        return self.twitter_connector.followers()

    def get_text_processing_limits(self):
        data = self.aylien_connector.RateLimits()
        stats = Stats()
        if "limit" in data and "remaining" in data:
            stats.limit = data["limit"]
            stats.remaining = data["remaining"]
        return stats


class Stats:

    def __init__(self):
        self.limit = -1
        self.remaining = -1

    def __str__(self):
        return "limit: {} remaining: {}".format(self.limit, self.remaining)


bot = Bot()
print(bot.get_text_processing_limits())