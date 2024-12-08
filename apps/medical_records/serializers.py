from rest_framework import serializers

from .models import MedicalRecord, MedicalPrescription, Exam

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'

class MedicalPrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalPrescription
        fields = '__all__'

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'