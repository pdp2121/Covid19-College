import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    try:
        consumer_key = "PQKI5F3kwsOiz4yOvjML0Ay7H"
        consumer_secret = "xJcksMCABgTpMzPFeVBI5OgMYQIYAdjWmVjbzTDqDOgaOV5tKj"
        access_token = "3300503975-NOrGvkB9o25So43WOyyam3X5wIpttBzLDQ16RAr"
        access_secret = "Tq9xX6ZU70Um7CZZ3Cfqf38yP71tdhu0mf9hIjTVp0htc"
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