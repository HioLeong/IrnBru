from django.conf.urls import patterns, url

from front_page import views

urlpatterns = patterns('front_page', 
    url(r'^$', views.index, name='index'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^dashboard/topics_articles_count/$', views.get_topics_articles_count, name='topics_articles_count'),
    url(r'^dashboard/factors_count/$', views.get_factors_count, name='factors_count'),
    url(r'^dashboard/get_all_data/$', views.get_all_data, name='get_all_data'),
)

