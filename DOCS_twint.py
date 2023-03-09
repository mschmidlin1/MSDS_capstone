
import tweepy
from my_secrets import TWITTER_API_KEY, TWITTER_BEARER_TOKEN, TWITTER_SECRET_KEY

auth = tweepy.OAuth2BearerHandler(TWITTER_BEARER_TOKEN)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

