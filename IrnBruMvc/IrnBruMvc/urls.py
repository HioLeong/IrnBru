from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    url(r'^topics_trainer/', include('topics_trainer.urls', namespace="topics_trainer")),
    url(r'^admin/', include(admin.site.urls)),
)
