from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    template = loader.get_template('factors_classification.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def classify_article(request, article_type):
    return HttpResponse(article_type)
