from django.conf.urls import patterns, url

from factors_trainer import views

urlpatterns = patterns('factors_trainer', 
    url(r'^$', views.index, name='index'),
)

