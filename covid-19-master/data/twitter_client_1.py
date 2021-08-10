import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    try:
        consumer_key = "JyYbwie2O4FspTC7poLVhhYyJ"
        consumer_secret = "EPkefGKDCU1tXcUqlr1AYM9VohrJxRU7VSuRQFksCtIoyokSsa"
        access_token = "3300503975-y1reLFdiqZAsFHgpLK719RwzBwUQ8s3Cb75yW0e"
        access_secret = "Ydp5ZXqU1tGmpxH0UtSrZzt0PrLrnDlEjKafp9vMvhpaq"
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