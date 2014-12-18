from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'pages.views.home', name='home'),
    url(r'^graph$', 'pages.views.graph', name='graph'),
    url(r'^(?P<teacher_id>\d+)$', 'pages.views.teacherinfo', name='teacherinfo'),
    url(r'^admin/', include(admin.site.urls)),
)
