from rest_framework import serializers

from .models import Clients, Events


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'


class EventsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['name', 'description']
