# -*- coding: utf-8 -*-
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

import json
import sys
# Create your views here.
from django.http import JsonResponse
from common.mymako import render_mako_context

from task_four.service import createTemplate,templateList,createCenter,createList,commissionList,commissionListFinish
import os

import time



# 解决中文转码
reload(sys)
sys.setdefaultencoding( "utf-8" )


from home_application.esb_helper import run_fast_execute_script,get_job_instance_log


def home1(request):
    id = request.GET.get('id')
    return render_mako_context(request, '/task_four/taskCenter.html', {"id": id})

def home2(request):
    id = request.GET.get('id')
    return render_mako_context(request, '/task_four/taskTemplate.html', {"id": id})

def create_template(request):
    return JsonResponse(createTemplate(request))

def upload_file(request):
    filedata = request.FILES.get('file')
    path = default_storage.save(os.getcwd()+"/task_four/temporarily/"+filedata.name,ContentFile(filedata.read()))
    return JsonResponse({'data':path})

def template_list(request):
    return JsonResponse(templateList(request))

def create_center(request):
    return JsonResponse(createCenter(request))

def create_list(request):
    return JsonResponse(createList(request))

def commission_list(request,id):
    return JsonResponse(commissionList(request,id))

def commission_finish(request,center_id,id):
    return JsonResponse(commissionListFinish(request,center_id,id))







