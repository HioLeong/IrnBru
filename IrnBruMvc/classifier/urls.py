from django.conf.urls import patterns, url

from classifier import views

urlpatterns = patterns('classifier', 
    url(r'^$', views.index, name='index')
)

