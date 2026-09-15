from django.db import models

class Appointment(models.Model):
    pet_name = models.CharField(max_length=100, verbose_name="Nombre de la Mascota")
    species = models.CharField(max_length=50, verbose_name="Especie")
    owner_name = models.CharField(max_length=100, verbose_name="Nombre del Dueño")
    reason = models.TextField(verbose_name="Motivo de Consulta")
    date = models.DateField(verbose_name="Fecha de Atención")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")

    def __str__(self):
        return f"Cita de {self.pet_name} - {self.date}"