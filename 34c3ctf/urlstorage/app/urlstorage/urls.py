"""urlstorage URL Configuration

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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    url(r'^captcha/', include('captcha.urls')),
]
urlpatterns += [
    url(r'^$', views.login, name='login'),
    url(r'^urlstorage', views.index, name='index'),
    url(r'^flag$', views.flag, name='flag'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^contact/queue$', views.contact_queue, name='queue'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^.*$', views.notfound, name='notfound'),
]
urlpatterns += staticfiles_urlpatterns()
