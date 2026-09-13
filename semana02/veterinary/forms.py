from django import forms

class AppointmentForm(forms.Form):
    pet_name = forms.CharField(label="Mascota", max_length=100)
    species = forms.CharField(label="Especie", max_length=100)
    owner_name = forms.CharField(label="Dueño", max_length=100)
    reason = forms.CharField(label="Motivo", widget=forms.Textarea)
    date = forms.DateField(label="Fecha", widget=forms.DateInput(attrs={'type': 'date'}))