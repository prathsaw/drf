from django.urls import path
from firstApp import views

urlpatterns = [
    path('api/', views.emp_data_view),
    path('jsonapi/', views.emp_data_jsonview),
    path('json_res_api/', views.emp_data_jsonview2),
    path('jsonCBVapi1/', views.JsonCBV.as_view()),
    path('jsonCBVapi2/', views.JsonCBV2.as_view())
]