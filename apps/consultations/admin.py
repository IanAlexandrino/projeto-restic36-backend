from django.contrib import admin

from .models import Consultation, ConsultationType

admin.site.register(Consultation)
admin.site.register(ConsultationType)