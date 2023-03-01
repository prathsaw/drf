from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()

router.register('studentAPI', views.StudentModelView, basename='studentapi')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view(), name='obtain_token'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='refresh_token'),
    path('verifytoken/', TokenVerifyView.as_view(), name="verify_token")
]





