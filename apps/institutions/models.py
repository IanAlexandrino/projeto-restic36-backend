from django.db import models

class InstitutionType(models.Model):
    description = models.CharField(
        max_length=255, 
        unique=True,
        error_messages={
            'null': 'Description cannot be null',
            'blank': 'Description cannot be blank',
            'unique': 'Description is already in use',
        },
    )

    def __str__(self):
        return self.description

class Institution(models.Model):
    name = models.CharField(
        max_length=255,
        default='', 
        error_messages={
            'null': 'Name cannot be null',
            'blank': 'Name cannot be blank',
        },
    )
    address = models.CharField(
        max_length=255, 
        default='', 
        error_messages={
            'null': 'Address cannot be null',
            'blank': 'Address cannot be blank',
        },
    )
    phone_number = models.CharField(
        max_length=15,
        unique=True, 
        default='', 
        error_messages={
            'null': 'Phone number cannot be null',
            'blank': 'Phone number cannot be blank',
            'max_length': 'Phone number cannot be longer than 15 characters',
            'unique': 'Phone number is already in use',
        },
    )
    email = models.EmailField(
        unique=True, 
        default='',
        error_messages={
            'null': 'Email cannot be null',
            'blank': 'Email cannot be blank',
            'invalid': 'Email must be valid',
            'unique': 'Email is already in use',
        }, 
    )
    type = models.ForeignKey(
        InstitutionType, 
        on_delete=models.CASCADE, 
        related_name='institutions'
    )
    

    def __str__(self):
        return self.name