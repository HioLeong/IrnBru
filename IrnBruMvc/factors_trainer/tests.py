from django.test import TestCase

from topics_editor.models import Topic, WordFrequency
from topics_trainer.models import Article, Choice
from factors_trainer.factors import *

class SimpleTest(TestCase):
    def set_up(self):
        topic_object = Topic.objects.create(topic='energy', 
                common_words=[WordFrequency(word='hello', frequency=10),
                    WordFrequency(word='world', frequency=5)])
        Article.objects.create(title='Hello goodbye', body='hello there. how are you world? how about a hello world?')
        #Choice.objects.create(choice=topic_object, topic = ['energy'])

    def test_sent_contains_topic_common_words(self):
        self.set_up()
        test_sentence = "hello world"
        expected = True
        actual = sent_contains_topic_common_words(test_sentence, 'energy')
        self.assertEqual(expected, actual)

    def get_factor_sentence_for_topic(self):
        topic = Topic.objects.get(topic='energy')
        expected = ['hello there.', 'how are you world?', 'how about a hello world?']
        actual = get_factor_sentence_for_topic(topic)
        self.assertEqual(expected, actual)

    def test_get_sentences_from_article(self):
        article = Article(title='title', body=['sentence one. sentence two.', 'sentence three.'])
        expected = ['sentence one.', 'sentence two.', 'sentence three.']
        actual = get_sentences_from_article(article)
        self.assertEqual(expected, actual)
