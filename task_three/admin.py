from django.contrib import admin

# Register your models here.

from django.contrib import admin
from task_three.models import HostMonitor
from task_three.models import Montitor

admin.site.register(HostMonitor)
admin.site.register(Montitor)