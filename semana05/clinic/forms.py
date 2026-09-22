from django import forms
from .models import Patient, Doctor, Specialty, MedicalSupply, Office, OfficeSupply

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'dni', 'phone']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

# Formulario para el Ejercicio 13 (Modelo Intermedio OfficeSupply)
class OfficeSupplyForm(forms.ModelForm):
    class Meta:
        model = OfficeSupply
        fields = ['office', 'supply', 'quantity']
        widgets = {
            'office': forms.Select(attrs={'class': 'form-control'}),
            'supply': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }