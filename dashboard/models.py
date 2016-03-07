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

    STATE = (
        ('Active', 'Active'),
        ('Recovered', 'Recovered'),
    )

    STATUS = (
        ('Good', 'Good'),
        ('Needs Attention', 'Needs Attention'),
        ('Check-in', 'Check-in'),
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
    state = models.CharField(max_length=50, default = "Active", choices=STATE)
    status = models.CharField(max_length=50, default = "Good", choices=STATUS)

    def visited_last_week(self):
        return self.last_appointment >= timezone.now() - datetime.timedelta(days=7)

    # was_published_recently.admin_order_field = 'pub_date'
    # was_published_recently.boolean = True
    # was_published_recently.short_description = 'Published recently?'


    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return self.full_name


class Rehab_Session(models.Model):
    """workout session scheduled for patient to do at home"""
    patient = models.ForeignKey(Patient, blank=False, null=False, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, blank=False, null=True)

    # def get_patient_doctor(self):
    #     "Returns doctor assigned to patient"
    #     return self.patient.doctor
    # doctor = property(get_patient_doctor)

    STATUS = (
        ('Upcoming', 'Upcoming'),
        ('Missed', 'Missed'),
        ('Completed', 'Completed'),
    )

    app_date_time = models.DateTimeField(default=datetime.datetime.now())
    app_length = models.IntegerField(blank=False, null=False, default=30)
    status = models.CharField(max_length=50, default= "Upcoming", choices=STATUS)

    def get_overall_accuracy(self):
        return 99.99

    def get_overall_range_of_motion(self):
        return 79.99

    def get_exercise_categories(self):
        dic = {
            "Shoulder":35,
            "Arm": 65
        }

        return dic

    overall_accuracy = property(get_overall_accuracy)
    overall_range_of_motion = property(get_overall_range_of_motion)
    exercise_categories = property(get_exercise_categories)

    def get_appointments_for_patient(self, patient_id):
        # appointments = appointments.objects.get(patient=self.patient)
        # appointments = appointments.objects.filter(patient.id = patient_id)
        appointments = Patient.objects.get(id=patient_id).book_set.all()

    class Meta:
        verbose_name_plural = u'Appointment'

    def __str__(self):
        return u'Rehab_Session : %s for %s' % (self.id, self.patient.full_name)

class Exercise_Set(models.Model):
    """ set of excercises
        Ex. 3 sets of 15 reps of Arm Raises
    """
    rehab_session = models.ForeignKey(Rehab_Session, on_delete=models.CASCADE)
    # Exercise

    EXERCISE_CHOICES = (
    ('Arm', (
            (1, 'Forward Bicep Curl'),
            (2, 'Side Bicep Curl'),
        )
    ),
    ('Shoulder', (
            (101, 'Front Arm Raise'),
            (102, 'Lateral Arm Raise'),
        )
    ),
    ('Back', (
            (201, 'Scapular Squeeze'),
            (202, 'Thoracic Extension'),
        )
    ),
    ('Leg', (
            (301, 'Standing Hamstring Curl'),
            (302, 'Sit to Stand'),
        )
    ),
    ('Knee', (
            (401, 'Assisted Knee Flexion'),
            (402, 'Prolonged Knee Extension'),
        )
    ),

    )   

    exercise = models.CharField(max_length=200, default= 401, choices=EXERCISE_CHOICES)

    sets_total = models.IntegerField(blank=False, null=False, default=3)
    sets_completed = models.IntegerField(blank=True, null=True)
    reps_total = models.IntegerField(blank=False, null=False, default=15)
    reps_completed = models.IntegerField(blank=True, null=True)
    accuracy = models.IntegerField(blank=True, null=True)
    range_of_motion = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return u'Set for %s' % (self.rehab_session)

"""
class Exercise(models.Model):
    exercise_set = models.ManyToManyField(Exercise_Set)

    EXERCISE_CATERGORIES = (
        ('Arm', 'Arm'),
        ('Shoulder', 'Shoulder'),
        ('Back', 'Back'),
        ('Leg', 'Leg'),
        ('Knee', 'Knee'),
    )

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=EXERCISE_CATERGORIES)
"""
        
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

