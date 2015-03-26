# -*- coding: utf-8 -*-

# Scrapy settings for article_extractor project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'article_extractor'

SPIDER_MODULES = ['article_extractor.spiders']
NEWSPIDER_MODULE = 'article_extractor.spiders'

ITEM_PIPELINES = {
        'article_extractor.pipelines.ArticleExtractorPipeline': 100,
        #'scrapy_mongodb.MongoDBPipeline': 200
}

MONGODB_URI = 'mongodb://127.0.0.1:27017'
MONGODB_DATABASE = 'fpy_db'
MONGODB_COLLECTION = 'topics_trainer_article'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'article_extractor (+http://www.yourdomain.com)'

