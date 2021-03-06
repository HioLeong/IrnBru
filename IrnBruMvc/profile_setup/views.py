from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import redirect

def index(request):
    template = loader.get_template('setup.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))
