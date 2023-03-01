from django.db import models


# Create your models here.
class Employee(models.Model):
    enum = models.IntegerField()
    ename = models.CharField(max_length=128)
    esal = models.FloatField()
    ecity = models.CharField(max_length=128)
