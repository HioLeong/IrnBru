from string import punctuation
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams
from nltk.featstruct import FeatStruct

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
    #factor_sentences = [s for s in sentence_article_tuple if sent_contains_topic_common_words(s[0], topic.topic)]
    return sentence_article_tuple

def update_factors():
    topics = Topic.objects.all()
    for t in topics:
        factor_sentences = get_factor_sentences_for_topic(t)
        for sent_art_tuple in factor_sentences:
            create_factor_from_sent_art_tuple(sent_art_tuple, t)

def create_factor_from_sent_art_tuple(sent_art_tuple, topic):
    # Create Factor if factor does not exist
    if not Factor.objects.filter(factor=sent_art_tuple[0]).exists():
        Factor.objects.create(
                topic = topic,
                factor = sent_art_tuple[0],
                sentiment = '',
                article = sent_art_tuple[1])
        return True
    else: 
        return False
            


def get_next_factor():
    return Factor.objects.filter(sentiment='')[0]

def get_factors_for_topic(topic):
    return Factor.objects.filter(topic_id=topic.id)

def get_factors_with_sentiment(sentiment):
    return Factor.objects.filter(sentiment=sentiment)

def get_pos_tag_of_sentence(sentence):
    sentence_toks = word_tokenize(sentence)
    return [tag[1] for tag in nltk.pos_tag(sentence_toks)]

def aggregate_pos_tags(pos_tags):
    aggregate = ''
    for tag in pos_tags:
        aggregate += '<' + tag + '>'
    return aggregate

def remove_punctuations(sentence):
    return ''.join(ch for ch in sentence if ch not in set(punctuation))

def get_factor_word_list(factor):
    factor_sent = remove_punctuations(factor.factor)
    factor_sent.lower()
    word_toks = word_tokenize(factor_sent)
    stop_words = stopwords.words('english')
    filtered_toks = [t for t in word_toks if not t in stop_words]
    word_list = []
    for tok in filtered_toks:
        if tok not in word_list:
            word_list.append(tok)
    return word_list

def get_trigrams_features(factor_sentence):
    factor_toks = word_tokenize(factor_sentence)
    factor_trigrams = get_ngrams_of_factor(factor_toks, 3)
    feat_list = []
    for trigram in factor_trigrams:
        feature = get_trigram_featstruct(trigram)
        feature.freeze()
        feat_list.append((trigram,True))
    return dict(feat_list)

def get_ngrams_of_factor(factor_toks, n=3):
    return list(ngrams(factor_toks, n))

def get_trigram_featstruct(trigram_tuple):
    return FeatStruct(x=trigram_tuple[0],y=trigram_tuple[1],z=trigram_tuple[2])
