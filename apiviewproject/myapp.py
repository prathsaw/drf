import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'apiview/'
headers = {'content-type': 'application/json'}


# def get_data(id=None):
#     data = {}
#     if id is not None:
#         data = {'id': id}
#     json_data = json.dumps(data)
#     res = requests.get(url=BASE_URL+END_POINT, headers=headers, data=json_data)
#     print(res.json())
#
# get_data(1)

# def post_data():
#     data = {
#         'first_name': 'Prashant',
#         'last_name': 'Desai',
#         'roll_number': 105,
#         'city': 'satara'
#     }
#     json_data = json.dumps(data)
#     res = requests.post(url=BASE_URL + END_POINT, headers=headers, data=json_data)
#     print(res.json())
#
#
# post_data()

# def update_data(id):
#     data = {
#         'id': id,
#         'first_name': 'Prashant',
#         'last_name': 'Desai',
#         'roll_number': 105,
#         'city': 'pachagani'
#     }
#     json_data = json.dumps(data)
#     res = requests.put(url=BASE_URL + END_POINT, headers=headers, data=json_data)
#     print(res.json())
#
#
# update_data(6)

def delete_data(id):
    data = {
        'id': id,
    }
    json_data = json.dumps(data)
    res = requests.delete(url=BASE_URL + END_POINT, headers=headers, data=json_data)
    print(res.json())


delete_data(6)


