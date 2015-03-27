from scrapy.exceptions import DropItem
from pymongo import MongoClient
import json

client = MongoClient('127.0.0.1', 27017)
db = client.fyp_db
collection = db.topics_trainer_article_new

class ArticleExtractorPipeline(object):
    def process_item(self, item, spider):
        if not collection.find_one({"title": item.get('title')}):
            collection.insert(dict(item))
            return item
        else:
            raise DropItem('Article with title already exists: %s' % item)
