from django.conf.urls import patterns, url

from article_summary import views

urlpatterns = patterns('article_summary',
        url(r'^$', views.topics_summary, name='article_summary')
        )
