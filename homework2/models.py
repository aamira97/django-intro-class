from django.db import models


class Human(models.Model):
    Gender = [('Male', 'Male'),
              ('Female', 'Female')]
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=30)
    year_of_birth = models.IntegerField()
    gender = models.CharField(choices=Gender, max_length=6)

