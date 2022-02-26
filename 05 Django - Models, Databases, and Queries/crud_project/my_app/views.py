from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import models
from .forms import PatientForm


# Create your views here.
def list_patient_view(request):
    all_patient = models.Patient.objects.all()
    context = {
        'patients': all_patient
    }
    print(all_patient)
    return render(request, 'my_app/list.html', context=context)


def register_patient_view(request):
    form = PatientForm()
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            webpage = reverse("my_app:list_patient")
            form.save()
            return HttpResponseRedirect(webpage)
    context = {
        "form": form
    }
    return render(request, 'my_app/new_patient.html', context)