from .serializers import StudentSerializer, EmployeeSerializers
from .models import Student, Employee
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from .paginations import MyPagination, MyLimitOffsetPagination


# for PageNumberPagination
# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     pagination_class = PageNumberPagination
#
#
# class EmployeeList(ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializers
#     pagination_class = MyPagination

# ======================================================================================================================

# for PageNumberPagination
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = LimitOffsetPagination


class EmployeeList(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    pagination_class = MyLimitOffsetPagination

