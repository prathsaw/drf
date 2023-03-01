from django.contrib import admin
from firstApp.models import Employee

# Register your models here.


@admin.register(Employee)
class EmployeeDetail(admin.ModelAdmin):
    list_display = ['enum', 'ename', 'esal', 'ecity']

