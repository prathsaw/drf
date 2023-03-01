from .models import Student
from .serializers import StudentSerializers
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttling import CustomThrottleRate


class StudentAPIView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    # throttle_classes = [AnonRateThrottle, UserRateThrottle]  # we mentioned throttle rate globally in settings.py file

    throttle_classes = [AnonRateThrottle, CustomThrottleRate]
    # for registered user we set our custom throttle rate, for that we build separate class in throttling.py and
    # registered that throttle rate globally in settings.py file

    # throttled scope is demonstrate in APIView project
