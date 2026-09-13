from django.urls import path
from . import views

app_name = 'veterinary'

urlpatterns = [
    path('', views.appointment_list, name='list'),
    path('crear/', views.appointment_create, name='create'),
]