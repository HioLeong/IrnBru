from django.conf.urls import patterns, url

from factors_trainer import views

urlpatterns = patterns('factors_trainer', 
    url(r'update/$', views.index, name='index'),
    url(r'(?P<topic_name>\w+)/$', views.get_factors, name='get_factors'),
)

