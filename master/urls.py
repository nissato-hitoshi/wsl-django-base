from django.urls import path, include

from .views import TopView
from .views import SampleView, AsyncView
from .views import EmployeeListView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView
from .views import GradeListView, GradeCreateView, GradeUpdateView, GradeDeleteView
from .views import PositionListView, PositionCreateView, PositionUpdateView, PositionDeleteView
from .views import DepartmentListView, DepartmentCreateView, DepartmentUpdateView, DepartmentDeleteView
from .views import AffiliationListView, AffiliationCreateView, AffiliationUpdateView, AffiliationDeleteView

urlpatterns = [

    # top
    path('', TopView.as_view(), name='master.top'),
    path('sample', SampleView.as_view(), name='master.sample'),
    path('async', AsyncView.as_view(), name='master.async'),
 
    # employee
    path('employee/index', EmployeeListView.as_view(), name='master.employee.index'),
    path('employee/create', EmployeeCreateView.as_view(), name='master.employee.create'),
    path('employee/update/<int:pk>/', EmployeeUpdateView.as_view(), name='master.employee.update'),
    path('employee/delete/<int:pk>/', EmployeeDeleteView.as_view(), name='master.employee.delete'),
 
    # grade
    path('grade/index', GradeListView.as_view(), name='master.grade.index'),
    path('grade/create', GradeCreateView.as_view(), name='master.grade.create'),
    path('grade/update/<int:pk>/', GradeUpdateView.as_view(), name='master.grade.update'),
    path('grade/delete/<int:pk>/', GradeDeleteView.as_view(), name='master.grade.delete'),
 
    # position
    path('position/index', PositionListView.as_view(), name='master.position.index'),
    path('position/create', PositionCreateView.as_view(), name='master.position.create'),
    path('position/update/<int:pk>/', PositionUpdateView.as_view(), name='master.position.update'),
    path('position/delete/<int:pk>/', PositionDeleteView.as_view(), name='master.position.delete'),
 
    # department
    path('department/index', DepartmentListView.as_view(), name='master.department.index'),
    path('department/create', DepartmentCreateView.as_view(), name='master.department.create'),
    path('department/update/<int:pk>/', DepartmentUpdateView.as_view(), name='master.department.update'),
    path('department/delete/<int:pk>/', DepartmentDeleteView.as_view(), name='master.department.delete'),
 
    # affiliation
    path('affiliation/index', AffiliationListView.as_view(), name='master.affiliation.index'),
    path('affiliation/create', AffiliationCreateView.as_view(), name='master.affiliation.create'),
    path('affiliation/update/<int:pk>/', AffiliationUpdateView.as_view(), name='master.affiliation.update'),
    path('affiliation/delete/<int:pk>/', AffiliationDeleteView.as_view(), name='master.affiliation.delete'),
]
