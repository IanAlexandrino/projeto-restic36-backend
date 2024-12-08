from rest_framework import serializers

from .models import MedicalRecord, MedicalPrescription, Exam, AccessHistory

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

class AccessHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessHistory
        fields = '__all__'
        read_only_fields = ['access_date_time']

    def validate(self, data):
        patient = data.get('patient')
        practitioner = data.get('practitioner')

        if not patient and not practitioner:
            raise serializers.ValidationError('It is necessary to list a Patient or a Practitioner.')
        if patient and practitioner:
            raise serializers.ValidationError('Only one of the fields (patient or practitioner) can be filled out.')
        
        return data