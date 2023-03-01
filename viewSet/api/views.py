from rest_framework import status, viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response


# Create your views here.
class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = StudentSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'Data updated successfully'}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu, request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'Data partially updated successfully'}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            stu.delete()
            return Response({'msg': 'Data deleted successfully'}, status=status.HTTP_201_CREATED)
