# -*- coding: utf-8 -*-

import datetime
import json
import sys
# Create your views here.
from django.http import JsonResponse
from common.mymako import render_mako_context

from data_preparation.service import cc_search_biz,cc_search_host_ByBizId,cc_search_user

from database_manager.admin import Custom

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import os

# 解决中文转码
reload(sys)
sys.setdefaultencoding( "utf-8" )

def custom_home(request):
    id = request.GET.get('id')
    return render_mako_context(request, '/database_manager/custom.html', {"id": id})

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

# 列表查询
def list(request):
    name = request.GET.get('name')
    if name:
        data = Custom.objects.filter(name__contains=name)
    else:
        data = Custom.objects.filter(name__contains='')

    type = request.GET.get('type')
    if type:
        data = Custom.objects.filter(type=type)

    listData = []
    for obj in data:
        listData.append(obj.toJson())
    return JsonResponse({'data': listData})

# 删除
def delete(request,id):
    Custom.objects.filter(id=id).delete()
    return JsonResponse({'result': 'true'})

def add(request):
    data = json.loads(request.body)
    exam = Custom(name=data['name'],type=data['type'],field_name=data['field_name'],desc=data['desc'])
    exam.save()
    return JsonResponse({'result': 'true'})

def exam_upload(request):
    filedata = request.FILES.get('file')
    path = default_storage.save(os.getcwd()+"/static/file/"+filedata.name,ContentFile(filedata.read()))
    return JsonResponse({'data':path})













