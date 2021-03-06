import scrapy
import article_extractor
from scrapy.selector import Selector
from scrapy.http import Request
from article_extractor.items import Article

class GuardianSpider(article_extractor.spiders.article_spider.ArticleSpider):
    name = "guardian"
    allowed_domains = ["theguardian.com","google.com","google.co.uk"]
    #start_urls = [
        #"https://www.google.com/search?q=site%3Atheguardian.com+scottish+independence+factors&num=1000&tbs=cdr%3A1%2Ccd_min%3A%2Ccd_max%3A9%2F17%2F2014",
        #"https://www.google.com/search?q=site%3Atheguardian.com+scottish+devolution&num=1000&tbs=cdr%3A1%2Ccd_min%3A%2Ccd_max%3A9%2F17%2F2014"
    #]

    selections = { 
            'date': '//span[@class="date"]/text()', 
            'title': '//h1[@class="content__headline js-score"]/text()', 
            'body': '//div[@class="content__article-body from-content-api js-article__body"]/p/text()' 
            }
