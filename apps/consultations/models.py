from django.db import models

from ..patients.models import Patient
from ..practitioners.models import Practitioner
from ..institutions.models import Institution

class ConsultationType(models.Model):
    description = models.CharField(
        max_length=255, 
        unique=True,
        default='',
        error_messages={
            'null': 'Description cannot be null',
            'blank': 'Description cannot be blank',
            'unique': 'Description is already in use',
        },
    )

    def __str__(self):
        return self.description
    
class Consultation(models.Model):
    consultation_date = models.DateField(
        error_messages={
            'null': 'Consultation date cannot be null',
            'blank': 'Consultation date cannot be blank',
            'invalid': 'Invalid date format',
        },
    )
    consultation_type = models.ForeignKey(
        ConsultationType, 
        on_delete=models.CASCADE, 
        related_name='consultations'
    )
    consultation_patient = models.ForeignKey(
        Patient, 
        on_delete=models.CASCADE, 
        related_name='consultations'
    )
    consultation_practitioner = models.ForeignKey(
        Practitioner, 
        on_delete=models.CASCADE, 
        related_name='consultations'
    )
    consultation_institution = models.ForeignKey(
        Institution, 
        on_delete=models.CASCADE, 
        related_name='consultations'
    )
