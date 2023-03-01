from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
from .utils import get_user_by_id
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST


# Create your views here.


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api(request, id=None):
    if request.method == 'GET':
        id = id
        if id is not None:
            stu = get_user_by_id(id)
            if stu is not None:
                serializer = StudentSerializer(stu)
                return Response(serializer.data)
            return Response({'msg': 'You must pass valid id'})

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Record created successfully.'}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        id = id
        if id is not None:
            stu = get_user_by_id(id)
            if stu is not None:
                serializers = StudentSerializer(stu, data=request.data)
                if serializers.is_valid():
                    serializers.save()
                    return Response({'msg': 'Record updated successfully.'})
                return Response(serializers.errors)
            return Response({'msg': 'You must pass valid id'})
        else:
            return Response({'msg': 'You must send id.'})

    if request.method == 'PATCH':
        id = id
        if id is not None:
            stu = get_user_by_id(id)
            if stu is not None:
                serializers = StudentSerializer(stu, data=request.data, partial=True)
                if serializers.is_valid():
                    serializers.save()
                    return Response({'msg': 'Record updated successfully.'})
                return Response(serializers.errors)
            return Response({'msg': 'You must pass valid id'})
        else:
            return Response({'msg': 'You must send id.'})

    if request.method == 'DELETE':
        id = id
        if id is not None:
            stu = get_user_by_id(id)
            if stu is not None:
                stu.delete()
                return Response({'msg': 'Record deleted successfully.'})
            return Response({'msg': 'You must pass valid id'})
        return Response({'msg': 'You must pass id.'})


