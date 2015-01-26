from django.http import HttpResponse
from django.template import RequestContext, loader

from topics_trainer.models import Article
from topics_editor.models import Topic

def index(request):
    return HttpResponse('/topics_trainer/index for articles')

def article_choice(request, article_index):
    article = Article.objects.all()[int(article_index)]
    topics = Topic.objects.all()

    template = loader.get_template('article_choice.html')
    context = RequestContext(request, {
        'article': article,
        'topics': topics
    })

    return HttpResponse(template.render(context))

def update_topic(request, article_id):
    if request.POST:
        # Update database with the topics
        print request.POST.getlist('topics')
        return HttpResponse("Update")
    else:
        return HttpResponse("Get")


