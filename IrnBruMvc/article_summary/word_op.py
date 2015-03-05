from nltk import FreqDist
from nltk.tokenize import *
from nltk.corpus import stopwords

from topics_trainer.models import Article, Choice
from topics_editor.models import Topic, WordFrequency

def get_topic_from_id(topic_id):
    return Topic.objects.get(id=topic_id).topic

def get_choices_of_topic(topic_id):
    return Choice.objects.filter(topic__contains=topic_id)

def get_article_from_choice(choice):
    article_id = choice.choice_id
    return Article.objects.get(id=article_id)

def get_articles_bodies_from_choices(choices):
    article_ids = [c.choice_id for c in choices]
    bodies = [ a.body for a in Article.objects.filter(id__in=article_ids)]
    return aggregate_list_of_lists(bodies)

def get_tokens_of_topic(bodies):
    toks = aggregate_list_of_lists([word_tokenize(b) for b in bodies])
    toks = [t.lower() for t in toks]

    filtered_toks = [t for t in toks if not t in get_stopwords()]
    return filtered_toks

def get_freqdist_of_toks(toks):
    return FreqDist(toks)

def get_stopwords():
    corpus_stopword = stopwords.words('english')
    f = open('article_summary/static/global_stopwords.txt', 'r')
    global_stopword = []
    for line in f:
        global_stopword.append(line[:-1])
    return corpus_stopword + global_stopword

''' Updates the most common words in the articles so far '''
def update_topics_common_words(numberOfWords):
    topics = Topic.objects.all()
    for topic in topics:
        choices = get_choices_of_topic(topic.id)
        article_bodies = get_articles_bodies_from_choices(choices)
        bodies_toks = get_tokens_of_topic(article_bodies)
        most_common = get_freqdist_of_toks(bodies_toks).most_common(numberOfWords)
        most_common_wordfrequency = get_wordfrequency_model_from_tuples(most_common)
        topic.common_words = most_common_wordfrequency
        topic.save()

def get_wordfrequency_model_from_tuples(tuples):
    wordfrequency_list= []
    for t in tuples:
        wordfrequency_list.append(WordFrequency(word=t[0], frequency=t[1]))
    return wordfrequency_list

def aggregate_list_of_lists(lists):
    return [item for sublist in lists for item in sublist]
