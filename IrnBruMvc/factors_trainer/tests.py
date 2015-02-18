from django.test import TestCase

from topics_editor.models import Topic, WordFrequency
from topics_trainer.models import Article
from factors_trainer.factors import sent_contains_topic_common_words

class SimpleTest(TestCase):
    def set_up(self):
        Topic.objects.create(topic='energy', 
                common_words=[WordFrequency(word='hello', frequency=10),
                    WordFrequency(word='world', frequency=5)])

    def test_sent_contains_topic_common_words(self):
        self.set_up()
        test_sentence = "hello world"
        expected = True
        actual = sent_contains_topic_common_words(test_sentence, 'energy')
        self.assertEqual(expected, actual)

    def test_topic_sentences(self):
        return


    def test_basic_addition(self):
        self.assertEqual(1 + 1, 2)
