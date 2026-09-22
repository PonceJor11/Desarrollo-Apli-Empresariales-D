from django.db import models


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Specialty(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cmp_license = models.CharField(max_length=10, unique=True)
    specialty = models.ForeignKey(Specialty, on_delete=models.PROTECT, related_name='doctors')
    patients = models.ManyToManyField(Patient, through='Consultation', related_name='doctors')

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"


# Entidad 1:1 con Consultation
class Prescription(models.Model):
    consultation = models.OneToOneField(
        'Consultation', 
        on_delete=models.CASCADE, 
        related_name='prescription'
    )
    indications = models.TextField()
    issued_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Receta de Consulta #{self.consultation.id}"

# Entidades para N:M ampliado con modelo intermedio
class MedicalSupply(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Office(models.Model):
    code = models.CharField(max_length=10, unique=True)
    floor = models.IntegerField()
    supplies = models.ManyToManyField(
        MedicalSupply, 
        through='OfficeSupply', 
        related_name='offices'
    )

    def __str__(self):
        return f"Consultorio {self.code}"

class OfficeSupply(models.Model):
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    supply = models.ForeignKey(MedicalSupply, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # Atributo propio 1
    last_restock = models.DateField(auto_now=True)     # Atributo propio 2

    def __str__(self):
        return f"{self.supply} en {self.office} ({self.quantity} und.)"


class MedicalHistory(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name='medical_history')
    blood_type = models.CharField(max_length=5)
    allergies = models.TextField(blank=True, default="Ninguna")
    chronic_diseases = models.TextField(blank=True, default="Ninguna")

    def __str__(self):
        return f"Historia Clínica de {self.patient}"


class MedicalAppointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateTimeField()
    reason = models.CharField(max_length=255)

    def __str__(self):
        return f"Cita de {self.patient}"


class Consultation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    consultation_date = models.DateField(auto_now_add=True)
    diagnosis = models.TextField()

    def __str__(self):
        return f"Consulta: {self.doctor} - {self.patient}"


class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='prescriptions')
    issued_date = models.DateField(auto_now_add=True)
    indications = models.TextField()

    def __str__(self):
        return f"Receta de {self.patient}"


class Medication(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name='medications')
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.dosage}"