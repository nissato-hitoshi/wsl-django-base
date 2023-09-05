from rest_framework import serializers

from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id',
            'employee_no',
            'name',
            'email',
            'hire_date',
            'retirement_date',
            'updated',
            'created',
        )