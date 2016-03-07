# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-07 19:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0020_auto_20160307_1830'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise_set',
            old_name='sets',
            new_name='sets_total',
        ),
        migrations.AlterField(
            model_name='exercise_set',
            name='excercises',
            field=models.CharField(choices=[('Arm', ((1, 'Forward Bicep Curl'), (2, 'Side Bicep Curl'))), ('Shoulder', ((101, 'Front Arm Raise'), (102, 'Lateral Arm Raise'))), ('Back', ((201, 'Scapular Squeeze'), (202, 'Thoracic Extension'))), ('Leg', ((301, 'Standing Hamstring Curl'), (302, 'Sit to Stand'))), ('Knee', ((401, 'Assisted Knee Flexion'), (402, 'Prolonged Knee Extension')))], default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='rehab_session',
            name='app_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 7, 19, 44, 21, 716951)),
        ),
    ]