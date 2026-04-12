from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  ROLE_CHOICES = (
    ('doctor', 'Doctor'),
    ('patient', 'Patient'),
  )
  role = models.CharField(max_length=20, choices=ROLE_CHOICES)
  name = models.CharField(max_length=255, blank=True)
  
