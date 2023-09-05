from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .api_views import EmployeeViewSet

employee_router = DefaultRouter()
employee_router.register(r'', EmployeeViewSet)

