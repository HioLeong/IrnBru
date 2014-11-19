import wordoperations
import nltk

from nltk import word_tokenize
from nltk import pos_tag
from nltk import sent_tokenize
from nltk.corpus import stopwords
from wordoperations import *

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

def getNames(tags):
    names = [a for (a,b) in tags if b =='NNP']
    return names

def getFreqDistOfToks(word_tags):
    return nltk.FreqDist(word_tags)

def demo():
    article = getArticleFromDir('../res/BBCOil.txt')
    print splitSent(article)
    word_toks = getWordToks(article)
    stop_words = stopwords.words("english")

    word_toks = filter(text)
    print(getFreqDistOfToks(word_toks).pprint())

def getMaxFreqWords(word_toks):
    return getFreqDistOfToks(word_toks)

def main():
    #demo()
    article = getArticleFromDir('../res/EconomistNationalist.txt')

    word_toks = getWordToks(article)
    word_toks = filter(word_toks)

    print getMaxFreqWords(word_toks).pprint()

if __name__ == "__main__":
    main()
