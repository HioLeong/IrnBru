from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField

from topics_editor.models import Topic

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = ListField(models.CharField(models.TextField()))

class Choice(models.Model):
    choice = models.ForeignKey(Article)
    topic = ListField(models.CharField(max_length=200))
