"""Word Operations"""
"""
    Provides basic operations with texts such as tokenizing and splitting
    articles to arbitrary lengths, filtering and removing characters
"""

import nltk

from nltk import word_tokenize
from nltk import pos_tag
from nltk import sent_tokenize
from nltk.corpus import stopwords
import re

def getWordToks(sent):
    toks = word_tokenize(sent)
    return toks

def removePunct(text):
    puncts = ['.',',','\'','\"','`','\'\'','-','...','``']
    return [w for w in text if w not in puncts]

def removeStopWords(text):
    stop_words = stopwords.words("english")
    return [w for w in text if w not in stop_words]

def splitSent(text):
    sentSets = sent_tokenize(text)
    return sentSets

def splitParagraphs(text):
    paragraphSets = re.split('\n\n',text)
    return paragraphSets

def filter_stops(text):
    return removeStopWords(removePunct(text))
