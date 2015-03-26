from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^topics_trainer/', include('topics_trainer.urls', namespace="topics_trainer")),
    url(r'^factors_trainer/', include('factors_trainer.urls', namespace="factors_trainer")),
    url(r'^article_summary/', include('article_summary.urls', namespace="article_summary")),
    url(r'^', include('front_page.urls', namespace="front_page")),
    url(r'^classifier/', include('classifier.urls', namespace="classifier")),
    url(r'^profile_setup/', include('profile_setup.urls', namespace='profile_setup')),
    url(r'^miner/', include('miner.urls', namespace='miner')),
    url(r'^admin/', include(admin.site.urls)),
)
