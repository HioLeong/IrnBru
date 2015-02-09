import itertools

from nltk import FreqDist
from nltk.tokenize import *
from nltk.corpus import stopwords

from topics_trainer.models import Article, Choice
from topics_editor.models import Topic

def get_topic_from_id(topic_id):
    return Topic.objects.get(id=topic_id).topic

def get_choices_of_topic(topic_id):
    return Choice.objects.filter(topic__contains=topic_id)

def get_articles_bodies_from_choices(choices):
    article_ids = [c.choice_id for c in choices]
    bodies = [ a.body for a in Article.objects.filter(id__in=article_ids)]
    return aggregate_list_of_lists(bodies)

def aggregate_list_of_lists(lists):
    return [item for sublist in lists for item in sublist]

def get_tokens_of_topic(bodies):
    toks = [word_tokenize(b) for b in bodies]
    filtered_toks = [t for t in toks if not t in get_stopwords()]
    return aggregate_list_of_lists(filtered_toks)

def get_stopwords():
    corpus_stopword = stopwords.words('english')
    f = open('article_summary/static/global_stopwords.txt', 'r')
    global_stopword = []
    for line in f:
        global_stopword.append(line[:-1])

    return corpus_stopword + global_stopword
