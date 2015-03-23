from django.conf.urls import patterns, include, url
from django.contrib import admin
from accounts.views import *


urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^notes/', include('notes.urls', namespace='notes')),
    # url(r'^register/', register, name='register'),
    # url(r'^login/', user_login, name='login'),
    # url(r'^logout', user_logout, name='logout'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    #url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'index'}, name='logout'),
    #url(r'^(?P<folder_name_slug>\w+)', folder, name='folder'),
)