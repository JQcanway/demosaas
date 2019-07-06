# -*- coding: utf-8 -*-

from django.conf.urls import patterns


urlpatterns = patterns(
    'data_preparation.views',
    (r'^$', 'home'),
    #获取业务
    (r'^search_biz/$', 'search_biz'),
    #获取主机
    (r'^search_host/(\d+)$', 'search_host'),
    #查询用户
    (r'^search_users/$', 'search_users'),

    #查询考试列表
    (r'^add$', 'add'),
    (r'^upload$', 'upload'),
    #查询考试列表
    (r'^list$', 'list'),
    # 查询主机详情
    (r'^one/(\d+)$', 'one'),
    # 查询考试删除
    (r'^delete/(\d+)$', 'delete'),
)
