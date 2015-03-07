import string
from nltk import NaiveBayesClassifier
from nltk.featstruct import FeatStruct

from factors_trainer.factor import *

class FactorsClassifier():
    def __init__(self):
        self.train_set = self.get_train_set()
        self.classifier = train_factor_classifier(self.train_set)

    def __get_pos_pattern_from_factor__(self, factor):
        sentence = factor.factor
        pos_tags = get_pos_tag_of_sentence(sentence)
        pos_pattern = aggregate_pos_tags(pos_tags)
        return pos_pattern

    def get_train_set(self):
        return []

    def factor_features(self, factor):
        pos_pattern = self.__get_pos_pattern_from_factor__(factor)
        return { 'pos_pattern': pos_pattern }

    def train_factor_classifier(self, train_set):
        classifier = NaiveBayesClassifier
        return
