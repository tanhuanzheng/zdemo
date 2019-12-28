from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<city>[a-z]+)/(?P<year>\d{4})$', views.index2)    # ?P<year>给分组起名字
]
