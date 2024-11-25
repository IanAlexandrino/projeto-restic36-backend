from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_all_and_post_practitioners, name='get_all_and_post_practitioners'),
    path('<int:id>/', views.get_put_and_delete_practitioner_by_id, name='get_put_and_delete_practitioner_by_id'),
    path('types/', views.get_all_and_post_practitioner_types, name='get_all_and_post_practitioner_types'),
    path('types/<int:id>/', views.get_put_and_delete_practitioner_type_by_id, name='get_put_and_delete_practitioner_type_by_id'),
]