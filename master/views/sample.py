from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from master.models import Employee

class SampleView(LoginRequiredMixin, TemplateView):
    template_name = 'master/sample.html'
