from django.contrib import admin

from .models import Practitioner, PractitionerType

admin.site.register(Practitioner)
admin.site.register(PractitionerType)
