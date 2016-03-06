from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import Patient


# from .models import Choice, Question



def index(request):
    # upcoming_appointments = Patient.objects.get(doctor_id = "1")
    upcoming_appointments = Patient.objects.filter(status="Active").order_by('next_appointment')
    patient_list = Patient.objects.all()
    context = {
        'upcoming_appointments': upcoming_appointments,
        'patient_list': patient_list
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
