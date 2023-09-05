from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone

from master.models import Grade
from master.forms import GradeForm

class GradeListView(LoginRequiredMixin, ListView):
    template_name = 'master/grade/index.html'
    model = Grade
    paginate_by = 10
    context_object_name = 'items'

    def get_queryset(self):
        return Grade.objects.all()

class GradeCreateView(LoginRequiredMixin, CreateView):
    template_name = 'master/grade/create.html'
    model = Grade
    form_class = GradeForm
    success_url = reverse_lazy('master.grade.index')

class GradeUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'master/grade/update.html'
    model = Grade
    form_class = GradeForm
    success_url = reverse_lazy('master.grade.index')
    context_object_name = 'item'

    def form_valid(self, form):
        Grade = form.save(commit=False)
        Grade.updated = timezone.now()
        Grade.save()
        return super().form_valid(form)

class GradeDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'master/grade/delete.html'
    model = Grade
    success_url = reverse_lazy('master.grade.index')
    context_object_name = 'item'
