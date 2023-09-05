from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
import asyncio
from django.core import serializers
from master.models import Employee

class SampleView(LoginRequiredMixin, TemplateView):
    template_name = 'master/sample.html'


class AsyncView(View):

    # メソッドの先頭にasyncを付ける
#    async def get(self, request, *args, **kwargs):
    def get(self, request, *args, **kwargs):
        items = []
#        async for emp in Employee.objects.all():
#            items.append(emp)

#        post_list = serializers.serialize('json', posts)
#        return HttpResponse(",".join(items))
#        res = serializers.serialize('json', items)
        res = serializers.serialize('json', Employee.objects.all())
        return HttpResponse(res, content_type="text/json-comment-filtered; charset=utf8")
