from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone

class TopView(LoginRequiredMixin, TemplateView):
    template_name = 'master/top.html'
