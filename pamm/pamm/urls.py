from django.conf.urls import patterns, include, url
from django.contrib import admin
from noted.views import home_view

urlpatterns = patterns('',
    url(r'^', include('notes.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^notes/', include('noted.urls', namespace='notes')),
    url(r'^login/$', home_view, name='home'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'home'}, name='logout'),
)

