from django.http import HttpResponse
from django.template import RequestContext, loader

from topics_trainer.models import Article

def index(request):
    return HttpResponse('/topics_trainer/index for articles')

def article_choice(request, article_index):

    article = Article.objects.all()[int(article_index)]
    template = loader.get_template('article_choice.html')
    context = RequestContext(request, {
        'article': article
    })

    return HttpResponse(template.render(context))
