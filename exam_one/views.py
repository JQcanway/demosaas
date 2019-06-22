# -*- coding: utf-8 -*-
import datetime
import json
from django.http import JsonResponse
from common.mymako import render_mako_context
from home_application.esb_helper import cc_search_user

# Create your views here.
from exam_one.models import Template

def task(request):
    id = request.GET.get('id')
    return render_mako_context(request, '/exam_one/task.html', {"id": id})

def template(request):
    id = request.GET.get('id')
    return render_mako_context(request, '/exam_one/template.html', {"id": id})

def test(request):
    result = {}
    result['result'] = True
    result['data'] ={'username':request.user.username,'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    return JsonResponse(result)


def template_create(request):
    data = json.loads(request.body)
    template = Template(name=data['name'],business=data['business'],script = data['script'],threshold = data['threshold'],remark = data['remark'],creator= request.user.username,create_date= datetime.datetime.now())
    template.save()
    return JsonResponse({'result': 'true'})

def template_list(request):
    name = request.GET.get('name')
    if name:
        data = Template.objects.filter(name__contains=name)
    else:
        data = Template.objects.filter(name__contains='')
    business = request.GET.get('business')
    if business:
        data = data.objects.filter(business=business)

    listData = []
    for obj in data:
        listData.append(obj.toJson())

    return JsonResponse({'data': listData})

def template_delete(request,id):
    Template.objects.filter(id=id).delete()
    return JsonResponse({'result': 'true'})