# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-06 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_patient_last_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='next_appointment',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
