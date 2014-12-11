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

def display_options():
    for i, topic in enumerate(__topics__):
        print str(i) + '. ' + topic['topic']
    print 'x. if no topic'

def print_array(texts):
    for text in texts:
        print text

def get_topic(title,body,topic_articles=__db__.topic_articles):
    print '************************************************'
    print_array(title)
    print_array(body)
    display_options()
    try:
        topic_index = int(raw_input())
        if topic_index >= 0 | topic_index < 7:
            topic = __topics__[int(topic_index)]['topic']
        else:
            topic = 'none'
        topic_article = { 'topic': topic, 'title': title, 'body': body}
        print topic_article
        topic_articles.insert(topic_article)
    except IndexError:
        print 'Index out of bound, try again'

def get_article(articles_dir):
    json_file = open(articles_dir)
    data = json.load(json_file)
    for art in data:
        title = art['title']
        body = art['body']
        get_topic(art,body)

def main():
    __init__()
    get_article(__project_dir__ + '/bbcfactors.json')
    return

if __name__ == '__main__':
    main()
