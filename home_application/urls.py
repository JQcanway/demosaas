# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'home_application.views',
    (r'^test$', 'test'),
    (r'^$', 'home'),
    (r'^dev-guide/$', 'dev_guide'),
    (r'^contactus/$', 'contactus'),
    (r'^test$', 'test'),
    (r'^modal/$', 'modal'),
    (r'^api/getJson/$', 'getJson'),
    (r'^api/getEchartsJson/$', 'getEchartsJson'),

    (r'^search_biz/$', 'search_biz'),
    (r'^search_set/$', 'search_set'),
    (r'^search_host/$', 'search_host'),
    (r'^fast_execute_script/$', 'fast_execute_script'),
    (r'^execute_job/$', 'execute_job'),
    (r'^job_detail/$', 'job_detail'),
    (r'^get_log_content/$', 'get_log_content'),
    (r'^fast_push_file/$', 'fast_push_file'),
    (r'^helloworld/$', 'helloworld'),

    (r'^script/$', 'script'),
    (r'^script/list/$', 'script_list'),
    (r'^script/(\d+)$', 'script_get'),
    (r'^script/add/$', 'script_add'),
    (r'^script/delete/(\d+)$', 'script_delete'),
    (r'^script/update/(\d+)$', 'script_update'),
)
