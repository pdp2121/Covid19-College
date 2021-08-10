import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    try:
        consumer_key = "XIn6Q7KCd9Rq5VSa840bg7Gb9"
        consumer_secret = "4mkGnzY5ZFYdQbyvEslBwNHzVmsHhrhYNwAgQoc6HKHLokQzn6"
        access_token = "3300503975-2cFYNVsnYuRwqNa8hefwQQ95UA2rZAFYjtk5Jm4"
        access_secret = "FO1uI4KsUWuAcsCXvd7LZRMiBnm2g7qFvTkU6n17xCbOT"
    except KeyError:
        sys.stderr.write("TWITTER_* environment variables not set\n")
        sys.exit(1)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

def get_twitter_client():
    auth = get_twitter_auth()
    client = API(auth)
    return client