from django.urls import path
from api import views

urlpatterns = [
    path('listAPI/', views.ListStudent.as_view()),
    path('createAPI/', views.CreateStudent.as_view()),
    path('retrieveAPI/<int:pk>/', views.RetrieveStudent.as_view()),
    path('updateAPI/<int:pk>/', views.UpdateStudent.as_view()),
    path('destroyAPI/<int:pk>/', views.DestroyStudent.as_view()),
    path('list_create_API/', views.ListCreateStudent.as_view()),
    path('retrieve_update_API/<int:pk>/', views.RetrieveUpdateStudent.as_view()),
    path('retrieve_destroy_API/<int:pk>/', views.RetrieveDestroyStudent.as_view()),
    path('retrieve_update_destroy_API/<int:pk>/', views.RetrieveUpdateDestroyStudent.as_view()),
    path('api/', views.ListCreateStudent.as_view()),
    path('api/<int:pk>/', views.RetrieveUpdateDestroyStudent.as_view())
]