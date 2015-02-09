from django.conf.urls import patterns, url
# from django.views.generic import TemplateView
from mango import views

urlpatterns = patterns('',
    url(r'^index/', views.index, name='index'),
    url(r'^$', views.demo, name='demo'),
    url(r'^hello/', views.demo, name='demo'),
    # url(r'^mango/', IndexView.as_view(), name='index'),
    # url(r'^demo/', TemplateView.as_view(template_name="demo.html")),
    # url(r'^about/', AboutView.as_view()),
)