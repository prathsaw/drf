from .models import Student


def get_user_by_id(id):
    try:
        stu = Student.objects.get(id=id)

    except Student.DoesNotExist:
        stu = None

    return stu
