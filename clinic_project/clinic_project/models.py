from django.db import models

class Doctor(models.Model):
  name = models.CharField(max_length=100)
  specialization = models.CharField(max_length=100)
  experience = models.CharField(max_length=100)
  def __str__(self):
    return self.name

class Patient(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()

class Appointment(models.Model):
  doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  date = models.DateField()
  time = models.TimeField()