from django.conf.urls import patterns, url

from factors_trainer import views

urlpatterns = patterns('factors_trainer', 
    url(r'update/$', views.index, name='index'),
    url(r'report/$', views.report, name='index'),
    url(r'get_factor/(?P<topic_name>\w+)/$', views.get_factors, name='get_factors'),
    url(r'update_factor/(?P<factor_id>.*)/$', views.update_factor, name='update_factor'),
)

