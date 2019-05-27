# -*- coding: utf-8 -*-

from django.conf.urls import patterns


urlpatterns = patterns(
    'task_two.views',
    (r'^$', 'home'),
    (r'^business/$', 'get_business'),
    (r'^host/(\d+)$', 'get_host'),
    (r'^script/$', 'get_script'),
    (r'^exec_script/$', 'exec_script'),
    (r'^monitor/$', 'monitor'),

)
