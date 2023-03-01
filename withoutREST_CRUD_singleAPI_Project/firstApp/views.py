import json
from firstApp.models import Employee
from firstApp.forms import EmployeeForm
from django.views.generic import View
from firstApp.utils import get_emp_by_id, is_json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from firstApp.mixins import SerializeMixin, HttpResponseMixin


# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCBV(HttpResponseMixin, SerializeMixin, View):
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
        provided_data = json.loads(data)

        # checking provided_data contains id attribute or not
        id = provided_data.get('id', None)

        # if provided_data contains id attribute then check provided id is present in database or not
        if id is not None:
            emp = get_emp_by_id(id)

            # if there is no matching id found, display no record found message.
            if emp is None:
                json_data = json.dumps({'msg': 'No such id present.'})
                return self.render_to_http_response(json_data, status=400)

            # if matching id found then fetch record corresponding to that id.

            json_data = self.serializeData([emp, ])
            return self.render_to_http_response(json_data)

        # if provided_data contains no id attribute then get all employee records.
        qs = Employee.objects.all()

        # converting queryset data into json data using custom serializeData() function written mixins.py file.
        json_data = self.serializeData(qs)
        return self.render_to_http_response(json_data)

    # ------------------------------------------------------------------------------------------------------------------

    # Create new record
    def post(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'Please provide json valid data'})
            return self.render_to_http_response(json_data, status=400)

        # if data received from partner application is in valid json format, then first convert it into python data.
        python_data = json.loads(data)

        # then pass python data to form class to create form object.
        form = EmployeeForm(python_data)

        # if data is cleaned then save it into database using form.save() method
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Record saved successfully'})
            return self.render_to_http_response(json_data)

        # if data failed to pass any validation check then display error message.
        if form.errors():
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=400)

    # ------------------------------------------------------------------------------------------------------------------

    # Update records

    def put(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'Please provide json valid data'})
            return self.render_to_http_response(json_data, status=400)

        # if data received from partner application is in valid json format, then first convert it into python data.
        provided_data = json.loads(data)

        # checking provided_data contains id attribute or not
        id = provided_data.get('id', None)

        # if provided_data contains id attribute then check provided id is present in database or not
        if id is not None:
            emp = get_emp_by_id(id)

            # if there is no matching id found, display no record found message.
            if emp is None:
                json_data = json.dumps({'msg': 'No such id present.'})
                return self.render_to_http_response(json_data, status=400)

            # if matching id found, then
            # we can get original data by using emp object
            original_data = {
                'enum': emp.enum,
                'ename': emp.ename,
                'esal': emp.esal,
                'ecity': emp.ecity,
            }

            # now update provided data into original_data
            original_data.update(provided_data)

            # we create form object using original data. we use argument instance which represent changes perform on
            # specified object only.
            form = EmployeeForm(original_data, instance=emp)

            # if form is valid the updated data save inside database table.
            if form.is_valid():
                form.save(commit=True)
                json_data = json.dumps({'msg': 'Record updated successfully.'})
                return self.render_to_http_response(json_data)

            if form.errors():
                json_data = json.dumps(form.errors)
                return self.render_to_http_response(json_data, status=400)

        # if id is None, then display provide id message
        json_data = json.dumps({'msg': 'Please provide id to update record'})
        return self.render_to_http_response(json_data, status=400)

    # ------------------------------------------------------------------------------------------------------------------

    # Delete record

    def delete(self, request, *args, **kwargs):
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
        provided_data = json.loads(data)

        # checking provided_data contains id attribute or not
        id = provided_data.get('id', None)

        # if provided_data contains id attribute then check provided id is present in database or not
        if id is not None:
            emp = get_emp_by_id(id)

            # if there is no matching id found, display no record found message.
            if emp is None:
                json_data = json.dumps({'msg': 'No such id present.'})
                return self.render_to_http_response(json_data, status=400)

            # if matching id found, then delete that particular record
            # emp.delete() returns tuple containing two items.
            # we use tuple unpacking concept to store that items in separate variables.
            status, deleted_item = emp.delete()

            if status == 1:
                json_data = json.dumps({'msg': 'Record deleted successfully.'})
                return self.render_to_http_response(json_data)
            else:
                json_data = json.dumps({'msg': 'Unable to delete record.'})
                return self.render_to_http_response(json_data, status=400)

        # if id is None, then display provide id message
        json_data = json.dumps({'msg': 'Please provide id to delete record'})
        return self.render_to_http_response(json_data, status=400)




