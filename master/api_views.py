from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(ReadOnlyModelViewSet):
    queryset = Employee.objects.all() 
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'employee_no', 'email']

