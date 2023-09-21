from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import Employee, Affiliation
from .serializers import EmployeeSerializer, AffiliationSerializer

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
    queryset = Affiliation.objects.all() 
    serializer_class = AffiliationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [\
          'employee__name'\
        , 'employee__employee_no'\
        , 'employee__email'\
        , 'department__department_name'\
        , 'position__position_name'\
        , 'grade__grade_name'\
    ]

