from django.urls import path
from api import views

urlpatterns = [
    path('apiview/', views.StudentAPI.as_view(), name='apiview'),
    path('apiview/<int:id>/', views.StudentAPI.as_view(), name='apiview_with_pk')
]