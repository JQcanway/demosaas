# -*- coding: utf-8 -*-
from django.db import models
import datetime

# Create your models here.

class Template(models.Model):
    name = models.CharField(max_length=32)
    businessId = models.CharField(max_length=32)
    business = models.CharField(max_length=32)
    script = models.TextField(null=True, blank=True)
    threshold = models.CharField(max_length=32)
    remark = models.TextField(null=True, blank=True)
    creator = models.CharField(max_length=32)
    create_date = models.DateTimeField(auto_now_add=True)

    def toJson(self):
        data = {}
        data['id'] = self.id
        data['name'] = self.name
        data['businessId'] = self.businessId
        data['business'] = self.business
        data['script'] = self.script
        data['threshold'] = self.threshold
        data['remark'] = self.remark
        data['creator'] = self.creator
        if self.create_date:
            data['create_date'] = self.create_date
        else:
            data['create_date'] = None
        return data