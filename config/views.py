from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

import asyncio
from django.http import HttpResponse
from django.views import View

from master.models import Employee
 

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


class AsyncView(View):
    # メソッドの先頭にasyncを付ける
    async def get(self, request, *args, **kwargs):
        items = []
        async for emp in Employee.objects.all():
            items.append(emp.name)
        return HttpResponse(",".join(items))
    