from django.conf.urls import patterns, url

from factors_trainer import views

urlpatterns = patterns('factors_trainer', 
    url(r'update/$', views.update, name='index'),
    url(r'get_factor/(?P<topic_name>[\w|\W]+)/$', views.get_factors, name='get_factors'),
    url(r'update_factor/(?P<factor_id>.*)/$', views.update_factor, name='update_factor'),
    url(r'^$', views.index, name='index'),
    # Reporting
    url(r'report/(?P<topic_name>\w+)/(?P<sentiment>\w*)/$', views.report_topic_factor_sentiments, name='report_topic_factor_sentiments'),
    url(r'report/(?P<topic>\w+)/$', views.report_sentiments, name='report_sentiments'),
    url(r'report/$', views.report, name='report')
)

