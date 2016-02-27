from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse


# from .models import Choice, Question



def index(request):
    # upcoming_appointments = Doctor.objects.order_by('-pub_date')[:5]
    upcoming_appointments = "temp"
    context = {'upcoming_appointments': upcoming_appointments}
    return render(request, 'dashboard/index.html', context)


def profile(request):
    profile = "temp"
    context = {'profile': profile}
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
