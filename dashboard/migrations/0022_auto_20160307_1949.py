# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-07 19:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_auto_20160307_1944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise_set',
            old_name='excercises',
            new_name='exercises',
        ),
        migrations.AlterField(
            model_name='rehab_session',
            name='app_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 7, 19, 49, 41, 323271)),
        ),
    ]
