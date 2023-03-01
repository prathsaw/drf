from rest_framework import serializers
from firstApp.models import Employee


# ----------------------------------------------------------------------------------------------------------------------
# Using serializers
# ----------------------------------------------------------------------------------------------------------------------


# def multiple_of_thousand(value):
#     if value % 1000 != 0:
#         raise serializers.ValidationError('Employee salary should be multiple of 1000')
#
#
# class EmployeeSerializer(serializers.Serializer):
#     enum = serializers.IntegerField()
#     ename = serializers.CharField(max_length=128)
#     esal = serializers.FloatField(validators=[multiple_of_thousand, ])
#     ecity = serializers.CharField(max_length=128)
#
#     # field level validation
#     def validate_esal(self, value):
#         if value < 100000:
#             raise serializers.ValidationError('The minimum salary should be 100000')
#         return value
#
#     # object level validation - this data field is python_dictionary
#     def validate(self, data):
#         ename = data.get('ename')
#         esal = data.get('esal')
#         if ename.lower() == 'prathamesh':
#             if esal < 200000:
#                 raise serializers.ValidationError("Prathames's salary should not be less than 200000")
#         return data
#
#     # if we want to perform post operations then we need to override create() method inside Serializer class
#     def create(self, validated_data):
#         return Employee.objects.create(**validated_data)
#
#     # if we want to perform update operations then we need to override update() method inside Serializer class
#     # update method receives current object instance and validated_data
#     def update(self, instance, validated_data):
#         # if validated_data contains 'enum' field then 'enum' field of current object instance get updated otherwise
#         # it remains same
#         instance.enum = validated_data.get('enum', instance.enum)
#         instance.ename = validated_data.get('ename', instance.enum)
#         instance.esal = validated_data.get('esal', instance.esal)
#         instance.ecity = validated_data.get('ecity', instance.ecity)
#         instance.save()
#         return instance

# ----------------------------------------------------------------------------------------------------------------------
# Using Model serializers
# ----------------------------------------------------------------------------------------------------------------------
def multiple_of_thousand(value):
    if value % 1000 != 0:
        raise serializers.ValidationError('Employee salary should be multiple of 1000')


class EmployeeSerializer(serializers.ModelSerializer):
    esal = serializers.FloatField(validators=[multiple_of_thousand, ])

    class Meta:
        model = Employee
        fields = '__all__'

        # field level validation
        def validate_esal(self, value):
            if value < 100000:
                raise serializers.ValidationError('The minimum salary should be 100000')
            return value

        # object level validation - this data field is python_dictionary
        def validate(self, data):
            ename = data.get('ename')
            esal = data.get('esal')
            if ename.lower() == 'prathamesh':
                if esal < 200000:
                    raise serializers.ValidationError("Prathames's salary should not be less than 200000")
            return data
