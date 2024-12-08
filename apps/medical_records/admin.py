from django.contrib import admin

from .models import MedicalRecord, MedicalPrescription, Exam, AccessHistory, Disease, DiseaseHistory, Diagnosis

admin.site.register(MedicalRecord)
admin.site.register(MedicalPrescription)
admin.site.register(Exam)
admin.site.register(AccessHistory)
admin.site.register(Disease)
admin.site.register(DiseaseHistory)
admin.site.register(Diagnosis)