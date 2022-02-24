from django.db import models
from django.core.validators import MaxLengthValidator, MinValueValidator

# Create your models here.


class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxLengthValidator(120)
    ])
    heartrate = models.IntegerField(null=True, validators=[
        MinValueValidator(1),
        MaxLengthValidator(300)
    ])

    # def __str__(self):
    #     return f"{self.last_name},{self.first_name},{self.age}"
