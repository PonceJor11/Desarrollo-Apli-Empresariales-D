from django import forms

class AppointmentForm(forms.Form):
    pet_name = forms.CharField(
        label="Nombre de la Mascota", 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    species = forms.CharField(
        label="Especie", 
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    owner_name = forms.CharField(
        label="Nombre del Dueño", 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    reason = forms.CharField(
        label="Motivo de Consulta", 
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    )
    date = forms.DateField(
        label="Fecha de Atención", 
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )