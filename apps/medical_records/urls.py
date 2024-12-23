from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_all_and_post_medical_records, name='get_all_and_post_medical_records'),
    path('<int:id>/', views.get_put_and_delete_medical_record_by_id, name='get_put_and_delete_medical_record_by_id'),
    path('prescriptions/', views.get_all_and_post_medical_prescriptions, name='get_all_and_post_medical_prescriptions'),
    path('prescriptions/<int:id>/', views.get_put_and_delete_medical_prescription_by_id, name='get_put_and_delete_medical_prescription_by_id'),
    path('exams/', views.get_all_and_post_exams, name='get_all_and_post_exams'),
    path('exams/<int:id>/', views.get_put_and_delete_exam_by_id, name='get_put_and_delete_exam_by_id'),
    path('access-histories/', views.get_all_and_post_access_histories, name='get_all_and_post_access_histories'),
    path('access-histories/<int:id>/', views.get_put_and_delete_access_history_by_id, name='get_put_and_delete_access_history_by_id'),
    path('diseases/', views.get_all_and_post_diseases, name='get_all_and_post_diseases'),
    path('diseases/<int:id>/', views.get_put_and_delete_disease_by_id, name='get_put_and_delete_disease_by_id'),
    path('diseases-histories/', views.get_all_and_post_diseases_histories, name='get_all_and_post_diseases_histories'),
    path('diseases-histories/<int:id>/', views.get_put_and_delete_disease_history_by_id, name='get_put_and_delete_disease-history_by_id'),
    path('diagnostics/', views.get_all_and_post_diagnostics, name='get_all_and_post_diagnostics'),
    path('diagnostics/<int:id>/', views.get_put_and_delete_diagnosis_by_id, name='get_put_and_delete_diagnosis_by_id'),
]