from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_all_and_post_consultations, name='get_all_and_post_consultations'),
    path('<int:id>/', views.get_put_and_delete_consultation_by_id, name='get_put_and_delete_consultation_by_id'),
    path('types/', views.get_all_and_post_consultation_types, name='get_all_and_post_consultation_types'),
    path('types/<int:id>/', views.get_put_and_delete_consultation_type_by_id, name='get_put_and_delete_consultation_type_by_id'),
]