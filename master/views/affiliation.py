from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone

from master.models import Affiliation
from master.forms import AffiliationForm

class AffiliationListView(LoginRequiredMixin, ListView):
    template_name = 'master/affiliation/index.html'
    model = Affiliation
    paginate_by = 10
    context_object_name = 'items'

    def get_queryset(self):
        return Affiliation.objects.all()

class AffiliationCreateView(LoginRequiredMixin, CreateView):
    template_name = 'master/affiliation/create.html'
    model = Affiliation
    form_class = AffiliationForm
    success_url = reverse_lazy('master.affiliation.index')

class AffiliationUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'master/affiliation/update.html'
    model = Affiliation
    form_class = AffiliationForm
    success_url = reverse_lazy('master.affiliation.index')
    context_object_name = 'item'

    def form_valid(self, form):
        Affiliation = form.save(commit=False)
        Affiliation.updated = timezone.now()
        Affiliation.save()
        return super().form_valid(form)

class AffiliationDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'master/affiliation/delete.html'
    model = Affiliation
    success_url = reverse_lazy('master.affiliation.index')
    context_object_name = 'item'
