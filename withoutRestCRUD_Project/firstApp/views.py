import json
from django.http import HttpResponse
from django.views.generic import View
from firstApp.models import Employee
from firstApp.utils import is_json, get_emp_by_id
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from firstApp.forms import EmployeeForm
from firstApp.mixins import SerializeMixin, HttpResponseMixin


# # Retrieve based on id

# class EmployeeDetailCBV(View):
#     def get(self, request, id, *args, **kwargs):
#         emp = Employee.objects.get(id=id)
#         # -----------------------------------------
#         # # serializing data manually using python inbuilt module json i.e. json.dump()
#
#         # emp_data = {
#         #     'enum': emp.enum,
#         #     'ename': emp.ename,
#         #     'esal': emp.esal,
#         #     'ecity': emp.ecity,
#         # }
#         # json_data = json.dumps(emp_data)
#         # -----------------------------------------
#         # # serializing data using django's inbuilt function i.e. serialize('json', qs)
#         json_data = serialize('json', [emp,])
#
#         python_data = json.loads(json_data)
#         final_list = []
#         for obj in python_data:
#             emp_data = obj['fields']
#             final_list.append(emp_data)
#         json_data = json.dumps(final_list)
#
#         # # if we want to display only particular fields to end user then
#         # json_data = serialize('json', [emp, ], fields=('enum', 'ename', 'ecity'))
#         return HttpResponse(json_data, content_type='application/json')


# Using Mixin Class we can reduce above code considerably

@method_decorator(csrf_exempt, name='dispatch')
class EmployeeDetailCBV(HttpResponseMixin, SerializeMixin, View):
    def get(self, request, id, *args, **kwargs):
        try:
            emp = Employee.objects.get(id=id)

        except Employee.DoesNotExist:
            json_data = json.dumps({'msg': 'The requested resource is not available.'})
            return self.render_to_http_response(json_data, status=404)

        else:
            json_data = self.serializeData([emp, ])
        return self.render_to_http_response(json_data)

    # ------------------------------------------------------------------------------------------------------------------

    # Update operation
    def put(self, request, id, *args, **kwargs):
        # checking if there is an employee with provided id is present or not
        # for that we have custom method in utils.py file

        emp = get_emp_by_id(id)
        if emp is None:
            # if there is no employee record found, display no record found message.
            json_data = json.dumps({'msg': 'No employee found to perform update operation.'})
            return self.render_to_http_response(json_data, status=400)

        # fetching data from test.py file
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

    # ------------------------------------------------------------------------------------------------------------------

    # Delete operation
    def delete(self, request, id, *args, **kwargs):
        emp = get_emp_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg': 'No employee found to perform delete operation.'})
            return self.render_to_http_response(json_data, status=400)

        # emp.delete() returns tuple containing two items.
        # we use tuple unpacking concept to store that items in separate variables.
        status, deleted_item = emp.delete()

        if status == 1:
            json_data = json.dumps({'msg': 'Record deleted successfully.'})
            return self.render_to_http_response(json_data)
        else:
            json_data = json.dumps({'msg': 'Unable to delete record.'})
            return self.render_to_http_response(json_data, status=400)


# ----------------------------------------------------------------------------------------------------------------------

# Retrieve all records
@method_decorator(csrf_exempt, name='dispatch')
class EmployeeListCBV(HttpResponseMixin, SerializeMixin, View):
    def get(self, request, *args, **kwargs):
        qs = Employee.objects.all()
        json_data = self.serializeData(qs)
        return self.render_to_http_response(json_data)

    # Post new record
    def post(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'Please provide json valid data'})
            return self.render_to_http_response(json_data, status=400)
        empdata = json.loads(data)
        form = EmployeeForm(empdata)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Record saved successfully'})
            return self.render_to_http_response(json_data)
        if form.errors():
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=400)

# ----------------------------------------------------------------------------------------------------------------------
