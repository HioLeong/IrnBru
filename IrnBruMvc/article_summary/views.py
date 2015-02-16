from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.template import RequestContext, loader

from topics_trainer.models import Article, Choice
from topics_editor.models import Topic
from article_summary.word_op import *

def topics_summary(request):
    choice = Choice.objects.all()
    template = loader.get_template('topic_summary.html')
    topics = Topic.objects.all()
    content = []

    # Need to refactor this to update elsewhere
    for t in topics:
        topic_name = t.topic
        choices = get_choices_of_topic(t.id)
        article_bodies = get_articles_bodies_from_choices(choices)
        bodies_toks = get_tokens_of_topic(article_bodies)
        freq_dist = get_freqdist_of_toks(bodies_toks).most_common(50)

        content.append({'topic': topic_name, 'freqdist': freq_dist})

    context = RequestContext(request, {
        'content': content
        })

    return HttpResponse(template.render(context))
