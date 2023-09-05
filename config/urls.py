"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import HomeView, AsyncView

from master.api_urls import employee_router

# API用 Url定義
api_urlpatterns = [
    path('employees/', include(employee_router.urls)),
]

# 通常 Url定義
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('account/', include('allauth.urls')),
    path('master/', include('master.urls')),
    path('async/', AsyncView.as_view(), name='async'),
    path('api/1.0/', include(api_urlpatterns)),
]
