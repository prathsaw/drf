from django.http import HttpResponse

# It is an independent class which contains several instance methods. Whenever we required these instance methods
# inherit child class using this class.
# Mixin class act as a parent class, and provide functionality to child class.
# It is a direct child class of object class.
# We won't create object for mixin class as it not contains any instance variable.
# Main purpose is code re-usability.


class HttpResponseMixins(object):
    def render_to_http_response(self, json_data):
        # can handle 1000 lines of code.
        return HttpResponse(json_data, content_type='application/json')
