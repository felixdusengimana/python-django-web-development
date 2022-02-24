from django.shortcuts import render
from . import models


# Create your views here.
def list_patient_view(request):
    all_patient = models.Patient.objects.all()
    context = {
        'patients': all_patient
    }
    return render(request, 'my_app/list.html', context=context)