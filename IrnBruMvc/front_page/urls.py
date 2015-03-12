from django.conf.urls import patterns, url

from front_page import views

urlpatterns = patterns('front_page', 
    url(r'^$', views.index, name='index')
)

