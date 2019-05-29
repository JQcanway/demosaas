# -*- coding: utf-8 -*-

from django.shortcuts import render

import json
import time
import sys
from celery.schedules import crontab
from celery.task import periodic_task
# Create your views here.
from django.http import JsonResponse
from common.mymako import render_mako_context
from task_three.admin import HostMonitor
from home_application.admin import Script
from task_three.admin import Montitor

# 解决中文转码
reload(sys)
sys.setdefaultencoding( "utf-8" )


from home_application.esb_helper import run_fast_execute_script,get_job_instance_log


def home(request):
    id = request.GET.get('id')
    return render_mako_context(request, '/task_three/monitor.html', {"id": id})

def add_monitor(request):
    data = json.loads(request.body)
    HostMonitor.objects.create(biz_id = data['biz_id'],biz_name= data['biz_name'],ip= data['ip'],bk_cloud_id= data['bk_cloud_id']).save()
    return JsonResponse({'result':'true'})

def monitor_list(request):
     data = HostMonitor.objects.all()
     list = []
     for obj in data:
         list.append(obj.toJson())
     print list
     return JsonResponse({'data': list})

def monitor_delete(request,id):
     HostMonitor.objects.filter(id = id ).delete()
     return JsonResponse({'result':'true'})

@periodic_task(run_every=crontab(minute='*/5', hour='*', day_of_week="*"))
def exec_monitor():
    data = HostMonitor.objects.all()
    salData = Script.objects.get(name='监控指标采集')
    list = []
    for obj in data:
        list.append(obj.toJson())
    hostData = {}
    for n in list:
        hostData.setdefault(n['biz_id'], []).append(n)
    for key in hostData.keys():
        ip =[]
        for host in hostData.get(key):
            ipData = {"ip": host['ip'], "bk_cloud_id": host['bk_cloud_id']}
            ip.append(ipData)
        execData = run_fast_execute_script(key,salData.content,ip)
        time.sleep(10)
        logData = get_job_instance_log(key,execData['data'])
        for log in logData:
            property = log['log_content'].split('.')
            if( len(property) > 1):
                Montitor.objects.create(MEMORY = property[1],DISK= property[2],CPU= property[3],DATE= property[0],IP=log['ip']).save()

def monitor_details(request,ip):
    print ip
    data = Montitor.objects.filter(IP=ip)
    list = []
    for obj in data:
        list.append({'date': obj.DATE, 'memory': obj.MEMORY.strip('%'), 'disk': obj.DISK.strip('%'), 'cpu': obj.CPU.strip('%')})

    return JsonResponse({'data':list})






