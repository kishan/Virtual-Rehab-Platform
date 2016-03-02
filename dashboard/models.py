from __future__ import unicode_literals
import datetime
from django.utils import timezone

from django.db import models
from django.utils.encoding import python_2_unicode_compatible




@python_2_unicode_compatible
class Doctor(models.Model):
    TITLE_CHOICES = (
        ('Mr', 'Mr.'),
        ('Ms', 'Ms.'),
        ('Dr', 'Dr.'),
    )

    # patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    votes = models.IntegerField(default=0)
    member_since = models.DateTimeField('member since')
    title = models.CharField(max_length=2, choices=TITLE_CHOICES)

    def __str__(self):
        return self.name
    
@python_2_unicode_compatible
class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    last_appointment = models.DateTimeField('date of last appointment')
    age = models.IntegerField(default=0)
    DOB = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    rehab_focus = models.CharField(max_length=20)
    # https://github.com/stefanfoulis/django-phonenumber-field
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    previous_injuries = models.CharField(max_length=50)
    notes = models.CharField(max_length=200)
    recovery_percentage = models.IntegerField(default=0)

    def visited_last_week(self):
        return self.last_appointment >= timezone.now() - datetime.timedelta(days=7)

    # was_published_recently.admin_order_field = 'pub_date'
    # was_published_recently.boolean = True
    # was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.name