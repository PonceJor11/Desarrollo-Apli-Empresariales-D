from django.shortcuts import render, redirect
from .models import APPOINTMENTS_DATA
from .forms import AppointmentForm

def appointment_list(request):
    return render(request, 'veterinary/list.html', {'appointments': APPOINTMENTS_DATA})

def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            new_id = len(APPOINTMENTS_DATA) + 1
            new_appointment = {
                "id": new_id,
                "pet_name": form.cleaned_data['pet_name'],
                "species": form.cleaned_data['species'],
                "owner_name": form.cleaned_data['owner_name'],
                "reason": form.cleaned_data['reason'],
                "date": str(form.cleaned_data['date']),
            }
            APPOINTMENTS_DATA.append(new_appointment)
            return redirect('veterinary:list')
    else:
        form = AppointmentForm()

    return render(request, 'veterinary/create.html', {'form': form})