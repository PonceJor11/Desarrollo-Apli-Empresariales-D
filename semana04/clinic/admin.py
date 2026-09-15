from django.contrib import admin
from .models import (
    Patient, 
    Specialty, 
    Doctor, 
    MedicalSupply, 
    Office, 
    MedicalHistory, 
    MedicalAppointment, 
    Consultation, 
    Prescription, 
    Medication
)

# Registrar modelos para verlos en el Admin
admin.site.register(Patient)
admin.site.register(Specialty)
admin.site.register(Doctor)
admin.site.register(MedicalSupply)
admin.site.register(Office)
admin.site.register(MedicalHistory)
admin.site.register(MedicalAppointment)
admin.site.register(Consultation)
admin.site.register(Prescription)
admin.site.register(Medication)