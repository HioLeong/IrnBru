from nltk.tokenize import sent_tokenize

from topics_editor.models import Topic
from article_summary.word_op import *

def sent_contains_topic_common_words(sent, topic_name):
    common_words = Topic.objects.get(topic=topic_name).common_words
    # TODO: if words exist - include the ranking
    for rank, val in enumerate(common_words):
        if val.word in sent:
            return True
        else:
            return False

def get_sentences_from_article(article):
    body = article.body
    sentences = []
    for block in body:
        art_sent = sent_tokenize(block)
        sentences.append(art_sent)
    return aggregate_list_of_lists(sentences)

def get_factor_sentence_for_topic(topic):
    # TODO: Break the article into sentences,
    return
