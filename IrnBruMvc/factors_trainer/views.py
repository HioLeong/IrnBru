# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.template import RequestContext, loader

from factors_trainer.factors import *
from topics_editor.models import Topic

def get_factors(request, topic_name):
    template = loader.get_template('factors_list.html')
    topic = Topic.objects.get(topic = topic_name)
    factors = get_factors_for_topic(topic)
    context = RequestContext(request, {
        'factors': factors
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
