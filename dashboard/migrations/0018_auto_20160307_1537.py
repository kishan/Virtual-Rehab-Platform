# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-07 15:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_auto_20160307_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rehab_session',
            name='app_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 7, 15, 37, 23, 361751)),
        ),
    ]
