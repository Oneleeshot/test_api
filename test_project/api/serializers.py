from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from user_device.models import Device, Workers


class DevicesSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class WorkersSerializer(ModelSerializer):
    devices = serializers.SerializerMethodField()

    class Meta:
        model = Workers
        fields = '__all__'

    def get_devices(self, obj):
        devices = Device.objects.filter(used_by=obj)
        s = DevicesSerializer(devices, many=True, context=self.context)
        return s.data
