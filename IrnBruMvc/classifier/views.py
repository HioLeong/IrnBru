from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import redirect
from nltk.tokenize import *

from topics_trainer.models import Article

from classifier.topics_classifier import *
from classifier.factors_classifier import *

import collections


def index(request):
    template = loader.get_template('factors_classification.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def get_article_classification(article):
    classifier = TopicsClassifier()
    body = sent_tokenize(article)
    article_obj = Article(title='', body=body)
    return classifier.classify(article_obj)

def get_classify_distribution(dist):
    data = []
    for label in dist.samples():
        percent = int(100*(round(dist.prob(label),2)))
        data.append({'label':label, 
        'value': dist.prob(label), 
        'percent': percent
        })
        print('%s: %f' % (label, dist.prob(label)))
    return sorted(data, key=lambda dist:dist['value'], reverse=True)

def classify_article(request):
    if request.POST:
        article = __get_article__(request)
        dist = get_article_classification(article)
        data = get_classify_distribution(dist)
        print data
        template = loader.get_template('classification_report.html')
        context = RequestContext(request, { 'data': data })
        return HttpResponse(template.render(context))
    else:
        return HttpResponse('No data')

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
    #TODO: Implement
    return ''

def __get_article_text__(article_text):
    return article_text
