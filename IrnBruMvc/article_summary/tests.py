from django.test import TestCase

from article_summary.word_op import *
from topics_editor.models import Topic
from topics_trainer.models import Article, Choice

class TopicsTrainerTest(TestCase):

    TOPIC_ID = u'54c175e59b5295250d06cdbc'

    def setUpChoices(self):
        a1 = Article.objects.create(title="title 1", body=[u"body one", u"body two"])
        a2 = Article.objects.create(title="title 2", body=[u"body three", u"body four"])
        a1.save() 
        a2.save()

        ''' Choices '''
        c1 = Choice.objects.create(choice_id=a1.id, topic=[self.TOPIC_ID])
        c2 = Choice.objects.create(choice_id=a2.id, topic=[self.TOPIC_ID])
        c1.save()
        c2.save()

    def setUp(self):
        topic = Topic.objects.create(id=self.TOPIC_ID, topic=u'energy')
        topic.save()

    def test_get_topic_by_id(self):
        self.setUp()
        expected  = u'energy'
        actual  = get_topic_from_id(self.TOPIC_ID)
        self.assertEqual(expected, actual)

    def test_get_choices_of_topic(self):
        self.setUp()
        self.setUpChoices()
        actual_ids = [c.id for c in Choice.objects.all()]
        # TODO: Rewrite get_choices...  - not orthogonal
        expected_ids = [c.id for c in get_choices_of_topic(self.TOPIC_ID)]
        self.assertEqual(expected_ids, actual_ids)

    def test_aggregate_list_of_lists(self):
        test_lists = [['a'],['b','c']]
        expected = ['a','b','c']
        actual = aggregate_list_of_lists(test_lists)
        self.assertEqual(expected, actual)

    def test_get_tokens_of_topic(self):
        self.setUp()
        self.setUpChoices()
        bodies = get_articles_bodies_from_choices(Choice.objects.all())
        fd = FreqDist(get_tokens_of_topic(bodies))
        print fd.most_common()

    def test_get_article_bodies_from_choices(self):
        self.setUp()
        self.setUpChoices()
        choices = get_choices_of_topic(self.TOPIC_ID)

        expected = ["body one","body two","body three","body four"]
        actual = get_articles_bodies_from_choices(choices)
        self.assertEqual(expected, actual)
