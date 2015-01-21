from django.http import HttpResponse
from django.template import RequestContext, loader

from topics_trainer.models import Article

def index(request):
    article = Article.objects.all()[0]
    template = loader.get_template('article_choice.html')
    context = RequestContext(request, {
        'article': article
    })

    return HttpResponse(template.render(context))
