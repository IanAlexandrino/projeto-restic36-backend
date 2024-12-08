from django.contrib import admin

from .models import MedicalRecord, MedicalPrescription, Exam, AccessHistory

admin.site.register(MedicalRecord)
admin.site.register(MedicalPrescription)
admin.site.register(Exam)
admin.site.register(AccessHistory)