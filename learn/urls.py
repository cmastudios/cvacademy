from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<lesson_id>\d+)/$', views.lesson, name='lesson'),
    url(r'^compile/$', views.compile, name='compile'),
]