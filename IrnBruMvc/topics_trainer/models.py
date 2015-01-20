from django.db import models

from djangotoolbox.fields import ListField

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    def __unicode__(self):
        return self.title

class Choice(models.Model):
    choice = models.ForeignKey(Article)
    topic = ListField()

