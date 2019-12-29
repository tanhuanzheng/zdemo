from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^hr$', views.hrespon),
    url(r'^jr$', views.jrespon),
    url(r'^rd$', views.rdirect),
    url(r'^ck$', views.cookie_index),
]
