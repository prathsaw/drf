from django.urls import path
from api import views

urlpatterns = [
    path('apiview/', views.student_api, name='apiview'),
    path('apiview/<int:id>/', views.student_api, name='apiview_with_pk')
]