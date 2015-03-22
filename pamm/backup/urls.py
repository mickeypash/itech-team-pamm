from django.conf.urls import patterns, url
# from django.views.generic import TemplateView
from backup import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
)