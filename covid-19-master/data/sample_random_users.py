import os
import sys
import json
import math
from collections import defaultdict
import random

def merge_user_lists(input_dir, include_protected=1):
    user_dict = defaultdict(lambda:None)
    for file_name in sorted(os.listdir(input_dir)):
        if file_name.endswith('.json'):
            college = file_name.split('_followers')[0]
            users = open(input_dir+'/'+file_name,'r').readlines()
            users = [json.loads(u) for u in users]
            for user in users:
                if include_protected == 0:
                    if user['protected']:
                        continue
                if user['screen_name'] in user_dict.keys():
                    user_dict[user['screen_name']]['college'].append(college)
                else:
                    user_dict[user['screen_name']] = {}
                    user_dict[user['screen_name']]['id'] = user['id']
                    user_dict[user['screen_name']]['id_str'] = user['id_str']
                    user_dict[user['screen_name']]['screen_name'] = user['screen_name']
                    user_dict[user['screen_name']]['name'] = user['name']
                    user_dict[user['screen_name']]['location'] = user['location']
                    user_dict[user['screen_name']]['college'] = [college]
                    user_dict[user['screen_name']]['followers_count'] = user['followers_count']
                    user_dict[user['screen_name']]['friends_count'] = user['friends_count']
                    user_dict[user['screen_name']]['listed_count'] = user['listed_count']
                    user_dict[user['screen_name']]['favourites_count'] = user['favourites_count']
                    user_dict[user['screen_name']]['statuses_count'] = user['statuses_count']
                    user_dict[user['screen_name']]['description'] = user['description']
                    user_dict[user['screen_name']]['description'] = user['description']
                    user_dict[user['screen_name']]['profile_image_url'] = user['profile_image_url']
                    
            print('<{}> users added. Total: {}'.format(college, len(user_dict.keys())))

    return user_dict, list(user_dict.values())

def write_batches(user_list, output_dir, batch_size):
    user_batch = []
    for i in range(len(user_list)):
        if i % batch_size == 0 and i != 0:
            with open(output_dir+'/batch_{}.json'.format(int(i/batch_size)), 'w') as batch_file:
                print('Writing batch_{}'.format(int(i/batch_size)))
                json.dump(user_batch, batch_file, indent=1)
            user_batch = [user_list[i]]
        else:
            user_batch.append(user_list[i])
            if i == len(user_list)-1:
                with open(output_dir+'/batch_{}.json'.format(math.ceil(i/batch_size)), 'w') as batch_file:
                    print('Writing batch_{}'.format(math.ceil(i/batch_size)))
                    json.dump(user_batch, batch_file, indent=1)

def sample_users(user_list, sample_size=5000):
    random.shuffle(user_list)
    return random.sample(user_list, sample_size)

if __name__ == '__main__':
    directory = os.getcwd()
    input_dir = directory+'/college-followers'

    K = int(sys.argv[1])
    include_protected = int(sys.argv[2])

    user_dict, user_list = merge_user_lists(input_dir, include_protected=include_protected)
    # user_sample = sample_users(user_list, sample_size=K)
    # print('Created user sample of size', len(user_sample), 'from', len(user_list), 'users.')

    output_file = directory+'/college_followers_sample_{}.json'.format(K)
    
    user_sample = json.load(open(output_file, 'r'))

    for user in user_sample:
        user['profile_image_url'] = user_dict[user['screen_name']]['profile_image_url']

    with open(directory+'/college_followers_sample_{}.json'.format(K), 'w') as f:
        json.dump(user_sample, f, indent=2)
