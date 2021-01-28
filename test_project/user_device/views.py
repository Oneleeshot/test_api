from django.views.generic import ListView, DetailView, UpdateView, CreateView
from rest_framework.viewsets import ModelViewSet
from user_device.models import Device, Workers
from api.serializers import DevicesSerializer


class DeviceListView(ListView):
    model = Device
    template_name = "user_device/devices.html"
    ordering = "device"
    context_object_name = "devices"


class DeviceDetailView(DetailView):
    model = Device
    template_name = "user_device/device.html"
    slug_field = "pk"
    context_object_name = "device"


class WorkersListView(ListView):
    model = Workers
    template_name = "user_device/workers.html"
    ordering = "first_name"
    context_object_name = "workers"


class WorkersDetailView(DetailView):
    model = Workers
    template_name = "user_device/worker.html"
    slug_field = "id"
    context_object_name = "worker"


class EmployeeUpdateView(UpdateView):
    model = Workers
    template_name = "user_device/edit_workers.html"
    slug_field = "id"
    slug_url_kwarg = "id"
    context_object_name = "workers"
    fields = ["first_name", "last_name", "phone", "image", "company"]
    success_url = '/workers/'


class CreateWorkers(CreateView):
    model = Workers
    fields = ["first_name", "last_name", "phone", "image", "company"]
    template_name = 'user_device/create_workers.html'
    success_url = '/workers/'


class CreateDevice(CreateView):
    model = Device
    fields = ["device", "configuration", "price", "paid_by", "used_by",
              "comment", "start_date"]
    template_name = 'user_device/create_device.html'
    success_url = '/devices/'


class DeviceUpdateView(UpdateView):
    model = Device
    template_name = "user_device/edit_device.html"
    slug_field = "pk"
    slug_url_kwarg = "pk"
    context_object_name = "devices"
    fields = ["device", "configuration", "price", "paid_by", "used_by",
              "comment", "start_date"]
    success_url = '/devices/'


