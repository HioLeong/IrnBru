from django.test import TestCase

from topics_editor.models import Topic, WordFrequency
from topics_trainer.models import Article, Choice
from factors_trainer.factors import *

class SimpleTest(TestCase):
    def setUp(self):
        topic_object = Topic.objects.create(topic='energy', 
                common_words=[WordFrequency(word='hello', frequency=10),
                    WordFrequency(word='world', frequency=5)])
        article_object = Article.objects.create(title='Hello goodbye', body=['there. how are you world?', 'how about a hello world?'])
        Choice.objects.create(choice=article_object, topic = ['energy'])

    def tearDown(self):
        Topic.objects.all().delete()
        Article.objects.all().delete()
        Choice.objects.all().delete()

    def test_sent_contains_topic_common_words(self):
        if Topic.objects.count() == 0:
            self.setUp()
        test_sentence = "how are you world?"
        expected = True
        actual = sent_contains_topic_common_words(test_sentence, 'energy')
        self.assertEqual(expected, actual)
        expected = False
        false_sentence = "nothingness"
        actual = sent_contains_topic_common_words(false_sentence, 'energy')
        self.assertEqual(expected, actual)

    def test_get_factor_sentences_for_topic(self):
        topic = Topic.objects.get(topic='energy')
        expected = ['how are you world?', 'how about a hello world?']
        actual = get_factor_sentences_for_topic(topic)
        self.assertEqual(expected, actual)

    def test_get_sentences_from_article(self):
        article = Article(title='title', body=['sentence one. sentence two.', 'sentence three.'])
        expected = ['sentence one.', 'sentence two.', 'sentence three.']
        actual = get_sentences_from_article(article)
        self.assertEqual(expected, actual)

    def test_get_articles_from_choices(self):
        if Topic.objects.count() == 0:
            self.setUp()
        choices = Choice.objects.all()
        expected = Article.objects.all()
        actual = get_articles_from_choices(choices)
        self.assertEqual(expected[0], actual[0])

    def test_update_factors(self):
        if Topic.objects.count() == 0:
            self.setUp()
        update_factors()
        topic = Topic.objects.all()[0]
        expected = [Factor(topic=topic,factor='how are you world?',sentiment=''), 
                Factor(topic=topic, factor='how about a hello world?', sentiment='')]
        actual = Factor.objects.all()

    def test_get_pos_tag_of_sentence(self):
        sentence = 'all work no play makes michael a dull boy'
        expected = ['DT', 'NN', 'DT', 'NN', 'VBZ', 'NN', 'DT', 'NN', 'NN']
        actual = get_pos_tag_of_sentence(sentence)
        self.assertEqual(expected, actual)


    def test_aggregate_pos_tags(self):
        pos_tags = ['DT', 'NN', 'DT', 'NN', 'VBZ', 'NN', 'DT', 'NN', 'NN']
        expected ='<DT><NN><DT><NN><VBZ><NN><DT><NN><NN>'
        actual = aggregate_pos_tags(pos_tags)
        self.assertEqual(expected, actual)

    def test_get_factor_word_list(self):
        word_list = ['hello', 'hello', 'world', 'foo','foo', 'bar']
        expected = ['hello', 'world', 'foo', 'bar']
        actual = get_factor_word_list(word_list)
        self.assertEqual(expected, actual)

    def test_get_trigrams_features(self):
        sent = 'Hello world, how are you today?'
        print get_trigrams_features(sent)
        # TODO: Finish

