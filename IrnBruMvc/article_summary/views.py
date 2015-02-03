from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.template import RequestContext, loader

from topics_trainer.models import Article, Choice

def topics_summary(request):
    choice = Choice.objects.all()
    template = loader.get_template('topics_summary.html')
