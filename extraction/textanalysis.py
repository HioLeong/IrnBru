import json

from nltk import word_tokenize
from nltk import pos_tag
from nltk import sent_tokenize
from nltk.corpus import stopwords
from wordoperations import *

TOPIC_JSON_FILE_DIR = "../res/topic.json"

def get_freq_of_word_toks(word_tags):
    return nltk.FreqDist(word_tags)

def get_max_of_freq(freq, n=1):
    freq.most_common()

def word_toks_in_topic_words(word_toks, topic_words, topic):
    for tok in word_toks:
        if (tok in topic_words): 
            return topic
    return ''

#TODO: Refactor - this opens the json file everytime
def match_topic_words(word_toks):
    related_topics = []

    json_data = open(TOPIC_JSON_FILE_DIR)
    data = json.load(json_data)

    for topic in data:
        topic_words = [topic['topic']] + topic['seeds']
        res = word_toks_in_topic_words(word_toks, topic_words, topic['topic'])
        if len(res) > 0:
            return res
    return ""

def get_topic_of_article(article_body):
    article_topic = []
    for sent in article_body:
        word_toks = getWordToks(sent)
        word_toks = filter_stops(word_toks)
        if len(word_toks) > 0:
            freq = get_freq_of_word_toks(word_toks)
            res = match_topic_words(word_toks)
            if (len (res) != 0):
                if res not in article_topic:
                    article_topic.insert(0, res)
    return article_topic
            #print freq.items()

