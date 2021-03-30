from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from datetime import datetime

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



def patient_report_directory_path(instance, filename):
    return 'patient/{0}-{1}/{2}_{3}'.format(instance.user.id, instance.user.patient_name, int(datetime.now().timestamp()), filename)

class FileUpload(models.Model):
    file = models.FileField(upload_to=patient_report_directory_path, blank=False, null=False, default=None)
    remark = models.CharField(max_length=50, default=None)
    description = models.TextField(default=None)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)