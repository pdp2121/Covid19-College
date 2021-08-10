import sys
import json
import os
import tweepy
from tweepy import Cursor
import progressbar
import datetime
import time
import twitter_client
import twitter_client_1
import twitter_client_2
import twitter_client_3
import twitter_client_4
import twitter_client_5
import twitter_client_6
import twitter_client_7
import twitter_client_8

start_date = datetime.datetime(2020, 1, 20, 0, 0, 0)
end_date = datetime.datetime(2020, 3, 20, 23, 59, 59)

def get_tweets(userid, api, output_dir):
    print("Getting <{}> tweets".format(userid))
    output_file = "{}_tweets.jsonl".format(userid)
    if output_file in os.listdir(output_dir):
        print('Skip!')
    else:
        count = 0
        with progressbar.ProgressBar(max_value=progressbar.UnknownLength) as bar:
            tweets = []
            try:
                tmp_tweets = api.user_timeline(user_id=userid, count=200)
                for tweet in tmp_tweets:
                    if tweet.created_at < end_date and tweet.created_at > start_date:
                        tweets.append(tweet)
                        count += 1
                        bar.update(count)

                if tweets:
                    last_tweet = None
                    while tmp_tweets[-1].created_at > start_date and tmp_tweets[-1] != last_tweet:
                        print("\nLast tweet @", tmp_tweets[-1].created_at, " - Fetch more ...")
                        tmp_tweets = api.user_timeline(user_id=userid, count=200, max_id = tmp_tweets[-1].id)
                        last_tweet = tmp_tweets[-1]
                        for tweet in tmp_tweets:
                            if tweet.created_at < end_date and tweet.created_at > start_date:
                                tweets.append(tweet)
                                count += 1
                                bar.update(count)
                    with open(output_dir+'/'+output_file, 'w') as f:
                        for tweet in tweets:
                            f.write(json.dumps(tweet._json)+"\n")
            except tweepy.TweepError as e:
                print(e)
                pass
                
                

if __name__ == '__main__':
    api = twitter_client.get_twitter_client()
    api_1 = twitter_client_1.get_twitter_client()
    api_2 = twitter_client_2.get_twitter_client()
    api_3 = twitter_client_3.get_twitter_client()
    api_4 = twitter_client_4.get_twitter_client()
    api_5 = twitter_client_5.get_twitter_client()
    api_6 = twitter_client_6.get_twitter_client()
    api_7 = twitter_client_7.get_twitter_client()
    api_8 = twitter_client_8.get_twitter_client()

    api_list = [api, api_1, api_2, api_3, api_4, api_5, api_6, api_7, api_8]
    input_file = sys.argv[1]
    directory = os.getcwd()
    output_dir = directory+'/user-timelines'

    users = json.load(open(input_file, 'r'))

    for i in range(len(users)):
        userid = users[i]['id']
        api_idx = i%9
        # print('***', api_idx)
        get_tweets(userid, api_list[api_idx], output_dir)