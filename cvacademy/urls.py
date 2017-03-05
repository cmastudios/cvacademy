from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cvacademy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'cvacademy.views.home'),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^learn/', include('learn.urls')),
	url(r'^accounts/login/$',  login),
    url(r'^accounts/logout/$', logout),
)
