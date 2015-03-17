from django.conf.urls import patterns, url

from front_page import views

urlpatterns = patterns('front_page', 
    url(r'^$', views.index, name='index'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^dashboard/topics_articles_count/$', views.get_topics_articles_count, name='topics_articles_count'),
)

