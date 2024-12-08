from django.db import models

from django.core.exceptions import ValidationError

from ..patients.models import Patient
from ..practitioners.models import Practitioner
from ..institutions.models import Institution

class MedicalRecord(models.Model):
    creation_date = models.DateField(
        error_messages={
            'null': 'Creation date cannot be null',
            'blank': 'Creation date cannot be blank',
            'invalid': 'Invalid date format',
        },
    )
    patient = models.ForeignKey(
        Patient, 
        on_delete=models.CASCADE, 
        related_name='medical_records'
    )
    practitioner = models.ForeignKey(
        Practitioner, 
        on_delete=models.CASCADE, 
        related_name='medical_records'
    )
    institution = models.ForeignKey(
        Institution, 
        on_delete=models.CASCADE, 
        related_name='medical_records'
    )

    def clean(self):
        if self.patient_medical_record.institution != self.institution_medical_record:
            raise ValidationError('The patient does not belong to the associated medical_record.')

        if self.practitioner_medical_record.institution != self.institution_medical_record:
            raise ValidationError('The doctor does not belong to the associated medical_record.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Creation Date: {self.creation_date} | Patient: {self.patient} | Practitioner: {self.practitioner} | Institution: {self.institution}'


class MedicalPrescription(models.Model):
    medication = models.CharField(
        max_length=100,
        error_messages={
            'null': 'Medication cannot be null',
            'blank': 'Medication cannot be blank',
        },
    )
    dosage = models.CharField(
        max_length=50,
        error_messages={
            'null': 'Dosage cannot be null',
            'blank': 'Dosage cannot be blank',
        },
    )
    frequency = models.CharField(
        max_length=50,
        error_messages={
            'null': 'Frequency cannot be null',
            'blank': 'Frequency cannot be blank',
        },
    )
    prescription_date = models.DateField(
        auto_now_add=True,
    )
    patient = models.ForeignKey(
        Patient, 
        on_delete=models.CASCADE, 
        related_name='medical_prescriptions'
    )
    practitioner = models.ForeignKey(
        Practitioner, 
        on_delete=models.CASCADE, 
        related_name='medical_prescriptions'
    )
    institution = models.ForeignKey(
        Institution, 
        on_delete=models.CASCADE, 
        related_name='medical_prescriptions'
    )

    def clean(self):
        if self.patient.institution != self.institution:
            raise ValidationError('The patient does not belong to the associated medical_prescription.')
        if self.practitioner.institution != self.institution:
            raise ValidationError('The doctor does not belong to the associated medical_prescription.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Medication: {self.medication} | Dosage: {self.dosage} | Frequency: {self.frequency} | Patient: {self.patient} | Practitioner: {self.practitioner}'
    

class Exam(models.Model):
    exam_type = models.CharField(
        max_length=50,
        error_messages={
            'null': 'Exam type cannot be null',
            'blank': 'Exam type cannot be blank',
        },
    )
    exam_date = models.DateField(
        error_messages={
            'null': 'Exam date cannot be null',
            'blank': 'Exam date cannot be blank',
            'invalid': 'Invalid date format',
        },
    )
    result = models.TextField(
        default='',
        blank=True, 
        null=True,
    )
    patient = models.ForeignKey(
        Patient, 
        on_delete=models.CASCADE, 
        related_name='exams'
    )
    practitioner = models.ForeignKey(
        Practitioner, 
        on_delete=models.CASCADE, 
        related_name='exams'
    )
    institution = models.ForeignKey(
        Institution, 
        on_delete=models.CASCADE, 
        related_name='exams'
    )

    def clean(self):
        if self.patient.institution != self.institution:
            raise ValidationError('The patient does not belong to the associated exam.')
        if self.practitioner.institution != self.institution:
            raise ValidationError('The doctor does not belong to the associated exam.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Exam type: {self.exam_type} | Exam date: {self.exam_date} | Result: {self.result} | Patient: {self.patient} | Institution: {self.institution}'
    

class AccessHistory(models.Model):
    access_date_time = models.DateTimeField(
        auto_now_add=True
    )
    access_type = models.CharField(
        max_length=50,
        error_messages={
            'null': 'Access type cannot be null',
            'blank': 'Access type cannot be blank',
        },
    )
    practitioner = models.ForeignKey(
        Practitioner, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL,
    )
    patient = models.ForeignKey(
        Patient, 
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def clean(self):
        if not self.paciente and not self.profissional:
            raise ValidationError('It must be related to a Patient or Practitioner.')
        if self.paciente and self.profissional:
            raise ValidationError('It cannot be related to both Patient and Practitioner at the same time.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        if self.paciente:
            return f'Access by Paciente: {self.paciente.nome} at {self.access_time}'
        elif self.profissional:
            return f'Access by Profissional: {self.profissional.nome} at {self.access_time}'