import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    try:
        consumer_key = "ZJVDGnz6vIC6tiTwnkWJaxZQ0"
        consumer_secret = "PVuYxtbeC9G3BVvvQE9MKzQehHnXGo6B9hrOrK0Z3sb5vkxJUu"
        access_token = "3300503975-UCq2XXAa6GxTXU8GgRSG7rjRHkv1QUlu7jlu9yF"
        access_secret = "LLgDn5BpF6yML8q26l1wKpj45NzickVlnQk3H06yu3rfY"
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