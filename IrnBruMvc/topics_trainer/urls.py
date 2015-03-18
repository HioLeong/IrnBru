from django.conf.urls import patterns, url

from topics_trainer import views

urlpatterns = patterns('topics_trainer', 
    url(r'^(?P<article_id>.*)/update_topic/$', views.update_topic, name='update_topic'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<article_id>\w+)/$', views.article_choice, name='article_choice')
)

