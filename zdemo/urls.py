"""zdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import users.urls

urlpatterns = [
    url(r'^$', include('bweather.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include(users.urls)),
    url(r'^bweather/', include('bweather.urls')),
    url(r'^cqs/', include('cqs.urls')),
    url(r'^dformdt/', include('dformdt.urls')),
    url(r'^enoneformdt/', include('enoneformdt.urls')),
    url(r'^fmetadt/', include('fmetadt.urls')),
    url(r'^grespon/', include('grespon.urls')),

]
