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
    Medication,
    OfficeSupply
)

# --- Punto 6: StackedInline (Relación 1:1) ---
class MedicalHistoryInline(admin.StackedInline):
    model = MedicalHistory
    extra = 1

# --- Punto 7: TabularInline (Relación N:M) ---
class OfficeSupplyInline(admin.TabularInline):
    model = OfficeSupply
    extra = 1

# --- Puntos 2, 3, 4 y 5: ModelAdmin Personalizados (3 clases) ---

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'dni') # Punto 3
    search_fields = ('first_name', 'last_name', 'dni')      # Punto 4
    inlines = [MedicalHistoryInline]                       # Punto 6

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')        # Punto 3
    list_filter = ('specialty',)                           # Punto 5

@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('id',)                                 # Punto 3
    inlines = [OfficeSupplyInline]                         # Punto 7

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('id', 'diagnosis')
    search_fields = ('diagnosis',)

# --- Punto 1: Registro simple del resto de los modelos ---
admin.site.register(Specialty)
admin.site.register(MedicalSupply)
admin.site.register(MedicalAppointment)
admin.site.register(Prescription)
admin.site.register(Medication)