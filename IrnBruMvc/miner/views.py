import os
import json

from django.http import HttpResponse
from django.template import RequestContext, loader
from string import Template

def index(request):
    template = loader.get_template('miner.html')
    miners = ['bbc', 'guardian', 'scotsman', 'dailymail']
    context = RequestContext(request, {
        'miners': miners
        })
    return HttpResponse(template.render(context))

def mine(request):
    miner_domain_map = {'bbc':'bbc.co.uk', 'guardian':'theguardian.com', 'dailymail':'dailymail.co.uk', 'scotsman':'scotsman.com'}
    if request.POST:
        path = '/Users/Home/FinalYearProject/IrnBru/article_extractor/article_extractor/spiders'
        source = request.POST['source']
        keywords = request.POST['keywords']
        keywords = keywords.replace(' ','+')
        template = Template('https://www.google.com/search?q=site%3A$domain+$keywords&num=1000&tbs=cdr%3A1%2Ccd_min%3A%2Ccd_max%3A9%2F17%2F2014')
        start_urls = [template.substitute(domain=miner_domain_map[source], keywords=keywords)]
        with open(path+'/starturl.json','w') as data_file:
            data = {'start_urls': start_urls}
            data_file.write(json.dumps(data, data_file))
        current_path = os.getcwd()
        os.chdir(path)
        os.system('scrapy crawl ' + source)
        os.chdir(current_path)
        return HttpResponse(start_urls)
    else:
        return HttpResponse('fail')
