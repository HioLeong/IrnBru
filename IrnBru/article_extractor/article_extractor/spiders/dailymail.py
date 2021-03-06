import scrapy
import article_extractor
from scrapy.selector import Selector
from scrapy.http import Request
from article_extractor.items import Article

class DailyMailSpider(article_extractor.spiders.article_spider.ArticleSpider):
    name = "dailymail"
    allowed_domains = ["dailymail.co.uk","google.com","google.co.uk"]
    #start_urls = [
        #"https://www.google.com/search?q=site%3Adailymail.co.uk+scottish+referendum&num=1000&tbs=cdr%3A1%2Ccd_min%3A%2Ccd_max%3A9%2F17%2F2014"
    #]

    selections = { 
            'date': '//span[@class="article-timestamp article-timestamp-published"]/text()',
            'title': '//div[@id="js-article-text"]/h1/text()',
            'body': '//div[@id="js-article-text"]/p[@class="mol-para-with-font"]/font/text()'
            }
