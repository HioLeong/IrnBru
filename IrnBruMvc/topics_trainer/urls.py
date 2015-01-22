from django.conf.urls import patterns, url

from topics_trainer import views

urlpatterns = patterns('', 
    url(r'^$', views.index, name='index'),
    url(r'^(?P<article_index>\d+)/$', views.article_choice, name='article_choice')
)

