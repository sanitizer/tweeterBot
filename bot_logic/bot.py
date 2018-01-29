#!/usr/bin/python3
from tweeterBot.api_connector.tweepy_client import TwitterClient
from tweeterBot.api_connector.aylien_client import AylienClient
from tweeterBot.bot_logic.model.api_stats import Stats
import re


class Bot:

    def __init__(self):
        self.twitter_connector = TwitterClient().connect()
        self.aylien_connector = AylienClient().connect()

    def get_home_timeline(self):
        return self.twitter_connector.home_timeline()

    def get_friend_tweets(self, user_id):
        return self.twitter_connector.user_timeline(user_id)

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

    def get_user_tweets(self, user_name, num_of_tweets=10):
        return self.twitter_connector.user_timeline(screen_name=user_name,
                                                    count=num_of_tweets,
                                                    tweet_mode="extended")

    # this method should be called after some api call, otherwise will be empty response
    def get_text_processing_limits(self):
        data = self.aylien_connector.RateLimits()
        stats = Stats()

        if "limit" in data and "remaining" in data:
            stats.limit = data["limit"]
            stats.remaining = data["remaining"]

        return stats

    def get_tweet_categories(self, tweet):
        tweet = self.sanitize_text_from_url(tweet)
        tweet = self.sanitize_text_from_refs(tweet)
        data = self.aylien_connector.Classify({"text": tweet})
        result = []
        for category in data["categories"]:
            result.append(category["label"])
        return result

    @staticmethod
    def sanitize_text_from_url(text):
        return re.sub(r'(http://|https://)\S+', '', text)

    @staticmethod
    def sanitize_text_from_refs(text):
        return re.sub(r'@\S', '', text)


def main():
    bot = Bot()


if __name__ == "__main__":
    main()
