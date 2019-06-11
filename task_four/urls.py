# -*- coding: utf-8 -*-

from django.conf.urls import patterns


urlpatterns = patterns(
    'task_four.views',
    (r'^center/$', 'home1'),
    (r'^center/create$', 'create_center'),
    (r'^center/list$', 'create_list'),


    (r'^template/$', 'home2'),
    (r'^template/upload$', 'upload_file'),
    (r'^template/create$', 'create_template'),
    (r'^template/list$', 'template_list'),

    (r'^commission/list/(\d+)$', 'commission_list'),
    (r'^commission/finish/(\d+)/(\d+)$', 'commission_finish'),
)
