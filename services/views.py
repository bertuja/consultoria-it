from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Service
from .forms import ServiceForm

class ServiceListView(ListView):
    model = Service
    template_name = 'services/service_list.html'
    context_object_name = 'servicios'
    ordering = ['-fecha_creacion']

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'
    context_object_name = 'servicio'

class ServiceCreateView(LoginRequiredMixin, CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'services/service_form.html'
    success_url = reverse_lazy('service_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class ServiceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Service
    fields = ['titulo', 'categoria', 'contenido', 'imagen']
    template_name = 'services/service_form.html'  # reutilizamos el mismo formulario
    success_url = reverse_lazy('service_list')

    def test_func(self):
        service = self.get_object()
        return self.request.user == service.autor

class ServiceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Service
    template_name = 'services/service_confirm_delete.html'
    success_url = reverse_lazy('service_list')

    def test_func(self):
        service = self.get_object()
        return self.request.user == service.autor
