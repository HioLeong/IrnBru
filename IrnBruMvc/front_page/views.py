from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def dashboard(request):
    template = loader.get_template('dashboard.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))
