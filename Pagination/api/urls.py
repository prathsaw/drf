from django.urls import path
from api import views

urlpatterns = [
    path('listStudent/', views.StudentList.as_view(), name='list_student'),
    path('listEmployee/', views.EmployeeList.as_view(), name='list_employee'),
]