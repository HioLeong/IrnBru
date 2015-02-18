from django.db import models
from djangotoolbox.fields import EmbeddedModelField

from topics_editor.models import Topic

# Create your models here.
class Factor(models.Model):
    topic = EmbeddedModelField('Topic')
    factor = models.CharField(max_length=2000)
    # Stay/Independent/Neutral
    sentiment = models.CharField(max_length=200)
