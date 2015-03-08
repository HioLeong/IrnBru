# Create your views here.

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.template import RequestContext, loader

from factors_trainer.factors import *
from topics_editor.models import Topic

def index(request):
    template = loader.get_template('topics_factors_list.html')
    topics = Topic.objects.all()
    context = RequestContext(request, {
        'topics': topics
        })
    return HttpResponse(template.render(context))


def get_factors(request, topic_name):
    template = loader.get_template('factors_list.html')
    topic = Topic.objects.get(topic = topic_name)
    factors = [factor for factor in get_factors_for_topic(topic) if factor.sentiment == '']
    context = RequestContext(request, {
        'factors': factors,
        'topic_name': topic_name.title()
        })
    return HttpResponse(template.render(context))

def report_sentiment(request, topic_name, sentiment):
    topic = Topic.objects.get(topic=topic_name)
    template = loader.get_template('report.html')
    factors = get_factors_with_sentiment(sentiment)
    topic_factors = [factor for factor in factors if factor.topic == topic]
    context = RequestContext(request, {
        'factors': topic_factors,
        'sentiment': sentiment
        })
    return HttpResponse(template.render(context))

def report(request):
    return HttpResponse('response')

def update(request):
    update_factors()
    return HttpResponse('Updated')

def update_factor(request, factor_id):
    factor = Factor.objects.get(id=factor_id)
    if request.POST:
        try:
            sentiment = request.POST['sentiment']
        except KeyError:
            sentiment = ''
        factor.sentiment = sentiment
        factor.save()
        return HttpResponse(sentiment)
    else:
        return HttpResponse('Not updated')
