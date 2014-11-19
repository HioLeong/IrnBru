from nltk import word_tokenize
from nltk import pos_tag
from nltk import sent_tokenize
from nltk.corpus import stopwords
from wordoperations import *

def get_freq_of_word_toks(word_tags):
    return nltk.FreqDist(word_tags)

def get_max_of_freq(freq, n=1):
    freq.most_common()

