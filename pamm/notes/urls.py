from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import index, add_note, add_tag, note_content

urlpatterns = patterns('',
	url(r'^$', index, name='index'),
	url(r'^addnote/$', add_note, name='addnote'),
	url(r'^addtag/$', add_tag, name='addtag'),
	url(r'^note/$', note_content, name='note'),
	)