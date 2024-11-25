from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Masculine'),
        ('F', 'Feminine'),
    ]

    name = models.CharField(
        max_length=255,
        default='', 
        error_messages={
            'null': 'Name cannot be null',
            'blank': 'Name cannot be blank',
        },
    )
    date_birth = models.DateField(
        error_messages={
            'null': 'Date of birth cannot be null',
            'blank': 'Date of birth cannot be blank',
            'invalid': 'Invalid date format',
        },
    )
    sex = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='M',
        error_messages={
            'null': 'Sex cannot be null',
            'blank': 'Sex cannot be blank', 
            'max_length': 'Sex cannot be longer than 1 character',
        }
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

    def __str__(self):
        return f'Name: {self.name} | Sex: {self.sex} | CPF: {self.cpf} | Phone number: {self.phone_number}'