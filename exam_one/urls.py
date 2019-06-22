# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'exam_one.views',
    (r'^task/$', 'task'),
    (r'^test/$', 'test'),

    (r'^template/$', 'template'),
    (r'^template/create$', 'template_create'),
    (r'^template/list$', 'template_list'),
    (r'^template/delete/(\d+)$', 'template_delete'),
)
