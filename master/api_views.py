from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(ReadOnlyModelViewSet):
    queryset = Employee.objects.all() 
    serializer_class = EmployeeSerializer