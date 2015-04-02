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
    factors_identified_count = Factor.objects.exclude(sentiment='').count();
    articles_count = Article.objects.count()
    articles_identified_count = Choice.objects.count()
    context = RequestContext(request, {
        'articles_count': articles_count,
        'factors_identified_count': factors_identified_count,
        'articles_identified_count': articles_identified_count
        })
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

def crop_sent_if_over_n(sent,n=150):
    if len(sent) > n:
        return sent[:n] + '...'
    else:
        return sent

def get_sentiments_tree_from_factors(factors):
    sentiments = ['Yes', 'No', 'Neutral']
    sentiment_tree = []
    for s in sentiments:
        root = {'name':s }
        sentiment_factor = [f for f in factors if f.sentiment == s]
        print sentiment_factor
        root['children'] = [{'name':crop_sent_if_over_n(f.factor,150),'sentiment':s} for f in sentiment_factor]
        sentiment_tree.append(root)
    return sentiment_tree

def get_all_data(request):
    tree = { 'name':'data' }
    tree_child = []
    topics = Topic.objects.all()
    for topic in topics:
        topic_root = { 'name': topic.topic }
        factors = Factor.objects.filter(topic=topic)
        topic_root['children'] = get_sentiments_tree_from_factors(factors)
        tree_child.append(topic_root)
    tree['children'] = tree_child
    return HttpResponse(json.dumps(tree), content_type='application/json')
