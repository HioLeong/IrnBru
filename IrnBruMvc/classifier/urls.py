from django.conf.urls import patterns, url

from classifier import views

urlpatterns = patterns('classifier', 
    url(r'^$', views.index, name='index'),
    url(r'classify_article/$', views.classify_article, name='classify_article')
)

