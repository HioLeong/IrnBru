from django.conf.urls import patterns, url

from topics_trainer import views

urlpatterns = patterns('', 
    url(r'^$', views.index, name='index')
)
