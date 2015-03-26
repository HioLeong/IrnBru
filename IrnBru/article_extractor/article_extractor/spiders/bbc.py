import scrapy
import article_extractor
from scrapy.selector import Selector
from scrapy.http import Request
from article_extractor.items import Article

class BbcSpider(article_extractor.spiders.article_spider.ArticleSpider):
    name = "bbc"
    allowed_domains = ["bbc.co.uk","google.com","google.co.uk"]
    start_urls = [
        "https://www.google.com/search?q=site%3Abbc.co.uk+scottish+independence+factors&num=1000&tbs=cdr%3A1%2Ccd_min%3A%2Ccd_max%3A9%2F17%2F2014",
        "https://www.google.com/search?q=site%3Abbc.co.uk+scottish+devolution&num=1000&tbs=cdr%3A1%2Ccd_min%3A%2Ccd_max%3A9%2F17%2F2014",
        "https://www.google.com/search?q=site%3Abbc.co.uk+scottish+independence&num=1000&tbs=cdr%3A1%2Ccd_min%3A%2Ccd_max%3A9%2F17%2F2014"
    ]

    selections = {
            'date': '//span[@class="date"]/text()',
            'title': '//h1[@class="story-body__h1"]/text()',
            'body': '//div[@class="story-body__inner"]/p/text()'
            }
