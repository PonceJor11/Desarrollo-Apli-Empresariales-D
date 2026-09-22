from django.urls import path
from . import views

urlpatterns = [
    # --- CRUD PACIENTES (EJERCICIO 7) ---
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/create/', views.patient_create, name='patient_create'),
    path('patients/<int:pk>/edit/', views.patient_update, name='patient_update'),
    path('patients/<int:pk>/delete/', views.patient_delete, name='patient_delete'),
    
    # --- CONSULTAS OPTIMIZADAS (EJERCICIO 6 Y 12) ---
    path('doctors-consultations/', views.doctor_consultations_view, name='doctor_consultations'),
    path('expanded-relations/', views.expanded_relations_view, name='expanded_relations'),

    path('office-supplies/', views.office_supply_list, name='office_supply_list'),
    path('office-supplies/create/', views.office_supply_create, name='office_supply_create'),
    path('office-supplies/<int:pk>/edit/', views.office_supply_update, name='office_supply_update'),
    path('office-supplies/<int:pk>/delete/', views.office_supply_delete, name='office_supply_delete'),
]