from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone

from master.models import Department
from master.forms import DepartmentForm

class DepartmentListView(LoginRequiredMixin, ListView):
    template_name = 'master/department/index.html'
    model = Department
    paginate_by = 10
    context_object_name = 'items'

    def get_queryset(self):
        return Department.objects.all()

class DepartmentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'master/department/create.html'
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy('master.department.index')

class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'master/department/update.html'
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy('master.department.index')
    context_object_name = 'item'

    def form_valid(self, form):
        Department = form.save(commit=False)
        Department.updated = timezone.now()
        Department.save()
        return super().form_valid(form)

class DepartmentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'master/department/delete.html'
    model = Department
    success_url = reverse_lazy('master.department.index')
    context_object_name = 'item'
