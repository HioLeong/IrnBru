from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.template import RequestContext, loader

from topics_trainer.models import Article, Choice
from topics_editor.models import Topic

def index(request):
    return HttpResponse('/topics_trainer/index for articles')

def article_choice(request, article_index):
    article = Article.objects.all()[int(article_index)]
    topics = Topic.objects.all()

    template = loader.get_template('article_choice.html')

    try:
        choice = Choice.objects.get(choice=article)
        context = RequestContext(request, {
            'article': article,
            'topics': topics,
            'chosen_topics': choice.topic
        })
    except ObjectDoesNotExist:
        context = RequestContext(request, {
            'article': article,
        'topics': topics,
        })

    return HttpResponse(template.render(context))

def update_topic(request, article_id):
    if request.POST:
        topic_keys = request.POST.getlist('topics')
        currentarticle = Article.objects.get(id=article_id)
        try: 
            choice = Choice.objects.get(choice=currentarticle)
            choice.topic = topic_keys
            choice.save(force_update=True)
        except ObjectDoesNotExist:
            choice = Choice(choice=currentarticle, topic=topic_keys)
            choice.save()

        return HttpResponse("Update")
    else:
        return HttpResponse("Get")


