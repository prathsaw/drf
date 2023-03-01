from django.urls import path
from api import views

urlpatterns = [
    path('apiview/', views.student_api, name='apiview'),

]