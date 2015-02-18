from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField

class WordFrequency(models.Model):
    word = models.CharField(max_length=200)
    frequency = models.IntegerField()

class Topic(models.Model):
    topic = models.CharField(max_length=200)
    seeds = ListField(models.CharField(max_length=200))
    common_words = ListField(EmbeddedModelField('WordFrequency'))
