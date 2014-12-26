import json
from pymongo import MongoClient

__project_dir__ = '../../res'

__topics__ = []
__client__ = MongoClient()
__db__ = __client__.projectdb

def load_topics():
    file = open(__project_dir__ + '/topic.json')
    data = json.load(file)
    for topic in data:
        __topics__.append(topic)

def __init__():
    load_topics()

def display_options(title=""):
    print title
    for i, topic in enumerate(__topics__):
        print str(i) + '. ' + topic['topic']

def __index_of_none__():
    _topics.index("None")

def get_topic(title,body,topic_article=__db__):
    display_options(title)
    try:
        topic_index = raw_input()
        topic = __topics__[int(topic_index)]['topic']
        __db__.article_topic.insert({"title":title, "topic":topic})
    except IndexError:
        print 'Index out of bound, try again'

def get_article(articles_dir):
    json_file = open(articles_dir)
    data = json.load(json_file)
    for art in data:
        title = art['title']
        body = art['body']
        if not __db__.article_topic.find_one({"title":title}):
            get_topic(title,body)

def main():
    __init__()
    get_article(__project_dir__ + '/bbcfactors.json')
    return

if __name__ == '__main__':
    main()
