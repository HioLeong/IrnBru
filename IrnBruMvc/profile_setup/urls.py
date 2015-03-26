from django.conf.urls import patterns, url

from profile_setup import views

urlpatterns = patterns('profile_setup', 
    url(r'^$', views.index, name='index'),
)

