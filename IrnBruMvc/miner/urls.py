from django.conf.urls import patterns, url

from miner import views

urlpatterns = patterns('miner', 
    url(r'^$', views.index, name='index'),
    url(r'mine/$', views.mine, name='mine')
)

