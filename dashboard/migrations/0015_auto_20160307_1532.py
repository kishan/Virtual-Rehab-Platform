# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-07 15:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_auto_20160307_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='exercise_set',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='app_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 7, 15, 32, 36, 336798)),
        ),
    ]
