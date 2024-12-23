from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/institutions/', include('apps.institutions.urls')),
    path('api/practitioners/', include('apps.practitioners.urls')),
    path('api/patients/', include('apps.patients.urls')),
    path('api/consultations/', include('apps.consultations.urls')),
    path('api/medical-records/', include('apps.medical_records.urls')),
]
