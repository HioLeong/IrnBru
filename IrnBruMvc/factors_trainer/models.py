from django.db import models
from djangotoolbox.fields import EmbeddedModelField

# Create your models here.
class Factor(models.Model):
    article = models.ForeignKey('topics_trainer.Article')
    topic = models.ForeignKey('topics_editor.Topic')
    factor = models.CharField(max_length=2000)
    sentiment = models.CharField(max_length=200)
