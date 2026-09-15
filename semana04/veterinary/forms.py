from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['pet_name', 'species', 'owner_name', 'reason', 'date']
        widgets = {
            'pet_name': forms.TextInput(attrs={'class': 'form-control'}),
            'species': forms.TextInput(attrs={'class': 'form-control'}),
            'owner_name': forms.TextInput(attrs={'class': 'form-control'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }