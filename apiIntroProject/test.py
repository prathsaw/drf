# run this file on terminal to see response on terminal. To get output run server on one terminal and on another
# terminal run this test.py file.

# import requests
# BASE_URL = 'http://127.0.0.1:8000/'
# APP_NAME = 'firstApp/'
# ENDPOINT = 'jsonapi/'

# response = requests.get(BASE_URL + APP_NAME + ENDPOINT)
# data = response.json()

# print('Data from django application.')
# print('*' * 40)
# print(f'Employee Name : {data["name"]}')
# print(f'Employee Salary : {data["salary"]}')
# print(f'Employee Number : {data["number"]}')
# print(f'Employee City : {data["city"]}')

# ----------------------------------------------------------------------------------------------------------------------

import requests
BASE_URL = 'http://127.0.0.1:8000/'
APP_NAME = 'firstApp/'
ENDPOINT = 'jsonCBVapi2/'

# get method from JsonCBV2 class

response = requests.get(BASE_URL + APP_NAME + ENDPOINT)
data = response.json()
print(data)

# post method from JsonCBV2 class   ----------> we have commented csrf middleware to bypass csrf_token validation.

response = requests.post(BASE_URL + APP_NAME + ENDPOINT)
data = response.json()
print(data)

# put method from JsonCBV2 class

response = requests.put(BASE_URL + APP_NAME + ENDPOINT)
data = response.json()
print(data)

# delete method from JsonCBV2 class

response = requests.delete(BASE_URL + APP_NAME + ENDPOINT)
data = response.json()
print(data)
