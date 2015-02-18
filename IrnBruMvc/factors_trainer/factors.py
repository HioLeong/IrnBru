from topics_editor.models import Topic

def sent_contains_topic_common_words(sent, topic_name):
    common_words = Topic.objects.get(topic=topic_name).common_words
    # Document 0 being the highest rank, 1 being the lowest
    # TODO: if words exist - include the ranking
    for rank, val in enumerate(common_words):
        if val.word in sent:
            return True
        else:
            return False
