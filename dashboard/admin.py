from django.contrib import admin

from .models import Patient, Doctor




class PatientAdmin(admin.ModelAdmin):
    model = Patient
    list_display = ('full_name', 'age', 'gender', 'previous_injuries', 'recovery_percentage', 'doctor')
    list_filter = ['last_name', 'DOB', 'recovery_percentage', 'doctor']
    search_fields = ['full_name']
    readonly_fields = ["age",]

admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor)
