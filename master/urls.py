from django.urls import path, include

from .views import TopView
from .views import SampleView
from .views import EmployeeListView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView
from .views import GradeListView, GradeCreateView, GradeUpdateView, GradeDeleteView
from .views import PositionListView, PositionCreateView, PositionUpdateView, PositionDeleteView
from .views import DepartmentListView, DepartmentCreateView, DepartmentUpdateView, DepartmentDeleteView
from .views import AffiliationListView, AffiliationCreateView, AffiliationUpdateView, AffiliationDeleteView
from .views import AccountingPeriodListView, AccountingPeriodCreateView, AccountingPeriodUpdateView, AccountingPeriodDeleteView
from .views import CostListView, CostCreateView, CostUpdateView, CostDeleteView
from .views import ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView

urlpatterns = [

    # top
    path('', TopView.as_view(), name='master.top'),
    path('sample', SampleView.as_view(), name='master.sample'),
 
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

    # accounting_period
    path('accounting_period/index', AccountingPeriodListView.as_view(), name='master.accounting_period.index'),
    path('accounting_period/create', AccountingPeriodCreateView.as_view(), name='master.accounting_period.create'),
    path('accounting_period/update/<int:pk>/', AccountingPeriodUpdateView.as_view(), name='master.accounting_period.update'),
    path('accounting_period/delete/<int:pk>/', AccountingPeriodDeleteView.as_view(), name='master.accounting_period.delete'),

    # cost
    path('cost/index', CostListView.as_view(), name='master.cost.index'),
    path('cost/create', CostCreateView.as_view(), name='master.cost.create'),
    path('cost/update/<int:pk>/', CostUpdateView.as_view(), name='master.cost.update'),
    path('cost/delete/<int:pk>/', CostDeleteView.as_view(), name='master.cost.delete'),

    # client
    path('client/index', ClientListView.as_view(), name='master.client.index'),
    path('client/create', ClientCreateView.as_view(), name='master.client.create'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='master.client.update'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='master.client.delete'),

]
