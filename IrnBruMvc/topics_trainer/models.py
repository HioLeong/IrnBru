from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = ListField(models.CharField(models.TextField()))
    source = models.CharField(max_length=200)

class Choice(models.Model):
    choice = models.ForeignKey(Article)
    topic = ListField(models.CharField(max_length=200))
