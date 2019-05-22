# -*- coding: utf-8 -*-
import json
import time

import requests
from django.http import JsonResponse

from account.decorators import login_exempt
from common.mymako import render_mako_context
from  common.mymako import render_json
from conf.default import APP_ID, APP_TOKEN, BK_PAAS_HOST
from home_application.esb_helper import cc_search_biz, cc_search_set, run_fast_execute_script, cc_search_host, \
    get_job_instance_log, get_host_ip_list, cc_get_job_detail, run_execute_job, cc_fast_push_file, \
    script_list_data,script_list_add,script_list_delete,script_list_update,script_list_get,cc_search_host_ByBizId


def home(request):
    """
    首页
    """
    id = request.GET.get('id')
    return render_mako_context(request, '/task_two/configuration.html',{ "id":id})

def get_business(request):
    data = cc_search_biz()
    data = data['data']
    print data
    selectData = []
    for obj in data['info']:
        selectData.append({'label':obj['bk_biz_name'],'value':obj['bk_biz_id']})
    print selectData
    return JsonResponse({'data': selectData})

def get_host(request,id):
    print "biz_id:"+id
    data = cc_search_host_ByBizId(id)
    print data
    data = data['data']
    hostList = []
    for obj in data['info']:
        host = obj['host']
        hostData={}
        hostData['innerip'] = host['bk_host_innerip']
        hostData['host_name'] = host['bk_host_name']
        hostData['os_name'] = host['bk_os_name']
        cloud = host['bk_cloud_id']
        cloud_area = ''
        for c in cloud:
            cloud_area += (c['bk_inst_name']+',')
        hostData['cloud_name'] = cloud_area[0:cloud_area.__len__()-1]
        hostList.append(hostData)
    return JsonResponse({'data':hostList})

def get_script(request):
    data = script_list_data(request)
    selectData = []
    for obj in data['data']:
        selectData.append({'label': obj['name'], 'value': obj['id']})
    print selectData
    return JsonResponse({'data': selectData})

def exec_script(request):
    data = json.loads(request.body)
    print data
    scriptId = data['script']
    print scriptId
    script = script_list_get(int(scriptId))
    script = script['data']
    ipList = data['ip']
    ipMap = []
    for ip in ipList:
        ipData = {"ip":ip,"bk_cloud_id":0}
        ipMap.append(ipData)
    execData = run_fast_execute_script(data['business'],script['content'],ipMap)

    logData = get_job_instance_log(data['business'],execData['data'])
    result = False
    logContent = ''
    for log in logData:
        result = log['is_success']
        logContent += log['log_content']

    return JsonResponse({'result':result.__str__().lower(),'logContent':logContent})