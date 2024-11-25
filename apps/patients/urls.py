from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_all_and_post_patients, name='get_all_and_post_patients'),
    path('<int:id>/', views.get_put_and_delete_patient_by_id, name='get_put_and_delete_patient_by_id'),
]