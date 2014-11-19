import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

class Article(scrapy.Item):
    title = scrapy.Field()
    body = scrapy.Field()
        
class DmozSpider(scrapy.Spider):
    name = "bbc"
    allowed_domains = ["bbc.co.uk"]
    start_urls = [
        "http://www.bbc.co.uk/search?q=scottish+independence&sa_f=search-serp"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        hxs = HtmlXPathSelector(response)
        for url in hxs.xpath('//h1/a/@href').extract():
            yield Request(url, callback = self.parseArticle)

    def parseArticle(self, response):
        hxs = HtmlXPathSelector(response)
        item = Article()

        item['title'] = hxs.xpath('//h1[@class="story-header"]/text()').extract()
        item['body'] = hxs.select('//div[@class="story-body"]/p/text()').extract()

        yield item


