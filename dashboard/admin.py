from django.contrib import admin

from .models import *

class Patient_Admin(admin.ModelAdmin):
    model = Patient
    list_display = ('first_name','last_name', 'age', 'gender', 'phone_number','recovery_percentage', 'doctor')
    list_filter = ['first_name','last_name', 'DOB', 'recovery_percentage', 'doctor']
    search_fields = ['full_name']
    readonly_fields = ["age",]


class Rehab_Session_Admin(admin.ModelAdmin):
    model = Rehab_Session
    list_display = ('patient','doctor', 'app_date_time', 'app_length', 'status')


class Exercise_Set_Admin(admin.ModelAdmin):
    model = Exercise_Set
    list_display = ('rehab_session','get_exercise_display', 'sets_total', 'sets_completed',
     'reps_total','reps_completed', 'accuracy', 'range_of_motion')

admin.site.register(Patient, Patient_Admin)
admin.site.register(Doctor)
admin.site.register(Rehab_Session, Rehab_Session_Admin)
admin.site.register(Exercise_Set, Exercise_Set_Admin)
# admin.site.register(Exercise)
