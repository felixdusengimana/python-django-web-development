from django.urls import path
from . import views

app_name = 'my_app'
urlpatterns = [
    path("", views.list_patient_view, name='list_patient'),
    path("add-patient/", views.register_patient_view, name="register_patient")
]


