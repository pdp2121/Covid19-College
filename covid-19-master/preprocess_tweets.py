import sys
import os
import json
import langdetect
import pandas as pd
from ekphrasis.classes.preprocessor import TextPreProcessor
from ekphrasis.classes.tokenizer import SocialTokenizer
from ekphrasis.classes.segmenter import Segmenter
from ekphrasis.dicts.emoticons import emoticons
from ekphrasis.dicts.noslang.slangdict import slangdict
import re
import datetime
from collections import defaultdict
import math

def preprocess(text):
    text = text.lower()
    text = re.sub(",", " ", text)
    text = re.sub("@ ", "@", text)
    text = re.sub("# ", "#", text)
    # text = re.sub(r"\'", "", text)
    text = re.sub('\S*@\S*\s?', '', text)
    text = re.sub(r"\"", "", text)
    text = re.sub("\'", "", text)
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r'\w*pic.twitter.co\w*', '', text)
    text = re.sub(r'\w*twitter.co\w*', '', text)
    text = re.sub(r'\w*twitter.com\w*', '', text)
    text = re.sub(r"./\S+", "", text)
    text = re.sub(r"@ \S+", "", text)
    text = re.sub(r"#\S+", "", text)
    text = re.sub(r'\n+', " ", text)
    try:
        if langdetect.detect(text) == 'en':
            return text
        else:
            return ""
    except:
        return ""

# def process_tags(text):
#     for e in re.findall(r"<hashtag>.*?</hashtag>", text):
#         segmented = e.split("<hashtag>")[1].split("</hashtag>")[0].strip()
#         hashtag = "_".join(segmented.split(" "))
#         text = re.sub(segmented, hashtag, text)
#     return text

directory = os.getcwd()
users = json.load(open(directory+'/college_followers_sample_100000.json', 'r'))

data = pd.DataFrame(columns=['id','conversation','username','text','retweets','favorites','date'])
text_processor = TextPreProcessor(
    # terms that will be normalized
    normalize=['url', 'email', 'percent', 'money', 'phone', 'user', 'time', 'date'],
    # terms that will be annotated
    annotate=['hashtag', 'allcaps', 'elongated', 'repeated', 'emphasis', 'censored'],
    fix_html=True,  # fix HTML tokens
    
    # corpus from which the word statistics are going to be used
    # for word segmentation 
    segmenter="twitter", 
    
    # corpus from which the word statistics are going to be used 
    # for spell correction
    corrector="twitter", 
    
    unpack_hashtags=True,  # perform word segmentation on hashtags
    unpack_contractions=True,  # Unpack contractions (can't -> can not)
    spell_correct_elong=True,  # spell correction for elongated words
    spell_correction=True,
    
    # select a tokenizer. You can use SocialTokenizer, or pass your own
    # the tokenizer, should take as input a string and return a list of tokens
    tokenizer=SocialTokenizer(lowercase=True).tokenize,
    
    # list of dictionaries, for replacing tokens extracted from the text,
    # with other expressions. You can pass more than one dictionaries.
    dicts=[emoticons, slangdict]
    )

segmenter = Segmenter(corpus="twitter") 
count = 0
all_texts = []
tweet_dict = defaultdict(lambda:None)

for user in users:
    tweet_file = directory+'/user-timelines/'+str(user['id'])+'_tweets.json'
    tweets = json.load(open(tweet_file, 'r'))
    for tweet in tweets:
        # text = preprocess(tweet['content']['text'])
        tokens = text_processor.pre_process_doc(tweet['text'])
        tokens = [segmenter.segment(t) for t in tokens]
        text = " ".join(tokens)
        if text:
            tweet_dict[]


# tweet_by_date = data.groupby('date').count()
# tweet_by_date.to_csv(directory+"/date.csv", index=False)