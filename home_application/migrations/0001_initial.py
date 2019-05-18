# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('version', models.IntegerField()),
                ('desc', models.CharField(max_length=128)),
                ('source', models.CharField(max_length=32)),
                ('type', models.CharField(max_length=32)),
                ('content', models.TextField(null=True, blank=True)),
                ('creator', models.CharField(max_length=32)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
