from django.contrib import admin
from django.urls import path
from apps.institutions.views import institutions, institutions_types

urlpatterns = [
    path('institutions/', institutions),
    path('institutions-types/', institutions_types),
]