from django.db import models

# Create your models here.

class HostMonitor(models.Model):
    biz_id = models.CharField(max_length=32)
    biz_name = models.CharField(max_length=32)
    ip = models.CharField(max_length=32)
    bk_cloud_id = models.CharField(max_length=32)

    def toJson(self):
        data = {}
        data['id'] = self.id
        data['biz_id'] = self.biz_id
        data['biz_name'] = self.biz_name
        data['ip'] = self.ip
        data['bk_cloud_id'] = self.bk_cloud_id
        return data

class Montitor(models.Model):
    IP = models.CharField(max_length=32)
    MEMORY = models.CharField(max_length=32)
    DISK = models.CharField(max_length=32)
    CPU = models.CharField(max_length=32)
    DATE = models.DateTimeField(max_length=32)

    def toJson(self):
        data = {}
        data['IP'] = self.MEMORY
        data['MEMORY'] = self.MEMORY
        data['DISK'] = self.DISK
        data['biz_name'] = self.biz_name
        data['CPU'] = self.CPU
        data['DATE'] = self.DATE
        return data