# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.template import RequestContext, loader

from factors_trainer.factors import *

def index(request):
    template = loader.get_template('factors_trainer.html')
    context = RequestContext(request, {
        'sentence': 'Sentence'
        })

    update_factors()

    return HttpResponse(template.render(context))
