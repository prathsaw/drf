import json
from firstApp.models import Employee


def is_json(data):
    try:
        python_data = json.loads(data)
        valid = True
    except ValueError:
        valid = False
    return valid


def get_emp_by_id(id):
    try:
        emp = Employee.objects.get(id=id)

    except Employee.DoesNotExist:
        emp = None

    return emp


def get_all_employees():
    qs = Employee.objects.all()
    return qs
