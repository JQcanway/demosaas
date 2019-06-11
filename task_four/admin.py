from django.contrib import admin

# Register your models here.

from django.contrib import admin
from task_four.models import Template,Center,Commission

admin.site.register(Template)
admin.site.register(Center)
admin.site.register(Commission)