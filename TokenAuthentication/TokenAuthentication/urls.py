"""viewSet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from api.customAuth import CustomAuthtoken
from rest_framework.authtoken.views import ObtainAuthToken

router = DefaultRouter()
router.register('AuthToken', views.StudentModelViewSet, basename='AuthToken')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('get_or_create_token', ObtainAuthToken),  # this url will return a token using default ObtainAuthToken class.
    # http POST http://127.0.0.1:8000/get_or_create_token/ username='prathamesh' password='prathamesh' --- hit command
    path('gettoken/', CustomAuthtoken.as_view()),  # this url is used for generating token using api endpoint
]
