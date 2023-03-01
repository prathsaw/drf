from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    roll_number = models.IntegerField()
    city = models.CharField(max_length=64)
