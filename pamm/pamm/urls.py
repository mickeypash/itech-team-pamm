from django.conf.urls import patterns, include, url
from django.contrib import admin
from notes.views import home

urlpatterns = patterns('',
    url(r'^$', home, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^notes/', include('notes.urls', namespace='notes')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    #url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'index'}, name='logout'),
    #url(r'^(?P<folder_name_slug>\w+)', folder, name='folder'),
)