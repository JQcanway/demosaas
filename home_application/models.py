# -*- coding: utf-8 -*-
from django.db import models

class Script(models.Model):
    name = models.CharField(max_length=32)
    version = models.IntegerField()
    desc = models.CharField(max_length=128)
    source = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    content = models.TextField(null=True, blank=True)
    creator = models.CharField(max_length=32)
    create_time = models.DateTimeField(auto_now_add=True)
    def toJson(self):
        data = {}
        data['id'] = self.id
        data['name'] = self.name
        data['version'] = self.version
        data['desc'] = self.desc
        data['source'] = self.source
        data['type'] = self.type
        data['content'] = self.content
        data['creator'] = self.creator
        if self.create_time:
            data['create_time'] = self.create_time
        else:
            data['create_time'] = None
        return data