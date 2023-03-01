from django.urls import path
from firstApp import views

urlpatterns = [
    path('api/', views.EmployeeRESTCBV.as_view()),
]