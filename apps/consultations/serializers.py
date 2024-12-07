from rest_framework import serializers

from .models import Consultation, ConsultationType

class ConsultationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultationType
        fields = '__all__'

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = '__all__'