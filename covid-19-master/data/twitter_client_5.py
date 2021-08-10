import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    try:
        consumer_key = "fQIYljtbpLvuDd0geFwTUOOI7"
        consumer_secret = "WOkYLQn5K0LrFNu4IHG7PMwikQ5vAo3oJ4cLcxDiCP8k3qApHg"
        access_token = "3300503975-7XFw1Ep1jR1BLWt4rKYqHDNIK4woY6B9U5NP3NL"
        access_secret = "B1rPc1WQo3KvSdOvlX6nPzNz6CepudpRuy1kloNdO5uj9"
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