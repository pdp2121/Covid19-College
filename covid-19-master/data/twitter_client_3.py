import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    try:
        consumer_key = "7w9dhtOBqnGbpfDUus7qkRr9t"
        consumer_secret = "JkvjNGSzzgjoynldUNGbfZsZRHCVMtcM7El2E6n51wS2IRCsr7"
        access_token = "3300503975-59cdOLI6CthD2qquO0j2oyLHRGJeNDEqfCsAKLv"
        access_secret = "sutQSm0BpwS9cxUbbWEBrgUIF7DLt9UXgAKrlq3W63hwD"
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