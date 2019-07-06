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

class Custom(models.Model):
    name = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    field_name = models.CharField(max_length=32)
    desc = models.CharField(max_length=512)

    def toJson(self):
        data = {}
        data['id'] = self.id
        data['name'] = self.name
        data['type'] = self.type
        data['field_name'] = self.field_name
        data['desc'] = self.desc
        return data



