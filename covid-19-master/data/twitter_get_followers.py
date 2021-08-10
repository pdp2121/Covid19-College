import os
import sys
import json
import time
import math
from tweepy import Cursor
import random
import twitter_client
import twitter_client_1
import twitter_client_2
import twitter_client_3
import progressbar

# def usage():
#     print("Usage:")
#     print("python {} <username>".format(sys.argv[0]))

def paginate(items, n):
    # enerate n-sized chunks from items
    for i in range(0, len(items), n):
        yield items[i:i+n]

def get_followers(api, usernames, max_followers, output_dir):
    for username in usernames:
        print("Getting <{}> followers".format(username))
        if api == 0:
            api = twitter_client.get_twitter_client()
        if api == 1:
            api = twitter_client_1.get_twitter_client()
        if api == 2:
            api = twitter_client_2.get_twitter_client()
        if api == 3:
            api = twitter_client_3.get_twitter_client()

        max_pages = math.ceil(max_followers/5000)
        count = 0
        json_file = output_dir + '/' + username + '_followers_full.json'
        # txt_file = output_dir + '/' + username + '_followers.txt'
        with open(json_file, 'w') as json_output:
            with progressbar.ProgressBar(max_value=progressbar.UnknownLength) as bar:
                for followers in Cursor(api.followers_ids, screen_name=username).pages(max_pages):
                    for chunk in paginate(followers, 100):
                        try:
                            users = api.lookup_users(user_ids=chunk)
                            for user in users:
                                user_info = user._json
                                screen_name = user_info['screen_name']
                                # with open(txt_file, 'a') as txt_output:
                                #     txt_output.write(screen_name+'\n')
                                json_output.write(json.dumps(user._json)+'\n')
                                count += 1
                                bar.update(count)
                        except:
                            pass
                    if len(followers) == 5000:
                        time.sleep(60)
        print("<{}> followers completed".format(username))
        time.sleep(random.randrange(30, 70, 5))

if __name__ == '__main__':
    directory = os.getcwd()
    user_file = sys.argv[1]
    api = int(sys.argv[2])
    usernames = open(directory+'/'+user_file,'r').readlines()
    usernames = [u.strip() for u in usernames]

    MAX_FOLLOWERS = 1500000
    output_dir = directory + '/college-followers'
    get_followers(api, usernames, MAX_FOLLOWERS, output_dir)