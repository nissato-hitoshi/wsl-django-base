from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone

from master.models import Position
from master.forms import PositionForm

class PositionListView(LoginRequiredMixin, ListView):
    template_name = 'master/position/index.html'
    model = Position
    paginate_by = 10
    context_object_name = 'items'

    def get_queryset(self):
        return Position.objects.all()

class PositionCreateView(LoginRequiredMixin, CreateView):
    template_name = 'master/position/create.html'
    model = Position
    form_class = PositionForm
    success_url = reverse_lazy('master.position.index')

class PositionUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'master/position/update.html'
    model = Position
    form_class = PositionForm
    success_url = reverse_lazy('master.position.index')
    context_object_name = 'item'

    def form_valid(self, form):
        Position = form.save(commit=False)
        Position.updated = timezone.now()
        Position.save()
        return super().form_valid(form)

class PositionDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'master/position/delete.html'
    model = Position
    success_url = reverse_lazy('master.position.index')
    context_object_name = 'item'
