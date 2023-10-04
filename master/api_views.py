from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import Employee, Affiliation, Department, Position, Grade
from .serializers import EmployeeSerializer, AffiliationSerializer, DepartmentSerializer, PositionSerializer, GradeSerializer

class EmployeeViewSet(ReadOnlyModelViewSet):
    queryset = Employee.objects.all() 
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [\
          'name'\
        , 'employee_no'\
        , 'email'\
    ]

class AffiliationViewSet(ReadOnlyModelViewSet):
    queryset = Affiliation.objects.filter()
    serializer_class = AffiliationSerializer
    filter_fields = ('accounting_period',)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = [\
          'employee__name'\
        , 'employee__employee_no'\
        , 'employee__email'\
        , 'department__department_name'\
        , 'position__position_name'\
        , 'grade__grade_name'\
    ]

class DepartmentViewSet(ReadOnlyModelViewSet):
    queryset = Department.objects.all() 
    serializer_class = DepartmentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['department_code', 'department_name']

class PositionViewSet(ReadOnlyModelViewSet):
    queryset = Position.objects.all() 
    serializer_class = PositionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['position_code', 'position_name']

class GradeViewSet(ReadOnlyModelViewSet):
    queryset = Grade.objects.all() 
    serializer_class = GradeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['grade_code', 'grade_name']
