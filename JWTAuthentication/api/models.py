from django.db import models

# Create your models here.


class Student(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)