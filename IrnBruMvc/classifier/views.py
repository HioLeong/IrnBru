from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import redirect

import collections

def index(request):
    template = loader.get_template('factors_classification.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def __get_article__(request):
    article_type_map = {
            'article-text': __get_article_text__,
            'article_url': __get_article_url__,
            'article_file': __get_article_file__
            }
    article_type = request.POST['article-type']
    return article_type_map[article_type](request.POST[article_type])

def __get_article_url__(article_url):
    #TODO: Implement
    return ''

def __get_article_file__(article_file):
    return ''

def __get_article_text__(article_text):
    return article_text

def classify_article(request):
    if request.POST:
        article = __get_article__(request)
        print article
        template = loader.get_template('factors_classification.html')
        context = RequestContext(request, {})
        return HttpResponse(template.render(context))
    else:
        return HttpResponse('No data')

