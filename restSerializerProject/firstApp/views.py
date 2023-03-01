import io
import json
from django.views.generic import View
from firstApp.mixins import HttpResponseMixin
from firstApp.utils import is_json, get_emp_by_id, get_all_employees
from rest_framework.parsers import JSONParser
from firstApp.serializers import EmployeeSerializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class EmployeeRESTCBV(HttpResponseMixin, View):
    def get(self, request, *args, **kwargs):
        # fetching data from partner application, here, test.py
        data = request.body

        # checking data from test.py file is valid or not i.e. json data or not.
        # for that we have custom method in utils.py file
        valid_json = is_json(data)

        if not valid_json:
            # if there is no valid json record, display provide valid json data message.
            json_data = json.dumps({'msg': 'Please provide valid json data.'})
            return self.render_to_http_response(json_data, status=400)

        # converting json data from test.py file into python dictionary
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)

        # checking provided_data contains id attribute or not
        id = python_data.get('id', None)

        # if provided_data contains id attribute then check provided id is present in database or not
        if id is not None:
            emp = get_emp_by_id(id)

            # if there is no matching id found, display no record found message.
            if emp is None:
                json_data = json.dumps({'msg': 'No such id present.'})
                return self.render_to_http_response(json_data, status=400)

            # if matching id found then fetch record corresponding to that id.
            serializer = EmployeeSerializer(emp)

            json_data = JSONRenderer().render(serializer.data)

            return self.render_to_http_response(json_data)

        # if provided_data contains no id attribute then get all employee records.
        qs = get_all_employees()
        serializer = EmployeeSerializer(qs, many=True)

        json_data = JSONRenderer().render(serializer.data)

        return self.render_to_http_response(json_data)

    def post(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            # if there is no valid json record, display provide valid json data message.
            json_data = json.dumps({'msg': 'Please provide valid json data.'})
            return self.render_to_http_response(json_data, status=400)

        # converting json data from test.py file into python dictionary
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)
        serializer = EmployeeSerializer(data=python_data)
        if serializer.is_valid():
            # when we called serializer.save() method internally create() method is called which is defined inside
            # serilizer class
            serializer.save()
            msg = {'msg': 'Resource created successfully'}
            json_data = JSONRenderer().render(msg)
            return self.render_to_http_response(json_data)
        json_data = JSONRenderer().render(serializer.errors)
        return self.render_to_http_response(json_data, status=404)

    def put(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            # if there is no valid json record, display provide valid json data message.
            json_data = json.dumps({'msg': 'Please provide valid json data.'})
            return self.render_to_http_response(json_data, status=400)

        # converting json data from test.py file into python dictionary
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)

        # checking provided_data contains id attribute or not
        id = python_data.get('id', None)

        # if provided_data contains id attribute then check provided id is present in database or not
        if id is not None:
            emp = get_emp_by_id(id)

            # if there is no matching id found, display no record found message.
            if emp is None:
                json_data = json.dumps({'msg': 'No such id present.'})
                return self.render_to_http_response(json_data, status=400)

            # with this if we tried to perform partial update, it won't work
            # it will ask for remaining fields also
            # serializer = EmployeeSerializer(emp, data=python_data)

            # if we want to perform partial update then we need one more extra parameter which partial=True
            serializer = EmployeeSerializer(emp, data=python_data, partial=True)

            if serializer.is_valid():
                serializer.save()
                msg = {'msg': 'Resource updated successfully'}
                json_data = JSONRenderer().render(msg)
                return self.render_to_http_response(json_data)
            json_data = JSONRenderer().render(serializer.errors)
            return self.render_to_http_response(json_data, status=400)
        json_data = json.dumps({'msg': 'Please provide id.'})
        return self.render_to_http_response(json_data, status=400)

    def delete(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            # if there is no valid json record, display provide valid json data message.
            json_data = json.dumps({'msg': 'Please provide valid json data.'})
            return self.render_to_http_response(json_data, status=400)

        # converting json data from test.py file into python dictionary
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)

        # checking provided_data contains id attribute or not
        id = python_data.get('id', None)

        # if provided_data contains id attribute then check provided id is present in database or not
        if id is not None:
            emp = get_emp_by_id(id)

            # if there is no matching id found, display no record found message.
            if emp is None:
                json_data = json.dumps({'msg': 'No such id present.'})
                return self.render_to_http_response(json_data, status=400)

            emp.delete()
            msg = {'msg': 'Resource Deleted successfully'}
            json_data = JSONRenderer().render(msg)
            return self.render_to_http_response(json_data)

        msg = {'msg': 'Unable to delete record.'}
        json_data = JSONRenderer().render(msg)
        return self.render_to_http_response(json_data)









