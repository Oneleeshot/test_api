from rest_framework.viewsets import ModelViewSet

from api.serializers import DevicesSerializer, WorkersSerializer
from user_device.models import Device, Workers


class DeviceViewSet(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DevicesSerializer


class WorkersViewSet(ModelViewSet):
    queryset = Workers.objects.all()
    serializer_class = WorkersSerializer

