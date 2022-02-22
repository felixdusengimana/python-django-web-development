from django.urls import path
from . import views

# register app namespace which is going to be used in URL names
app_name = "my_app"

urlpatterns = [
    path("", views.example_view, name="example_view"),
    path("variable/", views.variable_view, name="variable_view")
]