from django.contrib import admin
from firstApp.models import Employee

# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'enum', 'ename', 'esal', 'ecity']
