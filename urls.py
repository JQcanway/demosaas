# -*- coding: utf-8 -*-
"""
urls config
"""
from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# admin.autodiscover()

# 公共URL配置
urlpatterns = patterns(
    '',
    # Django后台数据库管理
    url(r'^admin/', include(admin.site.urls)),
    # 用户登录鉴权--请勿修改
    url(r'^account/', include('account.urls')),
    # 应用功能开关控制--请勿修改
    url(r'^app_control/', include('app_control.urls')),
    # task_two(里开始开发第二次作业主要功能
    url(r'^configuration/', include('task_two.urls')),
    # task_three(里开始开发第三次作业主要功能
    url(r'^monitor/', include('task_three.urls')),
    # task_four(里开始开发第四次作业主要功能
    url(r'^task/', include('task_four.urls')),
    # task_five(里开始开发第五次作业主要功能
    url(r'^work_manage/', include('task_five.urls')),
    # exam_one(里开始开发第1次考试主要功能
    url(r'^api/', include('exam_one.urls')),
    # 数据准备
    url(r'^data_preparation/', include('data_preparation.urls')),
    # 在home_application(根应用)里开始开发你的应用的主要功能
    url(r'^', include('home_application.urls')),

)


handler404 = 'error_pages.views.error_404'
handler500 = 'error_pages.views.error_500'
handler403 = 'error_pages.views.error_403'
handler401 = 'error_pages.views.error_401'
