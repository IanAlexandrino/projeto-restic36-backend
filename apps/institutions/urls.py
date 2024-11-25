from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_all_and_post_institutions, name='get_all_and_post_institutions'),
    path('<int:id>/', views.get_put_and_delete_institution_by_id, name='get_put_and_delete_institution_by_id'),
    path('types/', views.get_all_and_post_institution_types, name='get_all_and_post_intitution_types'),
    path('types/<int:id>/', views.get_put_and_delete_institution_type_by_id, name='get_put_and_delete_institution_type_by_id'),
]