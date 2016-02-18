# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('myproject.myapp.views',
    url(r'^list/$', 'list', name='list'),
    url(r'^clean/$', 'clean', name='clean'),
    url(r'^delete/(.*?)/$', 'delete', name='delete'),

)
