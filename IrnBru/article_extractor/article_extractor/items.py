import scrapy

class Article(scrapy.Item):
    title = scrapy.Field()
    body = scrapy.Field()
    date = scrapy.Field()
    author = scrapy.Field()
    source = scrapy.Field()

