import wordoperations
import nltk
import json

from nltk import word_tokenize
from nltk import pos_tag
from nltk import sent_tokenize
from nltk.corpus import stopwords
from wordoperations import *
from textanalysis import *

def sentHasNNP(sent_word_tags):
    for tok in sent_word_tags:
        if tok[1] == 'NNP':
            return True
    return False

def getArticleFromDir(dir): 
    file = open(dir, 'r')
    text = unicode(file.read(), 'utf-8')
    file.close()
    return text

def get_max_freq_word(freq, n=1):
    return


def get_article_from_json(json_dir):
    json_data= open(json_dir)
    data = json.load(json_data)
    for idx, article in enumerate(data):
        article_body = article['body']
        print idx 
        print get_topic_of_article(article_body)

def getNames(tags):
    names = [a for (a,b) in tags if b =='NNP']
    return names

def main():
    article = get_article_from_json('../res/bbcfactors.json')

    #word_toks = getWordToks(article)
    #word_toks = filter(word_toks)

    #print getMaxFreqWords(word_toks).pprint()

if __name__ == "__main__":
    main()
