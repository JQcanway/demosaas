# -*- coding: utf-8 -*-

import datetime
import json
import sys
# Create your views here.
from django.http import JsonResponse
from common.mymako import render_mako_context

from data_preparation.service import cc_search_biz,cc_search_host_ByBizId,cc_search_user
from admin import Examinee,Exam

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import os

# 解决中文转码
reload(sys)
sys.setdefaultencoding( "utf-8" )

def home(request):
    id = request.GET.get('id')
    return render_mako_context(request, '/data_preparation/home.html', {"id": id})

def search_biz(request):
    data = cc_search_biz(request.user.username)
    data = data['data']
    selectData = []
    for obj in data['info']:
        selectData.append({'label': obj['bk_biz_name'], 'value': obj['bk_biz_id']})
    return JsonResponse({'data': selectData})

def search_host(request,bizId):
    data = cc_search_host_ByBizId(bizId)
    data = data['data']
    hostList = []
    for obj in data['info']:
        host = obj['host']
        hostData = {}
        hostData['innerip'] = host['bk_host_innerip']
        hostData['host_name'] = host['bk_host_name']
        hostData['os_name'] = host['bk_os_name']
        cloud = host['bk_cloud_id']
        cloud_area = ''
        for c in cloud:
            cloud_area += (c['bk_inst_name'] + ',')
        hostData['cloud_name'] = cloud_area[0:cloud_area.__len__() - 1]

        hostData['bk_cloud_id'] = cloud[0]['id']
        hostList.append(hostData)
    return JsonResponse({'data': hostList})


def search_users(request):
    return JsonResponse(cc_search_user(), safe=False)

# 考试列表查询
def list(request):
    business = request.GET.get('business')

    listData = []
    if business:
        data = cc_search_host_ByBizId(business)
        data = data['data']
        for obj in data['info']:
            host = obj['host']
            hostData = {}
            hostData['innerip'] = host['bk_host_innerip']
            hostData['host_name'] = host['bk_host_name']
            hostData['os_name'] = host['bk_os_name']
            cloud = host['bk_cloud_id']
            cloud_area = ''
            for c in cloud:
                cloud_area += (c['bk_inst_name'] + ',')
            hostData['cloud_name'] = cloud_area[0:cloud_area.__len__() - 1]

            hostData['bk_cloud_id'] = cloud[0]['id']
            listData.append(hostData)

        ip =  request.GET.get('ip')
        if ip:
            listData = []
            for obj in data['info']:
                host = obj['host']
                if host['bk_host_innerip'] in ip:
                    hostData = {}
                    hostData['innerip'] = host['bk_host_innerip']
                    hostData['host_name'] = host['bk_host_name']
                    hostData['os_name'] = host['bk_os_name']
                    cloud = host['bk_cloud_id']
                    cloud_area = ''
                    for c in cloud:
                        cloud_area += (c['bk_inst_name'] + ',')
                    hostData['cloud_name'] = cloud_area[0:cloud_area.__len__() - 1]

                    hostData['bk_cloud_id'] = cloud[0]['id']
                    listData.append(hostData)
    else:
        return JsonResponse({'data': []})


    for obj in data:
        listData.append(obj.toJson())
    return JsonResponse({'data': listData})

# 考试详情查询
def exam_one(request,id):

    return JsonResponse(cc_search_user(), safe=False)

# 考试删除
def delete(request,id):
    Exam.objects.filter(id=id).delete()
    return JsonResponse({'result': 'true'})

def add(request):
    data = json.loads(request.body)
    exam = Exam(business=data['business'],name=data['name'],exam_type=data['exam_type'],principal=data['principal'],phone=data['phone'],exam_date=datetime.datetime.strptime(str(data['exam_date']).split('T')[0], '%Y-%m-%d'),site=data['site'],filePath=data['filePath'])
    exam.save()
    return JsonResponse({'result': 'true'})

def upload(request):
    filedata = request.FILES.get('file')
    path = default_storage.save(os.getcwd()+"/static/"+filedata.name,ContentFile(filedata.read()))
    return JsonResponse({'data':path})













