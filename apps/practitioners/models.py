from django.db import models
from ..institutions.models import Institution

class PractitionerType(models.Model):
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
    

class Practitioner(models.Model):
    name = models.CharField(
        max_length=255,
        default='', 
        error_messages={
            'null': 'Name cannot be null',
            'blank': 'Name cannot be blank',
        },
    )
    cpf = models.CharField(
        max_length=11,
        unique=True,
        default='',
        error_messages={
            'null': 'CPF cannot be null',
            'blank': 'CPF cannot be blank',
            'max_length': 'CPF cannot be longer than 11 characters',
            'unique': 'CPF is already in use',
        },
    )
    registration = models.CharField(
        max_length=50,
        unique=True,
        error_messages={
            'null': 'Registration cannot be null',
            'blank': 'Registration cannot be blank',
            'max_length': 'Registration cannot be longer than 50 characters',
            'unique': 'Registration is already in use',
        }
    )
    practitioner_type = models.ForeignKey(
        PractitionerType,
        on_delete=models.CASCADE, 
        related_name='practitioners'
    )
    practitioner_institution = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE,
        related_name='practitioners'
    )

    def __str__(self):
        return f'Name: {self.name} | Registration: {self.registration} | Practitioner Type: {self.practitioner_type} | Institution: {self.practitioner_institution.name}'
