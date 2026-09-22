from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm

def appointment_list(request):
    appointments = Appointment.objects.all().order_by('-date')
    return render(request, 'list.html', {'appointments': appointments})

def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'create.html', {'form': form})