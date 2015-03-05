from django.test import TestCase

from topics_trainer.models import Article
from classifier.topics_classifier import *

class SimpleTest(TestCase):
    def test_get_word_occurence(self):
        article = Article(title='Article title', body=['Energy bills would go up in an independent Scotland because bill payers in the rest of the UK (rUK) would not want to continue subsidising the Scottish renewable sector. A third of the UK\'s renewable subsidy currently goes to Scotland, while Scots pay only one tenth of the cost.'])
        print get_word_occurence(article)
