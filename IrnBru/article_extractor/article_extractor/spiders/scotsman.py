import scrapy
import article_extractor
from scrapy.selector import Selector
from scrapy.http import Request
from article_extractor.items import Article

class Scotsman(article_extractor.spiders.article_spider.ArticleSpider):
    name = "scotsman"
    allowed_domains = ["scotsman.com","google.com","google.co.uk"]
    start_urls = [
        "https://www.google.com/search?q=site%3Ascotsman.com+scottish+independence+factors&num=1000&tbs=cdr%3A1%2Ccd_min%3A%2Ccd_max%3A9%2F17%2F2014",
        "https://www.google.com/search?q=site%3Ascotsman.com+scottish+independence+defence&num=1000&tbs=cdr%3A1%2Ccd_min%3A%2Ccd_max%3A9%2F17%2F2014"
        "https://www.google.com/search?q=site%3Ascotsman.com+scottish+independence+culture&num=1000&tbs=cdr%3A1%2Ccd_min%3A%2Ccd_max%3A9%2F17%2F2014"
    ]

    selections = {
            'date': '//span[@class="timestamp__date"]/text()',
            'title': '//h1[@class="article__title"]/text()',
            'body': '//section[@class="article-content article__content KonaBody"]/p/text()'
            }
