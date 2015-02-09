from django.db import models

from djangotoolbox.fields import ListField

# Create your models here.
class Topic(models.Model):
    topic = models.CharField(max_length=200)
    seeds = ListField(models.CharField(max_length=200))
