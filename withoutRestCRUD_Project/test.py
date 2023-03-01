import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
APP_NAME = 'firstApp/'

# ----------------------------------------------------------------------------------------------------------------------
# ENDPOINT = 'emp_detail/'
#
#
# def get_detail(id):
#     response = requests.get(BASE_URL + APP_NAME + ENDPOINT + id + '/')
#     print(response.status_code)
#     print(response.json())
#
#
# id = input('enter the id : \n')
# get_detail(id)

# ----------------------------------------------------------------------------------------------------------------------
# ENDPOINT = 'emp_list/'
#
#
# def get_list():
#     response = requests.get(BASE_URL + APP_NAME + ENDPOINT)
#     print(response.status_code)
#     print(response.json())
#
# get_list()
# ----------------------------------------------------------------------------------------------------------------------
# ENDPOINT = 'emp_list/'
#
#
# def create_employee():
#     new_emp = {
#         'enum': 104,
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
# ENDPOINT = 'emp_detail/'
#
#
# def update_detail(id):
#     new_emp = {
#         'enum': 104,
#         'ename': 'Uday',
#         'esal': 127000,
#         'ecity': 'Aurangabad'
#     }
#     response = requests.put(BASE_URL + APP_NAME + ENDPOINT + id + '/', data=json.dumps(new_emp))
#     print(response.status_code)
#     print(response.json())
#
#
# id = input('enter the id : \n')
# update_detail(id)

# ----------------------------------------------------------------------------------------------------------------------

ENDPOINT = 'emp_detail/'


def delete_detail(id):
    response = requests.delete(BASE_URL + APP_NAME + ENDPOINT + id + '/')
    print(response.status_code)
    print(response.json())


id = input('enter the id : \n')
delete_detail(id)