"""civiwiki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from api import urls_write, urls_read, urls_templates, urls_auth
from api.tests import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(urls_write)),
    url(r'^api/', include(urls_read)),
    url(r'^api/', include(urls_auth)),
    url(r'^test/',test_view)
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', serve, {
            'document_root': settings.STATIC_ROOT, 'show_indexes': True
        }),
        url(r'^media/(?P<path>.*)$',serve, {
            'document_root': settings.MEDIA_ROOT, 'show_indexes': True
        }),
   ]

urlpatterns += [
    url(r'',include(urls_templates)),
]
