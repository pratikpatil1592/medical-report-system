from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(max_length=50, null=True, blank=True, default=None)
    age = models.IntegerField(null=True, default=None)
    address = models.TextField(null=True, default=None)
    patient_name = models.CharField(null=True, max_length=100, default=None)
    patient_relation = models.CharField(null=True, max_length=15, default=None)
    phone_number = models.CharField(null=True, max_length=13, default=None)

    def __str__(self):
        return self.email