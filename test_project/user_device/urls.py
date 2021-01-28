from django.urls import path

from user_device.views import *

app_name = 'user_device'

urlpatterns = [
    path('devices/', DeviceListView.as_view(), name='devices'),
    path('devices/<int:pk>/', DeviceDetailView.as_view(), name='device'),
    path('workers/', WorkersListView.as_view(), name='workers'),
    path('workers/<int:pk>/', WorkersDetailView.as_view(), name='worker'),
    path('workers/<int:pk>/edit/', EmployeeUpdateView.as_view(),
         name='edit_workers'),
    path('workers/new/', CreateWorkers.as_view(), name='new_worker'),
    path('devices/new/', CreateDevice.as_view(), name='devices'),
    path('devices/<int:pk>/edit/', DeviceUpdateView.as_view(), name='device'),

]
