import string
import nltk
from nltk import NaiveBayesClassifier
from nltk.util import ngrams
from nltk.featstruct import FeatStruct

from topics_editor.models import Topic
from factors_trainer.factors import *
from factors_trainer.models import Factor

class FactorsClassifier:
    def __init__(self, topic_name):
        topic = Topic.objects.get(topic=topic_name)
        self.train_set = self.get_train_set(topic)
        print self.train_set
        self.classifier = self.train_factor_classifier(self.train_set)

    def __get_pos_pattern_from_factor__(self, factor):
        sentence = factor.factor
        pos_tags = get_pos_tag_of_sentence(sentence)
        pos_pattern = aggregate_pos_tags(pos_tags)
        return pos_pattern

    def get_train_set(self, topic):
        topic_factors = Factor.objects.filter(topic=topic)
        # Does not take into consideration Neutrals
        sentiment_factors  = [factor for factor in topic_factors if factor.sentiment in ['Yes','No']]
        train_set = [(self.factor_features(factor),factor.sentiment) for factor in sentiment_factors]
        return train_set

    def factor_features(self, factor):
        word_freq = get_factor_word_list(factor)
        word_freq_feat = FeatStruct(word_freq)
        word_freq_feat.freeze()
        #pos_pattern = self.__get_pos_pattern_from_factor__(factor)
        #pat_feat = FeatStruct(pattern=pos_pattern)
        #pat_feat.freeze()
        feature = FeatStruct(words=word_freq_feat)
        feature.freeze()
        return feature

    def classify(self, factor):
        return self.classifier.classify(factor)

    def accuracy(self):
        return nltk.classify.accuracy(self.classifier, self.train_set)

    def train_factor_classifier(self, train_set):
        classifier = NaiveBayesClassifier.train(train_set)
        return classifier

    def show_most_informative_features(self):
        print self.classifier.show_most_informative_features()

    def test(self):
        print self.accuracy()
        print self.show_most_informative_features()

