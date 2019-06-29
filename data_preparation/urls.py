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
    (r'^exam_add$', 'exam_add'),
    (r'^exam_upload$', 'exam_upload'),
    #查询考试列表
    (r'^exam_list$', 'exam_list'),
    # 查询考试详情
    (r'^exam_one/(\d+)$', 'exam_one'),
    # 查询考试删除
    (r'^exam_delete/(\d+)$', 'exam_delete'),
)
