from pymongo import MongoClient
import json

__project_dir__ = '../../res'

__topics__ = []
__client__ = MongoClient('127.0.0.1', 27017)
__db__ = __client__.fyp_db

__finished__ = "Finished"

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
    print "F to finish"

def __index_of_none__():
    _topics.index("None")

def __insert_topic_article_into_db__(topic_article):
    __db__.article_topic.insert(topic_article)

def get_topic(title,body,topic_article=__db__):
    display_options(title)
    try:
        topic_index = raw_input()
        if (topic_index == "f"):
            return __finished__
        else:
            return __topics__[int(topic_index)]['topic']
    except IndexError:
        print 'Index out of bound, try again'

def __get_topic_article_json__(title, topics):
    return {
            "title": title,
            "topics": topics
           }

def get_article(articles_dir):
    json_file = open(articles_dir)
    data = json.load(json_file)
    for art in data:
        title = art['title']
        body = art['body']
        if not __db__.article_topic.find_one({"title":title}):
            topics = []
            input_topic = ""
            while input_topic != __finished__ or input_topic == "none":
                input_topic = get_topic(title, body)
                if not input_topic == __finished__:
                    topics.append(input_topic)
            __insert_topic_article_into_db__(__get_topic_article_json__(title,topics))

def save_articles(articles_dir):
    json_file = open(articles_dir)
    data = json.load(json_file)
    for t in data:
        topic = t['topic']
        seeds = t['seeds']
        __db__.topics_editor_topic.insert({"topic": topic, "seeds":seeds})


def main():
    __init__()
    #get_article(__project_dir__ + '/bbcfactors.json')
    save_articles(__project_dir__ + '/topic.json')
    return

if __name__ == '__main__':
    main()
