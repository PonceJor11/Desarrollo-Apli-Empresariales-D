from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class MedicalSupply(models.Model):
    name = models.CharField(max_length=120)
    stock = models.IntegerField(default=0)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class Office(models.Model):
    code = models.CharField(max_length=10, unique=True)
    floor = models.IntegerField()

    def __str__(self):
        return f"Consultorio {self.code}"

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

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"