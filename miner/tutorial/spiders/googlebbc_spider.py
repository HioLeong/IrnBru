import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from tutorial.items import Article

class BbcSpider(scrapy.Spider):
    name = "bbcgoog"
    allowed_domains = ["bbc.co.uk","google.com","google.co.uk"]
        #"https://www.google.com/search?q=site%3Abbc.co.uk+scottish+independence+referendum&num=1000&tbs=cdr%3A1%2Ccd_min%3A%2Ccd_max%3A9%2F17%2F2014"
    start_urls = [
        "https://www.google.com/search?q=site%3Abbc.co.uk+scottish+independence+factors&num=1000&tbs=cdr%3A1%2Ccd_min%3A%2Ccd_max%3A9%2F17%2F2014"
    ]
    articleList = []

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
            print url
            if (len(url) > 1):
                yield Request(url, callback = self.parseArticle)

    def parseArticle(self, response):
        hxs = Selector(response)
        item = Article()
        item['date'] = hxs.xpath('//span[@class="date"]/text()').extract()

        item['title'] = hxs.xpath('//h1[@class="story-header"]/text()').extract()
        item['body'] = hxs.xpath('//div[@class="story-body"]/p/text()').extract()

        if len(item['body']) > 0:
            yield item

