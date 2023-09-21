from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .api_views import EmployeeViewSet, AffiliationViewSet

# 社員情報 Rest Api 登録
employee_router = DefaultRouter()
employee_router.register(r'', EmployeeViewSet)

# 所属情報 Rest Api 登録
affiliation_router = DefaultRouter()
affiliation_router.register(r'', AffiliationViewSet)

# API用 Url定義
api_urlpatterns = [
    path('employees/', include(employee_router.urls)),
    path('affiliations/', include(affiliation_router.urls)),
]

