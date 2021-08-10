import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    try:
        consumer_key = "FPysg6t5v0NYimIgmyZg3en4b"
        consumer_secret = "s5TKwwQftcaP6LXBXc6IfGFaVJfc7bIg3xBDJk6ZKSQ1iVxPKC"
        access_token = "3300503975-ktaBIP8UNA2qIgJQ81vXBF4dekYvIFwbkmi1BmP"
        access_secret = "gEetGNiO43KairoRBppksoDPHyGirVPf5Z8vA53h7nVrM"
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