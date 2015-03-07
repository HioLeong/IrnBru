import string
from nltk import NaiveBayesClassifier
from nltk.featstruct import FeatStruct


class FactorsClassifier():
    def __init__(self):
        self.train_set = self.get_train_set()
        self.classifier = train_factor_classifier(self.train_set)

    def get_train_set(self):
        return []

    def factor_features(self, factor):
        feat
        return

    def train_factor_classifier(self, train_set):
        classifier = NaiveBayesClassifier
        return
