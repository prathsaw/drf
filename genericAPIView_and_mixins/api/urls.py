from django.urls import path
from api import views

urlpatterns = [
    # path('listAPI/', views.ListStudents.as_view(), name='listAPI'),
    # path('createAPI/', views.CreateStudent.as_view(), name='createAPI'),
    # path('retrieveAPI/<int:pk>/', views.RetrieveStudent.as_view(), name='retrieveAPI'),
    # path('updateAPI/<int:pk>/', views.UpdateStudent.as_view(), name='updateAPI'),
    # path('destroyAPI/<int:pk>/', views.DestroyStudent.as_view(), name='destroyAPI'),
    path('list_createAPI/', views.ListCreateStudent.as_view(), name='list_createAPI'),
    path('retrieve_update_destroyAPI/<int:pk>/', views.RetrieveUpdateDestroyStudent.as_view(),
         name='retrieve_update_destroyAPI'),
]