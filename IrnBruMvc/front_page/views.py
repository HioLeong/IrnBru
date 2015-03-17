from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.template import RequestContext, loader

from topics_trainer.models import Article, Choice
from factors_trainer.models import Factor
from topics_editor.models import Topic

import json

def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def dashboard(request):
    template = loader.get_template('dashboard.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def get_topics_articles_count(request):
    data = []
    topics  = Topic.objects.all()
    for topic in topics:
        topic_count = Choice.objects.filter(topic__contains=topic.id).count()
        data.append({'label': topic.topic.title(),
            'value': topic_count})
    return HttpResponse(json.dumps(data), content_type='application/json')

def get_factors_count(request):
    data = []
    topics = Topic.objects.all()
    for topic in topics:
        factors_count = Factor.objects.exclude(sentiment='').filter(topic=topic).count()
        data.append({'label':topic.topic, 'value': factors_count})
    return HttpResponse(json.dumps(data), content_type='application/json')
