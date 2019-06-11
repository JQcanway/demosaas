# -*- coding: utf-8 -*-
from django.db import models

class Template(models.Model):
    name = models.CharField(max_length=32)
    business = models.CharField(max_length=32)
    template_type = models.CharField(max_length=32)
    filePath = models.CharField(max_length=255)
    creator = models.CharField(max_length=32)
    create_date = models.DateTimeField(auto_now_add=True)
    update_user = models.CharField(max_length=32,null=True)
    update_date = models.DateTimeField(max_length=32,null=True)

    def toJson(self):
        data = {}
        data['id'] = self.id
        data['name'] = self.name
        data['business'] = self.business
        data['template_type'] = self.template_type
        data['filePath'] = self.filePath
        data['creator'] = self.creator
        data['create_date'] = self.create_date
        data['update_user'] = self.update_user
        data['update_date'] = self.update_date
        return data

class Center(models.Model):
    name = models.CharField(max_length=32)
    handle = models.CharField(max_length=32)
    business = models.CharField(max_length=32)
    template_type = models.CharField(max_length=32)
    operator = models.CharField(max_length=32)
    creator = models.CharField(max_length=32)
    create_date = models.DateTimeField(auto_now_add=True)
    task_state = models.CharField(max_length=32,default='待操作')

    def toJson(self):
        data = {}
        data['id'] = self.id
        data['name'] = self.name
        data['handle'] = self.handle
        data['business'] = self.business
        data['template_type'] = self.template_type
        data['operator'] = self.operator
        data['creator'] = self.creator
        data['create_date'] = self.create_date
        data['task_state'] = self.task_state
        return data

class Commission(models.Model):
    index = models.IntegerField()
    matter = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255)
    responsible = models.CharField(max_length=32)
    center_id = models.IntegerField()
    state = models.IntegerField(default=0)
    confirmor = models.CharField(max_length=32,null=True)
    confirm_time = models.DateTimeField(max_length=32,null=True)

    def toJson(self):
        data = {}
        data['id'] = self.id
        data['index'] = self.index
        data['matter'] = self.matter
        data['remarks'] = self.remarks
        data['responsible'] = self.responsible
        data['center_id'] = self.center_id
        data['state'] = ("已确认" if(self.state == 1) else "未确认")
        data['confirmor'] = self.confirmor
        data['confirm_time'] = self.confirm_time
        return data
