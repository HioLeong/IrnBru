import string
import nltk
from nltk import NaiveBayesClassifier
from nltk.featstruct import FeatStruct

from article_summary.word_op import *
from topics_trainer.models import Article
from topics_editor.models import Topic


class TopicsClassifier:
    def __init__(self):
        self.train_set = self.get_train_set()
        self.classifier = self.train_topic_classifier(self.train_set)

    def get_train_set(self):
        label_topic = []
        for topic in Topic.objects.all():
            topic_choices = get_choices_of_topic(topic.id)
        for choice in topic_choices:
            article = get_article_from_choice(choice)
            label_topic.append((article, topic.topic))
        train_set = [(self.topic_features(n), topic) for (n,topic) in label_topic]
        return train_set

    def get_test_set(self):
        label = topic

    def get_word_occurence(self, article):
        body_toks = aggregate_list_of_lists([word_tokenize(b) for b in article.body])
        toks = [t.lower() for t in body_toks]
        filtered_toks = [t for t in toks if not t in get_stopwords()]
        filtered_toks = [t for t in filtered_toks if not t in string.punctuation]
        freqdist = get_freqdist_of_toks(filtered_toks)
        return freqdist.most_common(len(filtered_toks))

    def topic_features(self, article):
        word_occurence = self.get_word_occurence(article)
        feature_list = FeatStruct(word_occurence)
        feature_list.freeze()
        feature = FeatStruct(word_occurence=feature_list)
        feature.freeze()
        return feature

    def train_topic_classifier(self, train_set):
        classifier = NaiveBayesClassifier.train(train_set)
        return classifier

    def classify(self, article):
        return classifier.classify(article)

    def get_classifier_accuracy(self, classifier, train_set):
        return nltk.classify.accuracy(classifier, train_set)

    def test():
        t_set = self.get_train_set()
        classifier = self.train_topic_classifier(t_set)
        self.get_classifier_accuracy(classifier, t_set)
