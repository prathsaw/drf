from django.core.serializers import serialize
from django.http import HttpResponse
import json


class SerializeMixin(object):
    def serializeData(self, qs):
        # Response contains some extra meta data
        # json_data = serialize('json', qs)
        # To remove extra meta data from response
        json_data = serialize('json', qs, fields=('enum', 'ename', 'ecity'))

        python_data = json.loads(json_data)
        final_list = []
        for obj in python_data:
            emp_data = obj['fields']
            final_list.append(emp_data)
        json_data = json.dumps(final_list)
        return json_data


class HttpResponseMixin(object):
    def render_to_http_response(self, json_data, status=200):
        return HttpResponse(json_data, content_type='application/json', status=status)
