from django.conf.urls import patterns, url
from eventapp import views


urlpatterns = patterns('',  # events/
                       url(r'^$', views.index, name='index'),
                       # url(r'^(?P<user_id>\d+)/$', views.userdetail, name='userdetail'),
                       url(r'^login/$', "django.contrib.auth.views.login", name='login'),
                       url(r'^login_success/$', views.login_success, name='login_success'),
                       url(r'^register/$', views.register, name='register'),
                       #url(r'^profile/$', views.edit_profile, name='profile'),
                       url(r'^regis_success/$', views.regis_success, name='success'),
                       url(r'^edit_success/$', views.edit, name='edit_success'),
                       url(r'^update/$', views.update, name='update'),
                       #url(r'^(?P<user_id>\d+)/results/$', views.results, name='results'),
)