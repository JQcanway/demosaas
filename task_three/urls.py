# -*- coding: utf-8 -*-

from django.conf.urls import patterns


urlpatterns = patterns(
    'task_three.views',
    (r'^$', 'home'),
    (r'^monitor_list/$', 'monitor_list'),
    (r'^delete/(\d+)$', 'monitor_delete'),
)
