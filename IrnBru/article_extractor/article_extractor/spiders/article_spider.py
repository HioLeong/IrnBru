import scrapy
import json
from scrapy.selector import Selector
from scrapy.http import Request
from article_extractor.items import Article

class ArticleSpider(scrapy.Spider):
    name = ""
    allowed_domains = []
    start_urls = []
    def __init__(self):
        with open('starturl.json') as data_file:
            data = json.load(data_file)
            self.start_urls = data['start_urls']

    def getUrl(self, url):
        if url[0:2] == '/u':
            return 'https://www.google.com' + url
        else: 
            return ''

    def parse(self, response):
        f = open('test.html', 'w')
        f.write(response.body)
        f.close()
        hxs = Selector(response)

        for data in hxs.xpath('//h3/a/@href').extract():
            url = self.getUrl(data)
            if (len(url) > 1):
                yield Request(url, callback = self.parseArticle)

    def parseArticle(self, response):
        print '-------------------------------- Parsing Article --------------------------'
        print self.selections['date']
        hxs = Selector(response)
        item = Article()
        item['date'] = hxs.xpath(self.selections['date']).extract()

        item['title'] = hxs.xpath(self.selections['title']).extract()
        item['body'] = hxs.xpath(self.selections['body']).extract()
        item['source'] = self.name

        if len(item['body']) > 0:
            yield item

