from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
     #url(r'^$', '.views.index', name='index'),
    url(r'^events/', include('eventapp.urls', namespace="events")),

    url(r'^admin/', include(admin.site.urls)),
)
