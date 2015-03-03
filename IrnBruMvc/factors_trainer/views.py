# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.template import RequestContext, loader

from factors_trainer.factors import *
from topics_editor.models import Topic

def get_factors(request, topic_name):
    template = loader.get_template('factors_list.html')
    topic = Topic.objects.get(topic = topic_name)
    factors = [factor for factor in get_factors_for_topic(topic) if factor.sentiment != '']
    context = RequestContext(request, {
        'factors': factors,
        'topic_name': topic_name.title()
        })
    return HttpResponse(template.render(context))

def update(request):
    update_factors()
    return HttpResponse('Updated')

def index(request):
    template = loader.get_template('factors_trainer.html')
    context = RequestContext(request, {
        'sentence': 'Sentence'
        })

    update_factors()
    return HttpResponse(template.render(context))

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
