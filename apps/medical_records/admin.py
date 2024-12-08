from django.contrib import admin

from .models import MedicalRecord, MedicalPrescription, Exam

admin.site.register(MedicalRecord)
admin.site.register(MedicalPrescription)
admin.site.register(Exam)