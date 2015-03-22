from django.conf.urls import patterns, include, url
from django.contrib import admin
from accounts.views import login

urlpatterns = patterns('',
    url(r'^', include('backup.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^notes/', include('notes.urls', namespace='notes')),
    url(r'^login/$', login, name='home'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'home'}, name='logout'),
)

