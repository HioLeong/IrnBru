from string import punctuation
from nltk.tokenize import sent_tokenize, word_tokenize

from topics_editor.models import Topic
from factors_trainer.models import Factor
from article_summary.word_op import *

#TODO: Refactor topic_name, to common words
def sent_contains_topic_common_words(sent, topic_name):
    common_words = Topic.objects.get(topic=topic_name).common_words
    sent = ''.join(ch for ch in sent if ch not in set(punctuation))
    toks = word_tokenize(sent)
    for rank, val in enumerate(common_words):
        if val.word in toks:
            return True
    return False

def get_sentences_from_article(article):
    body = article.body
    sentences = []
    for block in body:
        art_sent = sent_tokenize(block)
        sentences.append(art_sent)
    return aggregate_list_of_lists(sentences)

def get_articles_from_choices(choices):
    article_id = [c.choice_id for c in choices]
    return Article.objects.filter(id__in=article_id)

def get_factor_sentences_for_topic(topic):
    choices = get_choices_of_topic(topic.id)
    articles = get_articles_from_choices(choices)
    sentence_article_tuple = []
    for article in articles:
        for sentence in get_sentences_from_article(article):
            sentence_article_tuple.append((sentence,article))
    factor_sentences = [s for s in sentence_article_tuple if sent_contains_topic_common_words(s[0], topic.topic)]
    return factor_sentences

def update_factors():
    topics = Topic.objects.all()
    for t in topics:
        factor_sentences = get_factor_sentences_for_topic(t)
        for sent_art_tuple in factor_sentences:
            Factor.objects.create(
                    topic = t,
                    factor = sent_art_tuple[0],
                    sentiment = '',
                    article = sent_art_tuple[1])

def get_next_factor():
    return Factor.objects.filter(sentiment='')[0]

def get_factors_for_topic(topic):
    return Factor.objects.filter(topic_id=topic.id)

def get_factors_with_sentiment(sentiment):
    return Factor.objects.filter(sentiment=sentiment)

