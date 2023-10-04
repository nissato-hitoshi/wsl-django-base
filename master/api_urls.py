from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .api_views import EmployeeViewSet, AffiliationViewSet, DepartmentViewSet, PositionViewSet, GradeViewSet

# 社員情報 Rest Api 登録
employee_router = DefaultRouter()
employee_router.register(r'', EmployeeViewSet)

# 所属情報 Rest Api 登録
affiliation_router = DefaultRouter()
affiliation_router.register(r'', AffiliationViewSet)

# 部門情報 Rest Api 登録
department_router = DefaultRouter()
department_router.register(r'', DepartmentViewSet)

# 役職 Rest Api 登録
position_router = DefaultRouter()
position_router.register(r'', PositionViewSet)

# 資格 Rest Api 登録
grade_router = DefaultRouter()
grade_router.register(r'', GradeViewSet)

# API用 Url定義
api_urlpatterns = [
    path('employees/', include(employee_router.urls)),
    path('affiliations/', include(affiliation_router.urls)),
    path('departments/', include(department_router.urls)),
    path('positions/', include(position_router.urls)),
    path('grades/', include(grade_router.urls)),
]
