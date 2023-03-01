import json, requests

BASE_URL = 'http://127.0.0.1:8000/'
APP_NAME = 'firstApp/'
ENDPOINT = 'api/'


def get_employee(id=None):
    data = {}
    if id is not None:
        data = {
            'id': id
        }
    response = requests.get(BASE_URL + APP_NAME + ENDPOINT, data=json.dumps(data))
    print(response.status_code)
    print(response.json())


# id = input('Please enter the id : \n')
get_employee()

# ----------------------------------------------------------------------------------------------------------------------

# def create_employee():
#     new_emp = {
#         'enum': 103,
#         'ename': 'Uday',
#         'esal': 125000,
#         'ecity': 'Aurangabad'
#     }
#     response = requests.post(BASE_URL + APP_NAME + ENDPOINT, data=json.dumps(new_emp))
#     print(response.status_code)
#     print(response.json())
#
#
# create_employee()

# ----------------------------------------------------------------------------------------------------------------------
#
# def update_detail(id):
#     new_emp = {
#         'id': id,
#         'enum': 104,
#         # 'ename': 'Shubham',
#         'esal': 136000,
#         # 'ecity': 'Jalgaon'
#     }
#     response = requests.put(BASE_URL + APP_NAME + ENDPOINT, data=json.dumps(new_emp))
#     print(response.status_code)
#     print(response.json())
#
#
# id = input('enter the id : \n')
# update_detail(id)


# ----------------------------------------------------------------------------------------------------------------------


# def delete_detail(id):
#     data = {
#         # 'id': id,
#     }
#     response = requests.put(BASE_URL + APP_NAME + ENDPOINT, data=json.dumps(data))
#     print(response.status_code)
#     print(response.json())
#
#
# id = input('enter the id : \n')
# delete_detail(id)
