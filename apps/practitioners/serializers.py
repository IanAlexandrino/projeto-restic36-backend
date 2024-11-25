from rest_framework import serializers

from .models import Practitioner, PractitionerType

class PractitionerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PractitionerType
        fields = '__all__'

class PractitionerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practitioner
        fields = '__all__'