import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    try:
        consumer_key = "8UIZw79qs1WurXzKeb9cR3yRx"
        consumer_secret = "P8IMfhUgzdStJNC6wTs1FE5c57TpcBbbWGSr5BEV5VYqY1JVB4"
        access_token = "3300503975-VBd4DepTbOUfXAVyP7bNPyC36xwii5NnJK6YRaW"
        access_secret = "UrHoA7CyDAonIFz3xLOKartZxiFcm7digNTEh91Db80Xq"
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