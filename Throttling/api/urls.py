from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
from api.customAuth import CustomAuthtoken

router = DefaultRouter()
router.register('studentAPI', views.StudentAPIView, basename='studentAPI')

urlpatterns = [
    path('', include(router.urls)),
    path('gettoken/', CustomAuthtoken.as_view())
]