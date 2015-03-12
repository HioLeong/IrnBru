from django.conf.urls import patterns, url

from front_pageimport views

urlpatterns = patterns('factors_trainer', 
    url(r'^$', views.index, name='index')
)

