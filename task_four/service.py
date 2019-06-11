# -*- coding: utf-8 -*-
from datetime import datetime

from django.shortcuts import render

import json
import sys
import time
import xlrd

from task_four.admin import Template,Center,Commission

# 解决中文转码
reload(sys)
sys.setdefaultencoding( "utf-8" )

def createTemplate(request):
    data = json.loads(request.body)
    Template.objects.create(name=data['name'],business=data['business'],template_type= data['template_type'],filePath= data['filePath'], creator= data['creator'],create_date=datetime.now()).save()
    return {'result': 'true'}

def templateList(request):
    name = request.GET.get('name')
    if name:
        data = Template.objects.filter(name__contains=name)
    else:
        data = Template.objects.filter(name__contains='')

    business = request.GET.get('business')
    if business:
        data = Template.objects.filter(business = business)

    template_type = request.GET.get('template_type')
    if template_type:
        data = Template.objects.filter(template_type = template_type)

    listData = []
    for obj in data:
        listData.append(obj.toJson())

    return {'data': listData}

def createCenter(request):
    data = json.loads(request.body)

    center = Center(name=data['name'],business=data['business'],template_type= data['template_type'],operator = data['creator'],handle = data['handle'],creator= data['creator'],create_date=time.time())
    center.save()
    workbook = xlrd.open_workbook(data['filePath'])
    Data_sheet = workbook.sheets()[0]  # 通过索引获取
    rowNum = Data_sheet.nrows  # sheet行数

    for i in range(rowNum):
        if i > 1:
            Commission(index=Data_sheet.cell_value(i, 0),matter=Data_sheet.cell_value(i,1),remarks=Data_sheet.cell_value(i,2),responsible=Data_sheet.cell_value(i, 3),center_id=center.id).save()

    return {'result': 'true'}

def createList(request):
    name = request.GET.get('name')
    if name:
        data = Center.objects.filter(name__contains=name)
    else:
        data = Center.objects.filter(name__contains='')

    business = request.GET.get('business')
    if business:
        data = Center.objects.filter(business=business)

    template_type = request.GET.get('template_type')
    if template_type:
        data = Center.objects.filter(template_type=template_type)

    task_state = request.GET.get('task_state')
    if task_state:
        data = Center.objects.filter(task_state=task_state)

    creator = request.GET.get('creator')
    if creator:
        data = Center.objects.filter(creator=creator)

    handle = request.GET.get('handle')
    if handle:
        data = Center.objects.filter(handle__contains=handle)
    else:
        data = Center.objects.filter(handle__contains='')

    listData = []
    for obj in data:
        listData.append(obj.toJson())

    return {'data': listData}

def commissionList(request,id):
    sqlData = Commission.objects.filter(center_id = id)
    data = []
    for obj in sqlData:
        data.append(obj.toJson())
    return {'data':data}

def commissionListFinish(request,center_id,id):
    commission = Commission.objects.get(id = id )
    commission.state = 1
    commission.confirmor = 'admin'
    commission.confirm_time = datetime.now()
    commission.save()
    ensureCount = Commission.objects.filter(center_id = center_id,state = 1).count()
    allCount = Commission.objects.filter(center_id=center_id).count()
    if ensureCount == allCount:
        Center.objects.filter(id = center_id).update(task_state = "完成")
    else:
        Center.objects.filter(id=center_id).update(task_state="操作中")
    return {'result': 'true'}


