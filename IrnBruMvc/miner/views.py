from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    template = loader.get_template('miner.html')
    miners = ['bbc', 'guardian', 'scotsman', 'dailymail']
    context = RequestContext(request, {
        'miners': miners
        })
    return HttpResponse(template.render(context))

def mine(request):
    if request.POST:
        source = request.POST['source']
        keywords  = request.POST['keywords']
        return HttpResponse('success')
    else:
        return HttpResponse('fail')
