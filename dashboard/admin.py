from django.contrib import admin

from .models import Patient, Doctor

class PatientAdmin(admin.ModelAdmin):
    model = Patient
    list_display = ('first_name','last_name', 'age', 'gender', 'phone_number','recovery_percentage', 'doctor')
    list_filter = ['first_name','last_name', 'DOB', 'recovery_percentage', 'doctor']
    search_fields = ['full_name']
    readonly_fields = ["age",]

admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor)
