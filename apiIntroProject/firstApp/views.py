import json

from django.http import HttpResponse, JsonResponse


# Create your views here.
def emp_data_view(request):
    emp_data = {
        'name': 'Shubham',
        'salary': '150000',
        'number': '4565',
        'city': 'Jalgaon',
    }

    response = f"<h1>Name : {emp_data['name']}<br> Salary : {emp_data['salary']}<br> Number : {emp_data['number']}<br> City : {emp_data['city']}</h1>"
    return HttpResponse(response)


def emp_data_jsonview(request):
    emp_data = {
        'name': 'Shubham',
        'salary': '150000',
        'number': '4565',
        'city': 'Jalgaon',
    }
    json_data = json.dumps(emp_data)
    return HttpResponse(json_data, content_type='application/json')


def emp_data_jsonview2(request):
    emp_data = {
        'name': 'Shubham',
        'salary': '150000',
        'number': '4565',
        'city': 'Jalgaon',
    }
    return JsonResponse(emp_data)


from django.views.generic import View


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        emp_data = {
            'name': 'Shubham',
            'salary': '150000',
            'number': '4565',
            'city': 'Jalgaon',
        }
        return JsonResponse(emp_data)


from firstApp.mixins import HttpResponseMixins


class JsonCBV2(HttpResponseMixins, View):
    # we are interacting with this file from test.py file.
    # here we are using mixin concept, imported HttpResponseMixins class from mixins.py file.
    def get(self, request, *args, **kwargs):
        json_data = json.dumps({'dict': 'This response from get method'})
        # to call one instance method from another self key must be required
        return self.render_to_http_response(json_data)

    def post(self, request, *args, **kwargs):
        json_data = json.dumps({'dict': 'This response from post method'})
        return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        json_data = json.dumps({'dict': 'This response from put method'})
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        json_data = json.dumps({'dict': 'This response from delete method'})
        return HttpResponse(json_data, content_type='application/json')
