from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import FacilityForm
from .models import Facility


class FacilityListView(LoginRequiredMixin, ListView):
    model = Facility
    template_name = "facilities/list.html"
    context_object_name = "facilities"

    def get_queryset(self):
        return Facility.objects.filter(owner=self.request.user)


class FacilityCreateView(LoginRequiredMixin, CreateView):
    model = Facility
    form_class = FacilityForm
    template_name = "facilities/form.html"
    success_url = reverse_lazy("facility-list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, "Facility saved.")
        return super().form_valid(form)


class FacilityUpdateView(LoginRequiredMixin, UpdateView):
    model = Facility
    form_class = FacilityForm
    template_name = "facilities/form.html"
    success_url = reverse_lazy("facility-list")

    def get_queryset(self):
        return Facility.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Facility updated.")
        return super().form_valid(form)


class FacilityDeleteView(LoginRequiredMixin, DeleteView):
    model = Facility
    template_name = "facilities/confirm_delete.html"
    success_url = reverse_lazy("facility-list")

    def get_queryset(self):
        return Facility.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Facility deleted.")
        return super().form_valid(form)
