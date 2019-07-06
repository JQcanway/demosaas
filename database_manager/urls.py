# -*- coding: utf-8 -*-

from django.conf.urls import patterns


urlpatterns = patterns(
    'database_manager.views',
    (r'^custom/$', 'custom_home'),
    #添加
    (r'^custom/add$', 'add'),
    #查询考试列表
    (r'^custom/list$', 'list'),
    # 查询考试删除
    (r'^custom/delete/(\d+)$', 'delete'),
)
