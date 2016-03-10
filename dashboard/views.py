from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import Patient

import datetime
from datetime import timedelta
from django.utils.timezone import utc



# from .models import Choice, Question



def index(request):
    # upcoming_appointments = Patient.objects.get(doctor_id = "1")
    upcoming_appointments = Patient.objects.filter(state="Active").order_by('next_appointment')
    patient_list = Patient.objects.all()
    num_of_active_patients = Patient.objects.filter(state="Active").count()

    # find time until next appointment
    if len(upcoming_appointments) == 0:
        time_until_next_app = "N/A"
    else:
        next_appointment_date = upcoming_appointments[0].next_appointment
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        until_next_app = next_appointment_date - now
        if until_next_app.days > 0:
            time_until_next_app = str(until_next_app.days) + " days"
        elif (until_next_app.seconds//3600) > 0 :
            time_until_next_app = str(until_next_app.seconds//3600) + " hours"
        else:
            time_until_next_app = str((until_next_app.seconds//60)%60) + " min"

    context = {
        'time_until_next_app':time_until_next_app,
        'upcoming_appointments': upcoming_appointments,
        'patient_list': patient_list,
        'num_of_active_patients': num_of_active_patients
        }
    return render(request, 'dashboard/index.html', context)


def profile(request, patient_id):
    patient = Patient.objects.get(id = patient_id)
    recovery_percentage = patient.recovery_percentage
    if recovery_percentage < 20:
        stage1_percentage = recovery_percentage
        stage2_percentage = 0
    else:
        stage1_percentage = recovery_percentage * (0.7)
        stage2_percentage = recovery_percentage * (0.3)
    context = {
        'patient': patient,
        'stage1_percentage':stage1_percentage,
        'stage2_percentage':stage2_percentage
        }
    return render(request, 'dashboard/profile.html', context)


def session(request):
    session = "temp"
    context = {'session': session}
    return render(request, 'dashboard/session.html', context)

def form(request):
    form = "temp"
    context = {'form': form}
    return render(request, 'dashboard/form.html', context)


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
