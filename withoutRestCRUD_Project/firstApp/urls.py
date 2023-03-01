from django.urls import path
from firstApp import views

urlpatterns = [
    path('emp_detail/<int:id>/', views.EmployeeDetailCBV.as_view()),
    path('emp_list/', views.EmployeeListCBV.as_view()),
]
