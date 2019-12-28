from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index_one),
    url(r'^index_two/$', views.index_two, name='two'),
]