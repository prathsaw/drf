from django.urls import path
from firstApp import views

urlpatterns = [
    path('api/', views.EmployeeCBV.as_view())
]