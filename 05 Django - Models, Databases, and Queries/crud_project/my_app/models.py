from django.db import models
from django.core.validators import MaxLengthValidator, MinValueValidator

# Create your models here.


class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    heartrate = models.IntegerField(null=True)

    # def __str__(self):
    #     return f"{self.last_name},{self.first_name},{self.age}"
