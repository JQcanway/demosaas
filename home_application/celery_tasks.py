# -*- coding: utf-8 -*-
"""
celery 任务示例

本地启动celery命令: python  manage.py  celery  worker  --settings=settings
周期性任务还需要启动celery调度命令：python  manage.py  celerybeat --settings=settings
"""
import datetime

from celery import task
from celery.schedules import crontab
from celery.task import periodic_task

from common.log import logger
from home_application.admin import Script
from home_application.esb_helper import run_fast_execute_script, get_job_instance_log
from task_three.admin import Montitor
from task_three.admin import HostMonitor
import time


@task()
def async_task(x, y):
    """
    定义一个 celery 异步任务
    """
    logger.error(u"celery 定时任务执行成功，执行结果：{:0>2}:{:0>2}".format(x, y))
    return x + y


def execute_task():
    """
    执行 celery 异步任务

    调用celery任务方法:
        task.delay(arg1, arg2, kwarg1='x', kwarg2='y')
        task.apply_async(args=[arg1, arg2], kwargs={'kwarg1': 'x', 'kwarg2': 'y'})
        delay(): 简便方法，类似调用普通函数
        apply_async(): 设置celery的额外执行选项时必须使用该方法，如定时（eta）等
                      详见 ：http://celery.readthedocs.org/en/latest/userguide/calling.html
    """
    now = datetime.datetime.now()
    logger.error(u"celery 定时任务启动，将在60s后执行，当前时间：{}".format(now))
    # 调用定时任务
    async_task.apply_async(args=[now.hour, now.minute], eta=now + datetime.timedelta(seconds=60))


@periodic_task(run_every=crontab(minute='*/5', hour='*', day_of_week="*"))
def get_time():
    """
    celery 周期任务示例

    run_every=crontab(minute='*/5', hour='*', day_of_week="*")：每 5 分钟执行一次任务
    periodic_task：程序运行时自动触发周期任务
    """
    execute_task()
    now = datetime.datetime.now()
    print now

    data = HostMonitor.objects.all()
    salData = Script.objects.get(name='监控指标采集')
    list = []
    for obj in data:
        list.append(obj.toJson())
    hostData = {}
    for n in list:
        hostData.setdefault(n['biz_id'], []).append(n)
    for key in hostData.keys():
        ip = []
        for host in hostData.get(key):
            ipData = {"ip": host['ip'], "bk_cloud_id": host['bk_cloud_id']}
            ip.append(ipData)
        execData = run_fast_execute_script(key, salData.content, ip)
        time.sleep(10)
        logData = get_job_instance_log(key, execData['data'])
        for log in logData:
            property = log['log_content'].split('.')
            if (len(property) > 1):
                Montitor.objects.create(MEMORY=property[1], DISK=property[2], CPU=property[3], DATE=property[0],
                                        IP=log['ip']).save()
    Montitor.objects.create(MEMORY='20%', DISK='20%', CPU='20%', DATE=now,
                            IP='127.0.0.1').save()
    logger.error(u"celery 周期任务调用成功，当前时间：{}".format(now))
