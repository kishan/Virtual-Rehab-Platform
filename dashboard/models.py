from __future__ import unicode_literals
import datetime
from django.utils import timezone

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Patient(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    last_appointment = models.DateTimeField('date of last appointment')
    doctor = models.CharField(max_length=50) # change to Doctor model
    age = models.IntegerField(default=0)

    def visited_last_week(self):
        return self.last_appointment >= timezone.now() - datetime.timedelta(days=7)

    # was_published_recently.admin_order_field = 'pub_date'
    # was_published_recently.boolean = True
    # was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Doctor(models.Model):
    name = models.ForeignKey(Question, on_delete=models.CASCADE)
    patient = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name