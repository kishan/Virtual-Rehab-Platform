from __future__ import unicode_literals
import datetime
from datetime import date
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
    
    member_since = models.DateTimeField('member since')
    title = models.CharField(max_length=2, choices=TITLE_CHOICES)

    def _get_full_name(self):
        "Returns the person's full name."
        return 'Dr. %s %s' % (self.first_name, self.last_name)

    full_name = property(_get_full_name)

    def __str__(self):
        return self.full_name
    
@python_2_unicode_compatible
class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    STATUS = (
        ('Active', 'Active'),
        ('Recovered', 'Recovered'),
    )
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    def _get_full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)
    full_name = property(_get_full_name)

    DOB = models.DateField()
    def get_age(self):
        today = date.today() 
        delta = today - self.DOB
        return delta.days / 365
    age = property(get_age)

    pub_date = models.DateTimeField('date published')

    def get_last_appointment(self):
        return self.pub_date
    last_appointment = models.DateTimeField(null=True, blank=True)
    # last_appointment = property(get_last_appointment)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    rehab_focus = models.CharField(max_length=20)
    # https://github.com/stefanfoulis/django-phonenumber-field
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    previous_injuries = models.CharField(max_length=50)
    notes = models.CharField(max_length=200)
    recovery_percentage = models.IntegerField(default=0)
    dummy_image = models.CharField(max_length=200, default="http://pixel.nymag.com/imgs/daily/intelligencer/2015/08/10/10-donald-trump-debate.w750.h560.2x.jpg")
    next_appointment = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=9, default = "Active", choices=STATUS)

    def visited_last_week(self):
        return self.last_appointment >= timezone.now() - datetime.timedelta(days=7)

    # was_published_recently.admin_order_field = 'pub_date'
    # was_published_recently.boolean = True
    # was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.full_name



class Appointment(models.Model):
    patient = models.ForeignKey(Patient, blank=False, null=False)
    doctor = models.ForeignKey(Doctor, blank=False, null=False)

    # def get_patient_doctor(self):
    #     "Returns doctor assigned to patient"
    #     return self.patient.doctor
    # doctor = property(get_patient_doctor)




    app_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # app_length = models.IntegerField(blank=False, null=False)
    # status = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        verbose_name_plural = u'Appointment'

    def __str__(self):
        return u'Appointment : %s' % self.id

    # def assign_room(self, room_id):
    #     room = Room.objects.get(id=room_id)

    #     if room.status == "Available":
    #         room.status = "Waiting"
    #         room.save()

    #         appointment = Appointment.objects.get(patient=self.patient)
    #         appointment.room = room
    #         appointment.status = "ExamRoom"
    #         appointment.save()

    # def calculate_order(self):
    #     appointments = Appointment.objects.filter(doctor=self.doctor).exclude(status="Completed", doctor_entry_time__isnull=False)
        
    #     try:
    #         max_order = Appointment.objects.get(doctor=self.doctor).exclude(status="Completed", doctor_entry_time__isnull=False).order_by('-order')
    #     except Exception, e:
    #         max_order = 0
        

    #     if not appointments:
    #         return 1
    #     else:
    #         return int(max_order) + 1

    #     return 1

    # def assign_next_patient(self):
    #     available_rooms = Room.objects.filter(status="Available")
        
    #     if available_rooms:
    #         selected_room = available_rooms[0]
    #         doctors = Doctor.objects.all()

    #         for doctor in doctors:
    #             patient_queue = Appointment.objects.filter(doctor=doctor, status="WaitingRoom").order_by('order')

    #             if patient_queue:
    #                 patient_queue[0].assign_room(selected_room.id)
    #                 return True

    #     return False

    # def save(self, *args, **kwargs):
    #     super(Appointment, self).save(*args, **kwargs)