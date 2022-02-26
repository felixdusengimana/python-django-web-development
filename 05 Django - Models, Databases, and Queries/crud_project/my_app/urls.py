from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_patient_view, name='list_patient')
]


