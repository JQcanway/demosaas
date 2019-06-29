# -*- coding: utf-8 -*-
from django.db import models

import datetime


# ===============================================================================
# state = models.IntegerField(default=0)
# create_date = models.DateTimeField(auto_now_add=True)
#
# name = models.CharField(max_length=32)
# task_state = models.CharField(max_length=32,default='待操作')
# ===============================================================================

class Exam(models.Model):
    business = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    exam_type = models.CharField(max_length=32)
    principal = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    exam_date = models.DateField()
    site = models.CharField(max_length=32)
    filePath = models.CharField(max_length=255)

    def toJson(self):
        data = {}
        data['id'] = self.id
        data['business'] = self.business
        data['name'] = self.name
        data['exam_type'] = self.exam_type
        data['principal'] = self.principal
        data['phone'] = self.phone
        data['exam_date'] = self.exam_date
        data['site'] = self.site
        data['filePath'] = self.filePath

        if  int(datetime.datetime.strftime(self.exam_date,'%d')) > int(datetime.datetime.now().strftime('%d')):
            data['exam_state'] = '未开始'
        elif int(datetime.datetime.strftime(self.exam_date,'%d')) < int(datetime.datetime.now().strftime('%d')):
            data['exam_state'] = '已结束'
        else:
            data['exam_state'] = '考试中'
        return data

class Examinee(models.Model):
    name = models.CharField(max_length=32)
    department = models.CharField(max_length=32)
    score = models.IntegerField(default=0)
    result = models.CharField(max_length=32)
    desc = models.CharField(max_length=1024)

    def toJson(self):
        data = {}
        data['id'] = self.id
        data['name'] = self.name
        data['department'] = self.department
        data['score'] = self.score
        data['result'] = self.result
        data['desc'] = self.desc
        return data



