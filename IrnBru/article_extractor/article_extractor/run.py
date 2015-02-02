from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from article_extractor.spiders.bbc import BbcSpider
from scrapy.utils.project import get_project_settings

spider = BbcSpider()
settings = get_project_settings()
crawler = Crawler(settings)
crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
crawler.configure()
crawler.crawl(spider)
crawler.start()
log.start()
reactor.run() 
