from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, Doctor, Consultation, Office, OfficeSupply
from .forms import PatientForm, OfficeSupplyForm

# --- CRUD PACIENTE (EJERCICIO 7) ---

def patient_list(request):
    patients = Patient.objects.select_related('medical_history').all().order_by('last_name')
    return render(request, 'clinic/patient_list.html', {'patients': patients})

def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'clinic/patient_form.html', {'form': form, 'title': 'Registrar Paciente'})

def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'clinic/patient_form.html', {'form': form, 'title': 'Editar Paciente'})

def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'clinic/patient_confirm_delete.html', {'patient': patient})


# --- CONSULTAS OPTIMIZADAS (EJERCICIO 6 Y 12) ---

def doctor_consultations_view(request):
    doctors = Doctor.objects.prefetch_related('consultation_set__patient').all()
    return render(request, 'clinic/doctor_consultations.html', {'doctors': doctors})

def expanded_relations_view(request):
    consultations = Consultation.objects.select_related('doctor', 'patient').all()
    offices = Office.objects.prefetch_related('officesupply_set__supply').all()
    return render(request, 'clinic/expanded_relations.html', {
        'consultations': consultations,
        'offices': offices,
    })


# --- CRUD MODELO INTERMEDIO OFFICESUPPLY (EJERCICIO 13) ---

# Listar insumos asignados
def office_supply_list(request):
    items = OfficeSupply.objects.select_related('office', 'supply').all()
    return render(request, 'clinic/office_supply_list.html', {'items': items})

# Asignar nuevo insumo
def office_supply_create(request):
    if request.method == 'POST':
        form = OfficeSupplyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('office_supply_list')
    else:
        form = OfficeSupplyForm()
    return render(request, 'clinic/office_supply_form.html', {'form': form, 'title': 'Asignar Insumo a Consultorio'})

# Editar asignación
def office_supply_update(request, pk):
    item = get_object_or_404(OfficeSupply, pk=pk)
    if request.method == 'POST':
        form = OfficeSupplyForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('office_supply_list')
    else:
        form = OfficeSupplyForm(instance=item)
    return render(request, 'clinic/office_supply_form.html', {'form': form, 'title': 'Editar Asignación de Insumo'})

# Eliminar asignación
def office_supply_delete(request, pk):
    item = get_object_or_404(OfficeSupply, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('office_supply_list')
    return render(request, 'clinic/office_supply_confirm_delete.html', {'item': item})