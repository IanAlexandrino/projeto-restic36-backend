from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_all_and_post_medical_records, name='get_all_and_post_medical_records'),
    path('<int:id>/', views.get_put_and_delete_medical_record_by_id, name='get_put_and_delete_medical_record_by_id'),
    path('prescriptions/', views.get_all_and_post_medical_prescriptions, name='get_all_and_post_medical_prescriptions'),
    path('prescriptions/<int:id>/', views.get_put_and_delete_medical_prescription_by_id, name='get_put_and_delete_medical_prescription_by_id'),
    path('exams/', views.get_all_and_post_exams, name='get_all_and_post_exams'),
    path('exams/<int:id>/', views.get_put_and_delete_exam_by_id, name='get_put_and_delete_exam_by_id'),
]