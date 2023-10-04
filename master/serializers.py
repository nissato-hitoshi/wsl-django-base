from rest_framework import serializers

from .models import Employee
from .models import Affiliation
from .models import Grade
from .models import Position
from .models import Department

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = "__all__"

class AffiliationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Affiliation
        fields = "__all__"
    
    employee = EmployeeSerializer(read_only=True)
    grade = GradeSerializer(read_only=True)
    position = PositionSerializer(read_only=True)
    department = DepartmentSerializer(read_only=True)
